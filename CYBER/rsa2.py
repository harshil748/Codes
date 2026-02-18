from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import time

# load public key
with open("public.pem", "rb") as f:
    key = RSA.import_key(f.read())

cipher = PKCS1_OAEP.new(key)

# read file
with open("sample.txt", "rb") as f:
    data = f.read()

start = time.time()
encrypted = cipher.encrypt(data[:86])  # RSA block size limitation
end = time.time()

with open("encrypted.bin", "wb") as f:
    f.write(encrypted)

print("Encryption time:", end - start)
