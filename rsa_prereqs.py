######################################################
# Name: Andrew Teague
# Date: 11/30/23
# Purpose: helper functions to implement RSA
######################################################

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


def mr_test(number: int, base: int) -> bool:
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
    prime = 0
    while not passed:
        passed = True
        # get random number in the specified size
        prime = random.getrandbits(size)
        # a list of 10 different random numbers between [2, 1000]
        bases = random.sample(range(2, 1001), 10)
        # check if q is a strong pseudo prime
        for base in bases:
            if not mr_test(prime, base):
                passed = False
                break
        # Check Miller-Rabin primality test for each base
        if passed:
            for base in bases:
                if not mr_test(prime, base):
                    passed = False
                    break

    return prime


def ee_alg(a: int, b: int) -> (int, int, int):
    q_prev, r_prev, s_prev, t_prev = None, a, 1, 0
    q_curr, r_curr, s_curr, t_curr = a // b, b, 0, 1
    while r_curr > 1:
        r_prev, r_curr = r_curr, r_prev % r_curr
        if r_curr == 0:
            return r_prev, None, None

        q_curr, q_prev = r_prev // r_curr, q_curr
        s_curr, s_prev = s_prev - s_curr * q_prev, s_curr
        t_curr, t_prev = t_prev - t_curr * q_prev, t_curr
    return r_curr, s_curr % b, t_curr % a


def mod_inv(num, modulus):
    return ee_alg(num, modulus)[1]
