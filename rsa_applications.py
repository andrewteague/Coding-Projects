######################################################
# Name: Andrew Teague
# Date: 11/30/23
# Purpose: demonstrate a few mock applications of RSA
######################################################


import random
from rsa_core import key_gen, encrypt
from rsa_output import dig_sig_output, dig_cert_output, authentication_output
import hashlib


def dig_sig(message: str, priv_key: (int,int)) -> str:
    """ used to verify that a private key corresponding to some known public key was used to send a message"""
    hash_bytes = hashlib.sha256(message.encode('utf-8')).digest()
    hash_int = int.from_bytes(hash_bytes, byteorder='big')
    signature = encrypt(hash_int, priv_key)
    dig_sig_output(message, hash, hash_int, str(signature))
    return str(signature)



def dig_cert(name: str, pub_key: (int,int), signing_key: (int,int)) -> str:
    """binds a public key to an identity and is digitally signed by a trusted,
known entity"""
    message = f"{name} {str(pub_key)}"
    digital_signature = dig_sig(message, signing_key)
    dig_cert_output(message, signing_key, digital_signature)
    return f"{message} {digital_signature}"



def authentication(name: str, pub_key: (int,int),  priv_key: (int,int) , signing_key: (int,int),
                   verification_key: (int,int)) -> bool:
    certificate = dig_cert(name, pub_key, signing_key)
    verification_num = random.randint(1, 1000000)
    encrypted_num = encrypt(verification_num, pub_key)
    decrypted_num = encrypt(encrypted_num, priv_key)
    authentication_output(name, pub_key, priv_key, signing_key, verification_key,
                          certificate, verification_num, encrypted_num, decrypted_num)
    return verification_num == decrypted_num