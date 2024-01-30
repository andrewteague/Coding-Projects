######################################################
# Name: Andrew Teague
# Date: 11/30/23
# Purpose: Key Generation, Encryption and Decryption functions to implement RSA
######################################################


import random
from rsa_prereqs import get_prime, ee_alg, fast_mod_exp, mod_inv
from rsa_output import output_keygen


def key_gen(size: int) -> ((int,int) , (int,int)):
    """ a function which accepts the size of n, in bits, as a parameter and returns two tuples
    representing the public and private key"""
    p = get_prime(size // 2)
    q = get_prime(size // 2)
    n = p * q
    ttnt = (p - 1) * (q - 1)
    e = random.randint(3, p - 2)

    while ee_alg(e, ttnt)[0] != 1:
        e = random.randint(3, p - 2)
    d = mod_inv(e, ttnt)
    public_key = (n, e)
    private_key = (n, d)
    output_keygen(p, q, n, ttnt, e, d)
    return public_key, private_key


def encrypt(message: int, key: (int,int)) ->int:
    """Use the fast modular exponentiation function to return the result of messagekey[0]
(mod key[1])"""
    return fast_mod_exp(message, key[1], key[0])


# def decrypt(ciphertext: int, key: (int, int)) -> int:
#     return fast_mod_exp(ciphertext, key[1], key[0])