'''
Affine cipher is a type of monoalphabetic substitution cipher, wherein each letter in an alphabet 
is mapped to its numeric equivalent, encrypted using a simple mathematical function, 
and converted back to a letter.
It uses modular arithmetic to transform the integer that each plaintext letter 
corresponds to into another integer that correspond to a ciphertext letter. 
The encryption function for a single letter is
E ( x ) = ( k1 x + k2) mod m 
modulus m: size of the alphabet
k1 and k2: key of the cipher.
k1 must be chosen such that k1 and m are coprime.
'''

#extended euclidian algorithm to find modular inverse
def egcd(k1,k2):  
    x,y,u,v=0,1,1,0
    while k1!=0:
        q,r=k2//k1,k2%k1
        m,n=x-u*q,y-v*q
        k2,k1,x,y,u,v=k1,r,u,v,m,n
    gcd=k2
    return gcd, x, y

def modinv(k1,m):
    gcd, x, y = egcd(k1,m)
    if gcd!=1:
        return None
    else:
        return x % m
    
def encrypt_affline(message, key):
    translated = ''
    for t in message.upper():
        if t == ' ':
            translated += ' '
        else:
            translated += chr(((key[0] * (ord(t) - ord('A')) + key[1]) % 26) + ord('A'))
    return translated

def decrypt_affline(translated, key):
    message = ''
    mod_inv = modinv(key[0], 26)
    for t in translated.upper():
        if t == ' ':
            message += ' '
        else:
            message += chr(((mod_inv * (ord(t) - ord('A') - key[1])) % 26) + ord('A'))
    return message

def main():
    message = "This is a message"
    key=[3,5]
    print("Encrypted Text: ", format(encrypt_affline(message,key)))
    print("Decrypted Text: ", format(decrypt_affline(encrypt_affline(message,key),key)))

if __name__ == "__main__":
    main()