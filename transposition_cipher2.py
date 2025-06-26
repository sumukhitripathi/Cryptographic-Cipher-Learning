'''
This is Double Columnar Transposition Cipher
It uses the Single Columnar Transposition technique two times
It can use the same or different keys
The output obtained from the first encryption will be the input to the second encryption.
'''

import math
message='geeksforgeeks'
key1='nick'
key2='boat'

def get_order(key):   #get order of key even in repeated characters
    return [i for _, i in sorted((char, i) for i, char in enumerate(key))]

def encrypt_tranposition_cipher(message, key):
    col = len(key)
    row = int(math.ceil(len(message) / col))
    fill_null = row * col - len(message)
    message += '_' * fill_null

    #create matrix
    matrix = [list(message[i:i+col]) for i in range(0, len(message), col)]
    key_order = get_order(key)

    # Read column-wise
    translated = ''
    for idx in key_order:
        for r in matrix:
            translated += r[idx]
    return translated

def encrypt_double_columnar_transposition_cipher(message,key1,key2):
    intermediate=encrypt_tranposition_cipher(message,key1)
    final=encrypt_tranposition_cipher(intermediate,key2)
    return final

print(encrypt_double_columnar_transposition_cipher(message,key1,key2))