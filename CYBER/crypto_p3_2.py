import socket
import time
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP

# load public key
with open("public.pem", "rb") as f:
    public_key = RSA.import_key(f.read())

cipher = PKCS1_OAEP.new(public_key)

message = b"This is a secret message from Bob to Alice."

start = time.time()
encrypted_data = cipher.encrypt(message)
end = time.time()

print("Encryption time:", end - start)

client = socket.socket()
client.connect(("localhost", 9999))
client.send(encrypted_data)
client.close()

print("Encrypted message sent")
