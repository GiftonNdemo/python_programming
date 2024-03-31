def encrypt(plaintext, k):
    cyphertext=[]
    for i, j in zip(plaintext, k):
        cyphertext.append(chr(ord(i)^ord(j)))
        
    cypher = ''.join(cyphertext)
    return(cypher) # Do stuff and return ciphertext
    
encrypt("ball", "cake" )
