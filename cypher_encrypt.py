alphabet = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(plaintext, k):
    encrypted_text = []
    for letter in plaintext:
        if letter in alphabet:
            index = alphabet.find(letter)
            # Perform a cyclic shift
            encrypted_text.append(alphabet[(index - k) % len(alphabet)])
        else:
            # For characters not in alphabet (like spaces), keep them as is
            encrypted_text.append(letter)
    encrypted_word = ''.join(encrypted_text)
    return(encrypted_word)

encrypt('attack at dawn', 5)

