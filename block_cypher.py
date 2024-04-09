from Crypto.Cipher import AES
from Crypto import Random

def aes_encrypt(plaintext, k):
    iv = Random.new().read(AES.block_size)  # Generate a random IV
    cipher = AES.new(k, AES.MODE_CBC, iv)  # Create a new AES cipher object with CBC mode
    ciphertext = cipher.encrypt(plaintext)  # Encrypt the plaintext
    return iv + ciphertext  # Prepend the IV to the ciphertext


def aes_decrypt(ciphertext, k):
    iv = ciphertext[:AES.block_size]  # Extract the IV from the ciphertext
    cipher = AES.new(k, AES.MODE_CBC, iv)  # Create a new AES cipher object with CBC mode
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])  # Decrypt the ciphertext
    return plaintext.decode('latin1')  # Return the plaintext

'''
Use PyCrypto to encrypt and decrypt with AES-CBC:

    Implement a function encrypt, that given a plaintext and a 16-byte (128bit) key K, picks a random 16-byte (128 bit) IV, and returns a ciphertext encrypted with AES-CBC with the IV prepended to the ciphertext (in bytes).

    You may assume that the plaintext length (in bytes) is a multiple of 16.
    Implement a function decrypt, that given a ciphertext (as formatted by the encrypt function) and a 16-byte (128 bit) key
K, returns the plaintext as decrypted by AES-CBC (in 'latin1').
'''
