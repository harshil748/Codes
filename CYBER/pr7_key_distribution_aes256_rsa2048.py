import base64
import json
import secrets
import socket
import threading
import time
from typing import Dict, List, Tuple

try:
    from Cryptodome.Cipher import AES, PKCS1_OAEP
    from Cryptodome.PublicKey import RSA
except ImportError:
    from Crypto.Cipher import AES, PKCS1_OAEP
    from Crypto.PublicKey import RSA


HOST = "127.0.0.1"
PORT = 9107


class KeyDistributionServer:

    def __init__(self) -> None:
        self.public_keys: Dict[str, bytes] = {}
        self.deliveries: Dict[str, List[dict]] = {}
        self.session_counter = 0
        self.lock = threading.Lock()

    def handle_request(self, request: dict) -> dict:
        action = request.get("action")

        if action == "REGISTER":
            node_id = request["node_id"]
            pem = request["public_key_pem"].encode("utf-8")
            with self.lock:
                self.public_keys[node_id] = pem
                self.deliveries.setdefault(node_id, [])
            return {"status": "ok", "message": f"{node_id} registered"}

        if action == "REQUEST_SESSION":
            source = request["source"]
            destination = request["destination"]

            with self.lock:
                if (
                    source not in self.public_keys
                    or destination not in self.public_keys
                ):
                    return {
                        "status": "error",
                        "message": "Both nodes must register first",
                    }

                self.session_counter += 1
                session_id = f"S{self.session_counter:04d}"

                aes_key = secrets.token_bytes(32)

                src_pub = RSA.import_key(self.public_keys[source])
                dst_pub = RSA.import_key(self.public_keys[destination])

                src_cipher = PKCS1_OAEP.new(src_pub)
                dst_cipher = PKCS1_OAEP.new(dst_pub)

                enc_key_for_source = src_cipher.encrypt(aes_key)
                enc_key_for_destination = dst_cipher.encrypt(aes_key)

                package_for_source = {
                    "session_id": session_id,
                    "with_node": destination,
                    "encrypted_aes_key_b64": base64.b64encode(
                        enc_key_for_source
                    ).decode("utf-8"),
                }
                package_for_destination = {
                    "session_id": session_id,
                    "with_node": source,
                    "encrypted_aes_key_b64": base64.b64encode(
                        enc_key_for_destination
                    ).decode("utf-8"),
                }

                self.deliveries[source].append(package_for_source)
                self.deliveries[destination].append(package_for_destination)

            return {
                "status": "ok",
                "session_id": session_id,
                "message": f"Fresh AES-256 key generated and shared for {source}<->{destination}",
            }

        if action == "POLL_KEYS":
            node_id = request["node_id"]
            with self.lock:
                pending = self.deliveries.get(node_id, [])
                self.deliveries[node_id] = []
            return {"status": "ok", "keys": pending}

        return {"status": "error", "message": "Unknown action"}


def send_json(sock: socket.socket, payload: dict) -> None:
    data = json.dumps(payload).encode("utf-8")
    sock.sendall(len(data).to_bytes(4, "big") + data)


def recv_json(sock: socket.socket) -> dict:
    raw_len = sock.recv(4)
    if not raw_len:
        return {}
    msg_len = int.from_bytes(raw_len, "big")
    data = b""
    while len(data) < msg_len:
        chunk = sock.recv(msg_len - len(data))
        if not chunk:
            break
        data += chunk
    return json.loads(data.decode("utf-8"))


def run_kds_server(stop_event: threading.Event) -> None:
    kds = KeyDistributionServer()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
        srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv.bind((HOST, PORT))
        srv.listen(5)
        srv.settimeout(0.5)

        print(f"[KDS] Key-sharing server running on {HOST}:{PORT}")

        while not stop_event.is_set():
            try:
                conn, _ = srv.accept()
            except socket.timeout:
                continue

            with conn:
                request = recv_json(conn)
                response = kds.handle_request(request)
                send_json(conn, response)

        print("[KDS] Server stopped")


def rpc(payload: dict) -> dict:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        send_json(client, payload)
        return recv_json(client)


def register_node(node_id: str, public_key_pem: str) -> None:
    response = rpc(
        {
            "action": "REGISTER",
            "node_id": node_id,
            "public_key_pem": public_key_pem,
        }
    )
    print(f"[{node_id}] Register response: {response}")


