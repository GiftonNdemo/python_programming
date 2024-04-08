from Crypto.Cipher import ARC4

def rc4(plaintext, key):
    cipher = ARC4.new(key)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext
