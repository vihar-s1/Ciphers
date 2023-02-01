#!/usr/bin/env python
from os import system

'''
Encryption and Decryption functions for AutoKey-Cipher given the key is known.
'''

__char_index = {chr(i+97):i for i in range(26)}
__index_char = {i:chr(i+97) for i in range(26)}
        
        
def encrypt(text: str, key: int) -> str:
    '''
    - Performs Encryption operation on Cipher text using key 'key'.
    - returns cipher text
    '''
    text = list(text)
    cipher = []
    
    # encoding first character with the key
    cipher += __index_char[(__char_index[text[0]] + key) % 26]
    
    for i in range(1, len(text)):
        # encoding ith character with (i-1)th character
        cipher += __index_char[(__char_index[text[i]] + __char_index[text[i-1]]) % 26]
        
    return ''.join(cipher)


def decrypt(cipher: str, key: int):
    '''
    - Performs Decryption operation on Cipher text using key 'key'.
    - returns plain text
    '''
    text = []
    cipher = list(cipher)
    
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