import os
import secrets
import time


def _egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = _egcd(b % a, a)
    return (g, x - (b // a) * y, y)


def _modinv(a, m):
    g, x, _ = _egcd(a, m)
    if g != 1:
        raise ValueError("modular inverse does not exist")
    return x % m


def _is_probable_prime(n, k=40):
    if n < 2:
        return False
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for p in small_primes:
        if n % p == 0:
            return n == p

    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Miller-Rabin test rounds
    for _ in range(k):
        a = secrets.randbelow(n - 3) + 2
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def generate_prime(bits):
    while True:
        candidate = secrets.randbits(bits)
        candidate |= (1 << (bits - 1)) | 1
        if _is_probable_prime(candidate):
            return candidate


def generate_keypair(bits=1024):
    start = time.perf_counter()
    e = 65537
    while True:
        p = generate_prime(bits // 2)
        q = generate_prime(bits // 2)
        if p == q:
            continue
        phi = (p - 1) * (q - 1)
        if phi % e != 0:
            break
    n = p * q
    d = _modinv(e, phi)
    elapsed = time.perf_counter() - start
    return (n, e, d, elapsed)


def message_to_int(message_bytes):
    return int.from_bytes(message_bytes, byteorder="big")


def int_to_message(value, length):
    return value.to_bytes(length, byteorder="big")


def encrypt_int(m, n, e):
    if m <= 0 or m >= n:
        raise ValueError("message integer out of range for RSA modulus")
    return pow(m, e, n)


def decrypt_int(c, n, d):
    return pow(c, d, n)


def system_info():
    return {
        "os": os.name,
        "cpu_count": os.cpu_count(),
    }
