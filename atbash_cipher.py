'''
It is special case of Affine cipher with both the keys being 25 i.e. k1=k2=25
A->Z, B->Y,.....,Z->A
'''

message="This is a message"

map_table={'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V',
        'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q',
        'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L',
        'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G',
        'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 'Z' : 'A'}

def encrypt_decrypt_atbash(message):
    translated=''
    for c in message.upper():
        if (c!=' '):
            translated+=map_table[c]
        else:
            translated+=' '
    return translated


print("Encrypted message: ",encrypt_decrypt_atbash(message))
print("Decrypted message: ",encrypt_decrypt_atbash(encrypt_decrypt_atbash(message)))