'''
This is Rail Fence transposition cipher (zig-zag cipher)
The plain-text is written downwards and diagonally on successive rails of an imaginary fence.
When we reach the bottom rail, we traverse upwards moving diagonally, after reaching the top rail, 
the direction is changed again. Thus the alphabets of the message are written in a zig-zag manner.
After each alphabet has been written, the individual rows are combined to obtain the cipher-text.
'''

message = 'This is a message'
key = 'hack'  
num_rails = len(key)

def encrypt_RailFence_cipher(message, num_rails):
    rail = [['\n' for _ in range(len(message))] for _ in range(num_rails)]

    dir_down = False
    row, col = 0, 0

    for char in message:
        if row == 0 or row == num_rails - 1:
            dir_down = not dir_down
        rail[row][col] = char
        col += 1
        row = row + 1 if dir_down else row - 1

    result = []
    for r in rail:
        for char in r:
            if char != '\n':
                result.append(char)
    return ''.join(result)

def decrypt_RailFence_cipher(cipher, num_rails):
    rail = [['\n' for _ in range(len(cipher))] for _ in range(num_rails)]

    dir_down = None
    row, col = 0, 0

    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == num_rails - 1:
            dir_down = False
        rail[row][col] = '*'
        col += 1
        row = row + 1 if dir_down else row - 1

    index = 0
    for i in range(num_rails):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == num_rails - 1:
            dir_down = False
        result.append(rail[row][col])
        col += 1
        row = row + 1 if dir_down else row - 1

    return ''.join(result)

encrypted = encrypt_RailFence_cipher(message, num_rails)
print("Encrypted:", encrypted)

decrypted = decrypt_RailFence_cipher(encrypted, num_rails)
print("Decrypted:", decrypted)
