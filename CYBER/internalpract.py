def genrate_shared_key(p: int, own_private_key: int, other_public_key: int) -> int:
    return pow(other_public_key, own_private_key, p)


def shift_char(ch: str, shift: int) -> str:
    if "A" <= ch <= "Z":
        return chr((ord(ch) - ord("A") + shift) % 26 + ord("A"))
    if "a" <= ch <= "z":
        return chr((ord(ch) - ord("a") + shift) % 26 + ord("a"))
    return ch


def encrypt(message: str, key: int) -> str:
    shift = key % 26
    return "".join(shift_char(ch, shift) for ch in message)


def decrypt(cipher_text: str, key: int) -> str:
    shift = key % 26
    return "".join(shift_char(ch, -shift) for ch in cipher_text)


def main():
    p = int(input("Enter common prime modulus p: "))
    p1 = int(input("Enter Alice private key: "))
    pub1 = int(input("Enter Alice public key: "))
    q1 = int(input("Enter Bob private key: "))
    pub2 = int(input("Enter Bob public key: "))
    message = input("Enter the message to encrypt: ")

    shared_key1 = genrate_shared_key(p, p1, pub2)
    shared_key2 = genrate_shared_key(p, q1, pub1)

    print("Prime modulus p is: ", p)
    print("Alice private key is: ", p1)
    print("Alice public key is: ", pub1)
    print("Bob private key is: ", q1)
    print("Bob public key is: ", pub2)
    print("Shared key for Alice is: ", shared_key1)
    print("Shared key for Bob is: ", shared_key2)

    if shared_key1 != shared_key2:
        print("Both sides do not have same secret key.")
        return

    encrypted_message = encrypt(message, shared_key1)
    decrypted_message = decrypt(encrypted_message, shared_key1)

    print("Encrypted message: ", encrypted_message)
    print("Decrypted message: ", decrypted_message)


if __name__ == "__main__":
    main()
