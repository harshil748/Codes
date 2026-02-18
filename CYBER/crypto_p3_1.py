import socket
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP

# generate RSA keys
key = RSA.generate(1024)
private_key = key
public_key = key.publickey()

with open("public.pem", "wb") as f:
    f.write(public_key.export_key())

print("Public key generated.")

server = socket.socket()
server.bind(("localhost", 9999))
server.listen(1)

print("Alice waiting for Bob...")

conn, addr = server.accept()
print("Connected:", addr)

encrypted_data = conn.recv(2048)
conn.close()

cipher = PKCS1_OAEP.new(private_key)
decrypted = cipher.decrypt(encrypted_data)

print("Decrypted message:", decrypted.decode())
