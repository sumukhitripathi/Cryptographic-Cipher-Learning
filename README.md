# Cryptographic Cipher Learning

This repository contains beginner-friendly implementations of classical cryptographic ciphers and hashing examples in Python and C++.

## Objective

- Understand how classical encryption and decryption algorithms work
- Practice substitution and transposition cipher logic
- Build a foundation for modern cryptography concepts

## Cipher List

| Cipher | File | One-line definition |
|---|---|---|
| Affine Cipher | `affine_cipher.py` | A monoalphabetic substitution cipher that maps each letter using the function `(a*x + b) mod 26`. |
| Atbash Cipher | `atbash_cipher.py` | A fixed substitution cipher that reverses the alphabet (`A <-> Z`, `B <-> Y`, etc.). |
| Caesar Cipher | `caesar_cipher.py` | A substitution cipher that shifts each letter by a fixed number of positions. |
| Hill Cipher | `hill_cipher.py` | A polygraphic substitution cipher that encrypts letter blocks using matrix multiplication modulo 26. |
| Multiplicative Cipher | `multiplicative_cipher.cpp` | A substitution cipher that multiplies each letter index by a key modulo 26. |
| Playfair Cipher | `playfair_cipher.cpp` | A digraph substitution cipher that encrypts pairs of letters using a 5x5 key square. |
| Reverse Cipher | `reverse_cipher.py` | A transposition-style method that encrypts by reversing the entire text. |
| Columnar Transposition (Single) | `transposition_cipher1.py` | A transposition cipher that writes text in rows and reads it column-wise based on key order. |
| Columnar Transposition (Double) | `transposition_cipher2.py` | A stronger variant that applies columnar transposition two times (possibly with different keys). |
| Rail Fence Cipher | `transposition_cipher3.py` | A transposition cipher that places characters in a zig-zag rail pattern and reads row-wise. |
| SHA-1 Hash | `sha1_hash.py` | A cryptographic hash function that generates a 160-bit digest for input data integrity checks. |
| Vigenere Cipher | `vigen�re_cipher.py` | A polyalphabetic substitution cipher that uses a repeating keyword to determine shifts. |


## How to Run

### Run Python ciphers

```bash
python affine_cipher.py
```

### Compile and run C++ ciphers

```bash
g++ multiplicative_cipher.cpp -o multiplicative_cipher
./multiplicative_cipher

```

## Notes

- These scripts are educational and focused on clarity over production security.
- Classical ciphers are not secure for modern real-world cryptographic use.
- SHA-1 is deprecated for collision resistance and should not be used in new security-critical systems.