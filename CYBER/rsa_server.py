import socket
import time
import platform

from rsa_utils import (
    decrypt_int,
    generate_keypair,
    int_to_message,
    message_to_int,
    system_info,
)


HOST = "127.0.0.1"
PORT = 5000


def _recvline(fileobj):
    line = fileobj.readline()
    if not line:
        raise ConnectionError("connection closed")
    return line.rstrip(b"\n").decode("ascii")


def main():
    print("Alice (server) starting...")
    print(f"Platform: {platform.platform()}")
    print(f"System: {system_info()}")

    n, e, d, keygen_time = generate_keypair(1024)
    n_bytes = (n.bit_length() + 7) // 8
    print(f"RSA keygen time: {keygen_time:.6f} s")
    print(f"RSA modulus size: {n.bit_length()} bits")

    with socket.create_server((HOST, PORT)) as server:
        print(f"Listening on {HOST}:{PORT}")
        conn, addr = server.accept()
        with conn:
            print(f"Client connected: {addr}")
            fileobj = conn.makefile("rwb")

            # Send public key to client
            fileobj.write(f"{n}\n".encode("ascii"))
            fileobj.write(f"{e}\n".encode("ascii"))
            fileobj.flush()

            # Receive ciphertext as decimal string
            cipher_str = _recvline(fileobj).strip()
            if not cipher_str:
                raise ValueError("empty ciphertext")

            start = time.perf_counter()
            c = int(cipher_str)
            m = decrypt_int(c, n, d)
            decrypt_time = time.perf_counter() - start

            # Recover message length from next line
            msg_len = int(_recvline(fileobj))
            message = int_to_message(m, msg_len)

            print(f"Decryption time: {decrypt_time:.6f} s")
            print("Received message:")
            print(message.decode("utf-8", errors="replace"))

            fileobj.write(b"OK\n")
            fileobj.flush()


if __name__ == "__main__":
    main()
