#!/usr/bin/env python

'''
- Performs Encryption Decryption Operation for the AffineCipher
- Encryption of Affine Cipher: C = a * P + b (mod 26)
- Decryption of Affine Cipher: P = a^-1 * (C - b) (mod 26)
- Here, P and C are plain text and cipher text resp.
- a, b belong to Z26 ring. Also a must be an invertible element for cipher to work.
'''

from os import system
import re

__char_index = {chr(i+97): i for i in range(26)}
__index_char = {i: chr(i+97) for i in range(26)}
__inverse = {1: 1, 3: 9, 5: 21, 7: 15, 9: 3, 11: 19, 13: 13, 15: 7, 17: 23,
             19: 11, 21: 5, 23: 17, 25: 25}


def encrypt(text: str, key_a: int, key_b: int) -> str:
    """Performs encryption on the text using key (a, b)

    Args:
        text (str): the plain text string to be encrypted
        key_a (int): multiplicative part of the key
        key_b (int): additive part of the key

    Returns:
        str: returns cipher text on successfull encryption else returns None
    """
    # inverse of key_a is not found so we return None
    if __inverse.get(key_a, None) is None:
        return None

    text = list( str(re.sub(r'[^a-zA-Z]+', "", text)).lower() )
    cipher = []

    for char in text:
        cipher.append(__index_char[(key_a * __char_index[char] + key_b) % 26])

    return ''.join(cipher)


def decrypt(cipher: str, key_a: int, key_b: int) -> str:
    """Performs affine cipher decryption on cipher text using key (a, b)

    Args:
        cipher (str): cipher text to be decrypted
        key_a (int): multiplicative part of the key
        key_b (int): additive part of the key

    Returns:
        str: returns the plain text on successful decryption else returns None
    """
    if __inverse.get(key_a, None) is None:
        print("AffineCipher: decrypt(): gcd(a, 26) = 1 condition not satisfied for the given key tuple")
        return None

    text = []
    cipher = list( str(re.sub(r'[^a-zA-Z]+', "", cipher)).lower() )


    # we perform + 26 while subtracting key_b to ensure that modulo operation is performed 
    # on a positive value only as adding 26 is same as adding 0 in modulo-26 addition
    for char in cipher:
        text += __index_char[(__inverse[key_a] *
                              (__char_index[char] - key_b + 26)) % 26]

    return ''.join(text)


def __isCorrectKey__(isSolution: bool):
    if isSolution:
        exit(0)


def __main__():
    system('cls')

    cipher = input("Enter Cipher Text: ").lower()

    choice = input("1: Enter Key\n2: Exhaustive Key Search\nYour Choice: ")

    if choice == '1':
        key = int(input("Enter Key: "))
        print("Plain Text:", decrypt(cipher, key))
    elif choice == '2':
        for key in range(26):
            system('clear')
            print(key, ":", decrypt(cipher, key), '\n')
            __isCorrectKey__(
                input("Enter for next key or any other key to exit..."))
    else:
        print("Invalid Choice")


if __name__ == "__main__":
    # __main__()
    text = input()
    cipher = encrypt(text, 5, 10)
    print(cipher)
    print(decrypt(cipher, 5, 10))
