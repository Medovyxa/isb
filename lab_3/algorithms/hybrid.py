from algorithms.asymmetric import generate_keys, encrypt_with_rsa, decrypt_with_rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os

def hybrid_encrypt(text, symmetric_key, public_key):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(symmetric_key), modes.CBC(iv))
    encryptor = cipher.encryptor()

    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_text = padder.update(text) + padder.finalize()
    c_text = encryptor.update(padded_text) + encryptor.finalize()

    encrypted_key = encrypt_with_rsa(public_key, symmetric_key)

    return c_text, encrypted_key, iv

def hybrid_decrypt(encrypted_text, encrypted_key, iv, private_key):
    symmetric_key = decrypt_with_rsa(private_key, encrypted_key)

    cipher = Cipher(algorithms.AES(symmetric_key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    padded_text = decryptor.update(encrypted_text) + decryptor.finalize()

    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    text = unpadder.update(padded_text) + unpadder.finalize()
    return text