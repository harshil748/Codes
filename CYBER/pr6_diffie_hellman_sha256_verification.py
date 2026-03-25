import hashlib
import secrets


def generate_private_key(p: int) -> int:
    """Return a random private key in range [2, p-2]."""
    return secrets.randbelow(p - 3) + 2


def generate_public_key(g: int, private_key: int, p: int) -> int:
    """Compute public key: g^private_key mod p."""
    return pow(g, private_key, p)


def compute_shared_secret(other_public_key: int, own_private_key: int, p: int) -> int:
    """Compute shared secret: other_public_key^own_private_key mod p."""
    return pow(other_public_key, own_private_key, p)


def sha256_hex(text: str) -> str:
    """Return SHA256 hash of input text in hex format."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main() -> None:
    print("PR6: DIFFIE-HELLMAN KEY EXCHANGE + SHA256 HASH VERIFICATION")

    # Public parameters (can be known by everyone)
    p = 23
    g = 5

    print("\n[Public Parameters]")
    print(f"Prime p      : {p}")
    print(f"Generator g  : {g}")

    # Bob and Alice choose private keys independently
    bob_private = generate_private_key(p)
    alice_private = generate_private_key(p)

    # Bob and Alice compute public keys and exchange only these values
    bob_public = generate_public_key(g, bob_private, p)
    alice_public = generate_public_key(g, alice_private, p)

    print("\n[Key Generation]")
    print(f"Bob private key (secret)   : {bob_private}")
    print(f"Alice private key (secret) : {alice_private}")
    print(f"Bob public key (sent)      : {bob_public}")
    print(f"Alice public key (sent)    : {alice_public}")

    # Both compute the same shared secret without sending it
    bob_secret = compute_shared_secret(alice_public, bob_private, p)
    alice_secret = compute_shared_secret(bob_public, alice_private, p)

    print("\n[Shared Secret Computation]")
    print(f"Bob computed secret s   : {bob_secret}")
    print(f"Alice computed secret s : {alice_secret}")
    print(f"Secrets match?          : {bob_secret == alice_secret}")

    # Bob sends message M and hash H(M||s)
    message = "Hello Alice, payment approved for INR 25000."
    bob_hash = sha256_hex(message + str(bob_secret))

    print("\n[Bob -> Alice]")
    print(f"Message M               : {message}")
    print(f"Hash H(M||s) sent       : {bob_hash}")

    # Alice verifies by recomputing H(M||s)
    alice_computed_hash = sha256_hex(message + str(alice_secret))
    verified = alice_computed_hash == bob_hash

    print("\n[Alice Verification]")
    print(f"Alice computed H(M||s)  : {alice_computed_hash}")
    print(f"Received H(M||s)        : {bob_hash}")
    print(f"Integrity Check         : {'PASS' if verified else 'FAIL'}")

    # Optional tampering demonstration
    tampered_message = "Hello Alice, payment approved for INR 95000."
    tampered_hash = sha256_hex(tampered_message + str(alice_secret))
    tampering_detected = tampered_hash != bob_hash

    print("\n[Tampering Demo]")
    print(f"Tampered message        : {tampered_message}")
    print(f"Tampered H(M||s)        : {tampered_hash}")
    print(f"Tampering detected?     : {tampering_detected}")

    


if __name__ == "__main__":
    main()
