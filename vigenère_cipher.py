'''
The encryption is done using the Vigenère square or Vigenère table
The table consists of the alphabets written out 26 times in different rows, 
each alphabet shifted cyclically to the left compared to the previous alphabet, 
corresponding to the 26 possible Caesar Ciphers
For generating key, the given keyword is repeated in a circular manner until 
it matches the length of the plain text.
'''

message="This is a message"
key="hack"

def generate_key(msg,key):
    key=list(key)
    if len(key)==len(msg):
        return key
    else:
        for i in range(len(msg)-len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encrypt(msg, key):  # Ei = (Pi + Ki) mod 26
    translated = []
    key = generate_key(msg, key)
    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            translated_chr = chr((ord(char) + ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
        elif char.islower():
            translated_chr = chr((ord(char) + ord(key[i]) - 2 * ord('a')) % 26 + ord('a'))
        else:
            translated_chr = char
        translated.append(translated_chr)
    return "".join(translated)

def decrypt(msg,key):    #Di = (Ei - Ki) mod 26
    decrypted_text=[]
    key=generate_key(msg,key)
    for i in range(len(msg)):
        char=msg[i]
        if char.isupper():
            decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('A'))
        elif char.islower():
            decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('a'))
        else:
            decrypted_char = char
        decrypted_text.append(decrypted_char)
    return "".join(decrypted_text)

print("Encrypted message: ",encrypt(message,key))
print("Decrypted message: ",decrypt(encrypt(message,key),key))