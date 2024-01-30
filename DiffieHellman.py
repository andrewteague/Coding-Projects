######################################################
# Name: Andrew Teague
# Date: 11/21/23
# Purpose: Implement the Diffie Hellman key exchange protocol
######################################################
import secrets
import random


def fast_mod_exp(base: int, power: int, modulus: int) -> int:
    """an efficient algorithm for computing very large exponents mod some value"""
    result = 1

    while power > 0:
        if power % 2 == 1:
            result = (result * base) % modulus
            # result = result % modulus
        power = power // 2
        base = (base * base) % modulus
        # base = base % modulus

    return result


def miller_rabin_test(number: int, base: int) -> bool:
    """True if the number passes the test and is a strong pseudo prime, False if the number fails
the test and is proven composite"""
    # First Part: Compute s and t so that number – 1 = 2s * t
    s = 0
    t = number - 1
    while t % 2 == 0 and t > 0:
        t //= 2
        s += 1
    # Second Part: test if base^t (mod number) equals 1
    if fast_mod_exp(base, t, number) == 1:
        return True
    # Third Part: test if base^t * 2**I (mod number) is negative 1 for i in range (0, s-1) inclusive
    for i in range(s):
        if fast_mod_exp(base , t * (2**i), number) == number -1:
            return True

    return False


def get_prime(size: int) -> int:
    """getting q, a strong pseudo prime of the form 2*prime + 1"""
    passed = False
    while not passed:
        passed = True
        # random number q divided by 2 bits long
        prime = secrets.randbits(size // 2)
        # a list of 10 different random numbers between [2, prime-2]
        bases = [random.randint(2, prime - 2) for _ in range(10)]
        # check if q is a strong pseudo prime
        for base in bases:
            if not miller_rabin_test(prime, base):
                passed = False
                break
        # check if 2q + 1 is also prime
        if passed:
            for base in bases:
                if not miller_rabin_test(2 * prime + 1, base):
                    passed = False
                    break

    return 2 * prime + 1


def get_generator(prime: int) -> int:
    """ getting g, a generator of the cyclic group"""
    q = (prime - 1) // 2
    while True:
        g = random.randint(1, prime - 2)
        result = fast_mod_exp(g, q, prime)

        if result !=1:
            return g


def main() -> None:
    # Choose a prime number P
    # prime = 9974897320593393323034444433565936803804995634370485307
    prime = get_prime(365)
    print(f"Prime (P): {prime}")
    # Choose a generator G
    # generator = 5938482824295760067713474569266958157940183991385599526
    generator = get_generator(prime)
    print(f"Generator (G): {generator}")
    print('-' * 70)

    # Choose random numbers X and Y
    # X = 6563359795332039407511865330133038027964348794933377294
    X = random.randint(2, prime - 1)
    Y = random.randint(2, prime - 1)
    print(f"Random number X: {X}")
    print(f"Random number Y: {Y}")
    print('-' * 70)

    # Compute A and B
    A = fast_mod_exp(generator, X, prime)
    # B = 9404306422332471559440471122636214005275923029040639985
    B = fast_mod_exp(generator, Y, prime)
    print(f"A = G^X mod P: {A}")
    print(f"B = G^Y mod P: {B}")
    print('-' * 70)

    # Compute Key1 and Key2
    Key1 = fast_mod_exp(B, X, prime)
    Key2 = fast_mod_exp(A, Y, prime)
    print(f"Key1 = B^X mod P: {Key1}")
    print(f"Key2 = A^Y mod P: {Key2}")
    print('-' * 70)

    # Check if Key1 equals Key2
    keys_match = Key1 == Key2
    print(f"T/F Key1 and Key2 match: {keys_match}")

if __name__ == "__main__":
    main()