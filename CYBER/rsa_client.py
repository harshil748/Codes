import socket
import time

from rsa_utils import encrypt_int, message_to_int


HOST = "127.0.0.1"
PORT = 5000


def _recvline(fileobj):
    line = fileobj.readline()
    if not line:
        raise ConnectionError("connection closed")
    return line.rstrip(b"\n").decode("ascii")


def main():
    message = (
        "Hello Alice, this is Bob. Sending a short RSA-encrypted message over sockets."
    )
    message_bytes = message.encode("utf-8")

    with socket.create_connection((HOST, PORT)) as sock:
        fileobj = sock.makefile("rwb")

        n = int(_recvline(fileobj))
        e = int(_recvline(fileobj))
        n_bytes = (n.bit_length() + 7) // 8
        if len(message_bytes) >= n_bytes:
            raise ValueError("message too long for textbook RSA block")

        m = message_to_int(message_bytes)
        start = time.perf_counter()
        c = encrypt_int(m, n, e)
        encrypt_time = time.perf_counter() - start

        fileobj.write(f"{c}\n".encode("ascii"))
        fileobj.write(f"{len(message_bytes)}\n".encode("ascii"))
        fileobj.flush()

        ack = _recvline(fileobj)
        print(f"Encryption time: {encrypt_time:.6f} s")
        print(f"Server response: {ack}")


if __name__ == "__main__":
    main()
