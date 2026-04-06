


def generate_shared_key(other_public_key: int, own_private_key: int, p: int) -> int:
    return pow(other_public_key, own_private_key, p)


def check_same_secret_key(alice_secret: int, bob_secret: int) -> bool:
    return alice_secret == bob_secret


def shift_char(ch: str, shift: int) -> str:
    if "A" <= ch <= "Z":
        return chr((ord(ch) - ord("A") + shift) % 26 + ord("A"))
    if "a" <= ch <= "z":
        return chr((ord(ch) - ord("a") + shift) % 26 + ord("a"))
    return ch


def encrypt_message(message: str, key: int) -> str:
    shift = key % 26
    return "".join(shift_char(ch, shift) for ch in message)


def decrypt_message(cipher_text: str, key: int) -> str:
    shift = key % 26
    return "".join(shift_char(ch, -shift) for ch in cipher_text)


def main() -> None:
    print("Diffie-Hellman Shared Key Demo")

    p = int(input("Enter prime modulus p: "))
    alice_private = int(input("Enter Alice private key: "))
    alice_public = int(input("Enter Alice public key: "))
    bob_private = int(input("Enter Bob private key: "))
    bob_public = int(input("Enter Bob public key: "))
    message = input("Enter message to encrypt: ")

    alice_secret = generate_shared_key(bob_public, alice_private, p)
    bob_secret = generate_shared_key(alice_public, bob_private, p)

    print("\nAlice shared key:", alice_secret)
    print("Bob shared key:  ", bob_secret)
    print("Both sides same key?", check_same_secret_key(alice_secret, bob_secret))

    encrypted = encrypt_message(message, alice_secret)
    decrypted = decrypt_message(encrypted, alice_secret)

    print("\nOriginal message:", message)
    print("Encrypted message:", encrypted)
    print("Decrypted message:", decrypted)


if __name__ == "__main__":
    main()
