import hashlib
import secrets


def generate_private_key(p: int) -> int:
    return secrets.randbelow(p - 3) + 2


def generate_public_key(g: int, private_key: int, p: int) -> int:
    return pow(g, private_key, p)


def compute_shared_secret(other_public_key: int, own_private_key: int, p: int) -> int:
    return pow(other_public_key, own_private_key, p)


def sha256_hex(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main() -> None:
    print("PR6: DIFFIE-HELLMAN KEY EXCHANGE + SHA256 HASH VERIFICATION")

    p = 23
    g = 5

    print("\n[Public Parameters]")
    print(f"Prime p      : {p}")
    print(f"Generator g  : {g}")

    bob_private = generate_private_key(p)
    alice_private = generate_private_key(p)

    bob_public = generate_public_key(g, bob_private, p)
    alice_public = generate_public_key(g, alice_private, p)

    print("\n[Key Generation]")
    print(f"Bob private key (secret)   : {bob_private}")
    print(f"Alice private key (secret) : {alice_private}")
    print(f"Bob public key (sent)      : {bob_public}")
    print(f"Alice public key (sent)    : {alice_public}")

    bob_secret = compute_shared_secret(alice_public, bob_private, p)
    alice_secret = compute_shared_secret(bob_public, alice_private, p)

    print("\n[Shared Secret Computation]")
    print(f"Bob computed secret s   : {bob_secret}")
    print(f"Alice computed secret s : {alice_secret}")
    print(f"Secrets match?          : {bob_secret == alice_secret}")

    message = "Hello Alice, payment approved for INR 25000."
    bob_hash = sha256_hex(message + str(bob_secret))

    print("\n[Bob -> Alice]")
    print(f"Message M               : {message}")
    print(f"Hash H(M||s) sent       : {bob_hash}")

    alice_computed_hash = sha256_hex(message + str(alice_secret))
    verified = alice_computed_hash == bob_hash

    print("\n[Alice Verification]")
    print(f"Alice computed H(M||s)  : {alice_computed_hash}")
    print(f"Received H(M||s)        : {bob_hash}")
    print(f"Integrity Check         : {'PASS' if verified else 'FAIL'}")

    tampered_message = "Hello Alice, payment approved for INR 95000."
    tampered_hash = sha256_hex(tampered_message + str(alice_secret))
    tampering_detected = tampered_hash != bob_hash

    print("\n[Tampering Demo]")
    print(f"Tampered message        : {tampered_message}")
    print(f"Tampered H(M||s)        : {tampered_hash}")
    print(f"Tampering detected?     : {tampering_detected}")

    


if __name__ == "__main__":
    main()
