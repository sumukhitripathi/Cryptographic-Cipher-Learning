'''
Hill cipher is a polygraphic substitution cipher based on linear algebra.
Each letter is represented by a number modulo 26.
The encryption of a message is done by multiplying the message vector with a key matrix.
The decryption is done by multiplying the encrypted message vector with the inverse of the key matrix.
The key matrix must be invertible modulo 26 for the cipher to work.
'''

import math
MOD = 26

def prepare_message(message, n):
    message = message.lower().replace(" ", "")
    while len(message) % n != 0:
        message += 'x'
    return message

def key_to_matrix(key):
    key = key.lower()
    n = int(len(key) ** 0.5)
    if n * n != len(key):
        raise ValueError("Key length must be a perfect square!")
    matrix = []
    index = 0
    for i in range(n):
        row = []
        for j in range(n):
            row.append(ord(key[index]) - ord('a'))
            index += 1
        matrix.append(row)
    return matrix

def matrix_multiply(A, B):
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
            result[i][j] %= MOD
    return result

def matrix_vector_multiply(matrix, vector):
    n = len(matrix)
    result = []

    for i in range(n):
        total = 0
        for j in range(n):
            total += matrix[i][j] * vector[j]
        result.append(total % MOD)

    return result

def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return (matrix[0][0]*matrix[1][1] -
                matrix[0][1]*matrix[1][0])
    det = 0
    for c in range(n):
        minor = [row[:c] + row[c+1:] for row in matrix[1:]]
        det += ((-1)**c) * matrix[0][c] * determinant(minor)
    return det

def matrix_inverse(matrix):
    n = len(matrix)
    det = determinant(matrix) % MOD
    if math.gcd(det, MOD) != 1:
        raise ValueError("Key matrix is not invertible modulo 26")
    det_inv = pow(det, -1, MOD)
    cofactors = []
    for r in range(n):
        cofactor_row = []
        for c in range(n):
            minor = [row[:c] + row[c+1:] for i,row in enumerate(matrix) if i != r]
            cofactor = ((-1)**(r+c)) * determinant(minor)
            cofactor_row.append(cofactor % MOD)
        cofactors.append(cofactor_row)
    adjugate = list(map(list, zip(*cofactors)))
    inverse = []
    for row in adjugate:
        inverse.append([(element * det_inv) % MOD for element in row])
    return inverse

#Message encryption
def encrypt_hill_cipher(message, key):
    key_matrix = key_to_matrix(key)
    n = len(key_matrix)
    message = prepare_message(message, n)
    encrypted = ""
    for i in range(0, len(message), n):
        block = message[i:i+n]
        vector = [ord(char) - ord('a') for char in block]
        result = matrix_vector_multiply(key_matrix, vector)
        encrypted += ''.join(chr(num + ord('a')) for num in result)
    return encrypted

#Message decryption
def decrypt_hill_cipher(ciphertext, key):
    key_matrix = key_to_matrix(key)
    inverse_matrix = matrix_inverse(key_matrix)
    n = len(inverse_matrix)
    decrypted = ""
    for i in range(0, len(ciphertext), n):
        block = ciphertext[i:i+n]
        vector = [ord(char) - ord('a') for char in block]
        result = matrix_vector_multiply(inverse_matrix, vector)
        decrypted += ''.join(chr(num + ord('a')) for num in result)
    return decrypted

# Example Usage
message = "This is a message"
key = "gybnqkurp" 
encrypted = encrypt_hill_cipher(message, key)
print("Encrypted:", encrypted)
decrypted = decrypt_hill_cipher(encrypted, key)
print("Decrypted:", decrypted)