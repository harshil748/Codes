def xor_decrypt(data, key):
    return bytes([b ^ key for b in data])


with open("encrypted_data.bin", "rb") as f:
    ciphertext = f.read()

for k in range(256):
    decrypted = xor_decrypt(ciphertext, k)
    if b"FLAG{" in decrypted:
        print(f"[+] Key Found: {k}")
        print(decrypted.decode(errors="ignore"))
        break
