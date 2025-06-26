'''
This is a caesar cipher
It shifts the characters by n positions
eg: for n=4, A->E, B->F
'''

message='This is a message'

def encrypt_caesar_cipher(message,n):     
    translated=''
    for i in range(len(message)):
        char=message[i]
        if char.isupper():
            translated+=chr((ord(char)+n-65)%26+65)
        elif char.islower():
            translated+=chr((ord(char)+n-97)%26+97)
        else:
            translated+=char
    return translated

print(encrypt_caesar_cipher(message,4))

def decrypt_caesar_cipher(translated,n):
    msg=''
    for i in range(len(translated)):
        char=translated[i]
        if char.isupper():
            msg+=chr((ord(char)-n-65)%26+65)
        elif char.islower():
            msg+=chr((ord(char)-n-97)%26+97)
        else:
            msg+=char
    return msg

print(decrypt_caesar_cipher(encrypt_caesar_cipher(message,4),4))