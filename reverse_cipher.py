#The encryption is done by reversing the text

message='This is message'

def encrypt_reverse_cipher(message):
    translated=''
    for i in range(len(message)):
        translated+=message[len(message)-i-1]
    return translated

print(encrypt_reverse_cipher(message))

def decrypt_reverse_cipher(translated):
    msg=''
    for i in range(len(translated)):
        msg+=translated[len(translated)-i-1]
    return msg

print(decrypt_reverse_cipher(encrypt_reverse_cipher(message)))