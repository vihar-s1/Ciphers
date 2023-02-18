#!/usr/bin/env python
'''
Encryption and Decryption functions for Shift Cipher, also known as, Caeser Cipher, given the key is known.
'''

from os import system

# A-Z mapped to 0-25 over ring Z26
__char_index = {chr(i+97): i for i in range(26)}
__char_index[' '] = ' '


def decrypt(cipher: str, key: int) -> str:
    """Performs shift cipher decryption using given key. 
    Any non-alphabet character including whitespaces is removed from the text before processing.

    Args:
        cipher (str): text to be decrypted
        key (int): key to be used to decryt the text

    Returns:
        str: decryted plain text
    """
    cipher = list(cipher.replace(r'[^a-zA-Z]+', "").lower())
    text = ""
    for char in cipher:
        index = __char_index[char]
        text = text + chr(97 + (index - key) % 26)
    return text


def encrypt(text: str, key: int) -> str:
    """Performs shift cipher encryption using given key. 
    Any non-alphabet character including whitespaces is removed from the text before processing.

    Args:
        text (str): text to be encrypted
        key (int): key to be used to encryt the text

    Returns:
        str: encrypted cipher text
    """
    text = list(text.replace(r'[^a-zA-Z]+', "").lower())
    cipher = ""
    for char in text:
        index = __char_index[char]
        cipher = cipher + chr(97 + (index + key) % 26)
    return cipher


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
            print(f'\n{key}', ":", decrypt(cipher, key), '\n')
            __isCorrectKey__(
                input("Enter for next key or any other key to exit..."))
    else:
        print("Invalid Choice")


if __name__ == "__main__":
    __main__()
