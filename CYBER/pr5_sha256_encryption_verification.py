import base64
import hashlib
import json
from dataclasses import dataclass

try:
    from Cryptodome.Cipher import AES
    from Cryptodome.Random import get_random_bytes
except ImportError:
    from Crypto.Cipher import AES
    from Crypto.Random import get_random_bytes


@dataclass
class EncryptedPacket:
    nonce_b64: str
    ciphertext_b64: str
    tag_b64: str


def sha256_hex(message: str) -> str:
    return hashlib.sha256(message.encode("utf-8")).hexdigest()


def encrypt_bundle(secret_key: bytes, message: str) -> EncryptedPacket:
    message_hash = sha256_hex(message)

    bundle = {
        "message": message,
        "hash": message_hash,
    }
    plain_bytes = json.dumps(bundle).encode("utf-8")

    cipher = AES.new(secret_key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(plain_bytes)

    return EncryptedPacket(
        nonce_b64=base64.b64encode(cipher.nonce).decode("utf-8"),
        ciphertext_b64=base64.b64encode(ciphertext).decode("utf-8"),
        tag_b64=base64.b64encode(tag).decode("utf-8"),
    )


def decrypt_bundle(secret_key: bytes, packet: EncryptedPacket) -> dict:
    nonce = base64.b64decode(packet.nonce_b64)
    ciphertext = base64.b64decode(packet.ciphertext_b64)
    tag = base64.b64decode(packet.tag_b64)

    cipher = AES.new(secret_key, AES.MODE_GCM, nonce=nonce)
    plain_bytes = cipher.decrypt_and_verify(ciphertext, tag)

    return json.loads(plain_bytes.decode("utf-8"))


def verify_integrity(received_message: str, received_hash: str) -> bool:
    computed_hash = sha256_hex(received_message)
    return computed_hash == received_hash


def main() -> None:
    print("ENCRYPTION + SHA256 INTEGRITY VERIFICATION")
    secret_key = get_random_bytes(32)

    message = "Bank transfer approved: INR 25,000 to account X123."

    print("\n[Bob] Original Message (M):")
    print(message)
    packet = encrypt_bundle(secret_key, message)

    print("\n[Bob] Encrypted bundle sent to Alice:")
    print(f"nonce       : {packet.nonce_b64}")
    print(f"ciphertext  : {packet.ciphertext_b64}")
    print(f"auth tag    : {packet.tag_b64}")

    decrypted_data = decrypt_bundle(secret_key, packet)
    received_message = decrypted_data["message"]
    received_hash = decrypted_data["hash"]

    print("\n[Alice] Decrypted data:")
    print(f"Received Message M : {received_message}")
    print(f"Received Hash H(M) : {received_hash}")

    is_valid = verify_integrity(received_message, received_hash)
    computed_hash = sha256_hex(received_message)

    print("\n[Alice] Hash Verification:")
    print(f"Computed Hash H(M) : {computed_hash}")
    print(f"Received Hash H(M) : {received_hash}")
    print(
        f"Integrity Check    : {'PASS (Message not altered)' if is_valid else 'FAIL (Message altered)'}"
    )

    tampered_message = received_message.replace("25,000", "95,000")
    tampered_valid = verify_integrity(tampered_message, received_hash)

    print("\n[Tampering Demo]")
    print(f"Tampered Message   : {tampered_message}")
    print(
        f"Integrity Check    : {'PASS' if tampered_valid else 'FAIL (Tampering detected)'}"
    )


if __name__ == "__main__":
    main()