def request_new_session(source: str, destination: str) -> str:
    response = rpc(
        {
            "action": "REQUEST_SESSION",
            "source": source,
            "destination": destination,
        }
    )
    print(f"[{source}] Session request response: {response}")
    return response.get("session_id", "")


def poll_encrypted_keys(node_id: str) -> List[dict]:
    response = rpc({"action": "POLL_KEYS", "node_id": node_id})
    return response.get("keys", [])


def decrypt_session_key(private_key: RSA.RsaKey, encrypted_key_b64: str) -> bytes:
    encrypted_key = base64.b64decode(encrypted_key_b64)
    cipher = PKCS1_OAEP.new(private_key)
    return cipher.decrypt(encrypted_key)


def aes_encrypt_message(aes_key: bytes, message: str) -> Tuple[str, str, str]:
    cipher = AES.new(aes_key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(message.encode("utf-8"))
    return (
        base64.b64encode(cipher.nonce).decode("utf-8"),
        base64.b64encode(ciphertext).decode("utf-8"),
        base64.b64encode(tag).decode("utf-8"),
    )


def aes_decrypt_message(
    aes_key: bytes, nonce_b64: str, ciphertext_b64: str, tag_b64: str
) -> str:
    nonce = base64.b64decode(nonce_b64)
    ciphertext = base64.b64decode(ciphertext_b64)
    tag = base64.b64decode(tag_b64)
    cipher = AES.new(aes_key, AES.MODE_GCM, nonce=nonce)
    plain = cipher.decrypt_and_verify(ciphertext, tag)
    return plain.decode("utf-8")


def main() -> None:
    print(
        "PR7: PRACTICAL KEY DISTRIBUTION (KDS + AES-256 SESSION KEY + RSA-2048 SHARING)"
    )

    stop_event = threading.Event()
    server_thread = threading.Thread(
        target=run_kds_server, args=(stop_event,), daemon=True
    )
    server_thread.start()

    time.sleep(0.5)

    node_a_private = RSA.generate(2048)
    node_b_private = RSA.generate(2048)
    node_a_public_pem = node_a_private.publickey().export_key().decode("utf-8")
    node_b_public_pem = node_b_private.publickey().export_key().decode("utf-8")

    print("\n[Setup] Node A and Node B generated RSA-2048 key pairs")

    register_node("NodeA", node_a_public_pem)
    register_node("NodeB", node_b_public_pem)

    session_id = request_new_session("NodeA", "NodeB")

    node_a_packages = poll_encrypted_keys("NodeA")
    node_b_packages = poll_encrypted_keys("NodeB")

    pkg_a = next((p for p in node_a_packages if p["session_id"] == session_id), None)
    pkg_b = next((p for p in node_b_packages if p["session_id"] == session_id), None)

    if pkg_a is None or pkg_b is None:
        print("[Error] Session key package missing")
        stop_event.set()
        server_thread.join(timeout=1)
        return

    node_a_session_key = decrypt_session_key(
        node_a_private, pkg_a["encrypted_aes_key_b64"]
    )
    node_b_session_key = decrypt_session_key(
        node_b_private, pkg_b["encrypted_aes_key_b64"]
    )

    print("\n[Key Distribution Result]")
    print(f"Session ID: {session_id}")
    print(f"Node A session key length: {len(node_a_session_key) * 8} bits")
    print(f"Node B session key length: {len(node_b_session_key) * 8} bits")
    print(
        f"Both nodes received same AES-256 key? {node_a_session_key == node_b_session_key}"
    )

    message = "Hello NodeB, this message uses AES-256 key received from KDS."
    nonce_b64, ciphertext_b64, tag_b64 = aes_encrypt_message(
        node_a_session_key, message
    )

    decrypted_message = aes_decrypt_message(
        node_b_session_key, nonce_b64, ciphertext_b64, tag_b64
    )

    print("\n[Practical Communication Demo]")
    print(f"Original message at Node A : {message}")
    print(f"Decrypted message at Node B: {decrypted_message}")
    print(f"Message transfer success?   : {message == decrypted_message}")

    stop_event.set()
    server_thread.join(timeout=1)

if __name__ == "__main__":
    main()
