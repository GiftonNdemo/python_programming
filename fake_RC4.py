def get_prg(plaintext_size, k):
    i=j=0
    key=[ord(c)for c in k]
    keystream = []
    for _ in range(plaintext_size):
            i=(i+1)%32
            j=(j+key[i])%32
            key[i], key[j] = key[j], key[i]
            keystream.append(chr(key[(key[i]+key[j])%32]))
            
    return ''.join(keystream)# return keystream

def fake_rc4(plaintext, keystream):
    cyphertext = []
    for txt, ks in zip(plaintext, keystream):
        ks = ord(ks)  # Convert keystream character to ASCII value
        cyphertext.append(chr(ord(txt) ^ ks))
    cypherword = ''.join(cyphertext)
    return cypherword# return ciphertext
