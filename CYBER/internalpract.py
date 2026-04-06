import hashlib
import secrets


def genrate_shared_key(p: int,p1: int,q: int)-> int:
    return pow(q, p1, p)


def main():
    p = int(input("Enter the public key 1: "))
    q = int(input("Enter the public key 2: "))
    p1 = int(input("Enter the private key 1: "))
    q1 = int(input("Enter the public key 2: "))

    print("Public key 1 is: ", p)
    print("Public key 2 is: ", q)
    print("Private key 1 is: ", p1)
    print("Private key 2 is: ", q1)
    print("Shared key for user 1 is: ", genrate_shared_key(p, p1, q))
    print("Shared key for user 2 is: ", genrate_shared_key(p, q1, p))