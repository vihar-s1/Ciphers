#!/usr/bin/env python
'''
Encryption and Decryption functions for AutoKey-Cipher given the key is known.
'''

from os import system
import re

__char_index = {chr(i+97):i for i in range(26)}
__index_char = {i:chr(i+97) for i in range(26)}
        
        
def encrypt(text: str, key: int) -> str:
    """Performs encryption on the text "text" using seed key "key". The function replaces any character outside of a-z A-Z with a blank string ("")

    Args:
        text (str): plain text to be encryted
        key (int): key used to perform encrytion

    Returns:
        str: returns cipher text on successful encryption else returns None
    """
    text = list( re.sub(r'[^a-zA-Z]+', "", text).lower() )
    cipher = []
    
    # encoding first character with the key
    cipher += __index_char[(__char_index[text[0]] + key) % 26]
    
    for i in range(1, len(text)):
        # encoding ith character with (i-1)th character
        cipher += __index_char[(__char_index[text[i]] + __char_index[text[i-1]]) % 26]
        
    return ''.join(cipher)


def decrypt(cipher: str, key: int) -> str:
    """Performs decryption on the text "cipher" using seed key "key". The function replaces any character outside of a-z A-Z with a blank string ("")

    Args:
        text (str): cipher text to be decryted
        key (int): key used to perform decrytion

    Returns:
        str: returns plain text on successful decryption else returns None
    """
    text = []
    cipher = list( re.sub(r'[^a-zA-Z]+', "", cipher).lower() )

    
    # decoding first character with the key
    text += __index_char[(__char_index[cipher[0]] - key) % 26]
    
    for i in range(1, len(cipher)):
        # decoding ith character with (i-1)th character
        text += __index_char[(__char_index[cipher[i]] - __char_index[text[-1]]) % 26]
        
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
            print(key, ":", decrypt(cipher, key),'\n')
            __isCorrectKey__(input("Enter for next key or any other key to exit..."))
    else:
        print("Invalid Choice")
        
        
if __name__ == "__main__":
    __main__()