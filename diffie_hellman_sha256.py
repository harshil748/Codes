def power(a, b, p):
    if b == 1:
        return a
    else:
        return pow(a, b) % p


def main():
    P = 23
    print("The value of P:", P)
    G = 5
    print("The value of G:", G)
    a = 4
    print("The private key a for Alice:", a)
    x = power(G, a, P)
    b = 3
    print("The private key b for Bob:", b)
    y = power(G, b, P)
    ka = power(y, a, P)
    kb = power(x, b, P)

    print("Secret key for Alice is:", ka)
    print("Secret key for Bob is:", kb)


if __name__ == "__main__":
    main()