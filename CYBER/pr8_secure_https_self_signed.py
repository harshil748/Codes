import argparse
import os
import subprocess
import ssl
from http.server import HTTPServer, SimpleHTTPRequestHandler


def generate_self_signed_cert(
    cert_file: str, key_file: str, common_name: str, days: int
) -> None:
    cert_dir = os.path.dirname(cert_file)
    key_dir = os.path.dirname(key_file)
    if cert_dir:
        os.makedirs(cert_dir, exist_ok=True)
    if key_dir:
        os.makedirs(key_dir, exist_ok=True)

    cmd = [
        "openssl",
        "req",
        "-x509",
        "-newkey",
        "rsa:2048",
        "-sha256",
        "-days",
        str(days),
        "-nodes",
        "-keyout",
        key_file,
        "-out",
        cert_file,
        "-subj",
        f"/CN={common_name}",
    ]

    subprocess.run(cmd, check=True)


def build_https_server(
    host: str, port: int, cert_file: str, key_file: str
) -> HTTPServer:
    server = HTTPServer((host, port), SimpleHTTPRequestHandler)

    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile=cert_file, keyfile=key_file)
    server.socket = context.wrap_socket(server.socket, server_side=True)

    return server


def main() -> None:
    parser = argparse.ArgumentParser(
        description="PR8: Run HTTPS server with self-signed SSL certificate (lab/testing use)."
    )
    parser.add_argument(
        "--host", default="127.0.0.1", help="Server host (default: 127.0.0.1)"
    )
    parser.add_argument(
        "--port", type=int, default=4443, help="HTTPS port (default: 4443)"
    )
    parser.add_argument(
        "--cert",
        default="certs/server.crt",
        help="Path to certificate file (default: certs/server.crt)",
    )
    parser.add_argument(
        "--key",
        default="certs/server.key",
        help="Path to private key file (default: certs/server.key)",
    )
    parser.add_argument(
        "--cn", default="localhost", help="Certificate Common Name (default: localhost)"
    )
    parser.add_argument(
        "--days", type=int, default=365, help="Certificate validity in days"
    )
    parser.add_argument(
        "--regen",
        action="store_true",
        help="Regenerate certificate/key even if files already exist",
    )

    args = parser.parse_args()

    cert_exists = os.path.exists(args.cert)
    key_exists = os.path.exists(args.key)

    if args.regen or not (cert_exists and key_exists):
        print("[Setup] Generating self-signed certificate...")
        try:
            generate_self_signed_cert(args.cert, args.key, args.cn, args.days)
        except FileNotFoundError:
            print("[Error] OpenSSL is not installed or not available in PATH.")
            print("Install OpenSSL first, then rerun this script.")
            return
        except subprocess.CalledProcessError as exc:
            print(f"[Error] Certificate generation failed: {exc}")
            return
    else:
        print("[Setup] Using existing certificate and key.")

    print("\nStarting HTTPS server with self-signed certificate")
    print(f"Host: {args.host}")
    print(f"Port: {args.port}")
    print(f"Certificate: {args.cert}")
    print(f"Private Key: {args.key}")

    print("\n[How to test]")
    print(f"1. Browser: https://{args.host}:{args.port}")
    print("3. CLI test:")
    print(f"   curl -k https://{args.host}:{args.port}")



    try:
        server = build_https_server(args.host, args.port, args.cert, args.key)
        print("\n[Running] Press Ctrl+C to stop server.")
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[Stop] HTTPS server stopped.")
    except OSError as exc:
        print(f"[Error] Could not start server: {exc}")


if __name__ == "__main__":
    main()