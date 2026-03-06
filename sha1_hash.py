'''
SHA-1 or Secure Hash Algorithm 1 is a cryptographic algorithm that takes an input and produces a 160-bit (20-byte) hash value.
The SHA-1 algorithm is designed to be a one-way function, meaning that it is computationally infeasible to reverse the process 
and retrieve the original input from the hash value. It is commonly used for data integrity verification, digital signatures, 
and password hashing.
'''

import hashlib

def sha1_hash(input_string):
    # Create a new sha1 hash object
    sha1 = hashlib.sha1()
    # Update the hash object with the bytes of the input string
    sha1.update(input_string.encode('utf-8'))
    # Get the hexadecimal representation of the hash
    return sha1.hexdigest()

# Example usage
if __name__ == "__main__":
    input_string = "This is a message"
    hash_value = sha1_hash(input_string)
    print(f"Input: {input_string}")
    print(f"SHA-1 Hash: {hash_value}")