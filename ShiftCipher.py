#!/usr/bin/env python
from os import system


__char_index = {chr(i+97):i for i in range(26)}
__char_index[' '] = ' '

def decrypt(cipher, key):
    cipher = list(cipher)
    text = ""
    for char in cipher:
        ascii = __char_index[char]
        text = text + chr(97 + (ascii-key)%26)
    return text
        
def encrypt(text, key):
    text = list(text)
    cipher = []
    for char in text:
        ascii = __char_index[char]
        cipher = cipher + chr(97 + (ascii+key)%26)
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
            print(f'\n{key}', ":", decrypt(cipher, key),'\n')
            __isCorrectKey__(input("Enter for next key or any other key to exit..."))
    else:
        print("Invalid Choice")

if __name__ == "__main__":
    __main__()