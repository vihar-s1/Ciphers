#!/usr/bin/env python
from os import system


__char_index = {chr(i+97):i for i in range(26)}
__index_char = {i:chr(i+97) for i in range(26)}
__inverse = {1:1, 3:9, 5:21, 7:15, 9:3, 11:19, 13:13, 15:7, 17:23,
             19:11, 21:5, 23:17, 25:25}
        

def encrypt(text: str, key_a: int, key_b: int):
    text = list(text)        
    cipher = []
    
    for char in text:
        cipher.append( __index_char[ (key_a * __char_index[char] + key_b) % 26 ] )
        
    return ''.join(cipher)


def decrypt(cipher: str, key_a: int, key_b: int):
    try:
        if 26 % key_a == 0:
            raise Exception
    except:
        print("AffineCipher: decrypt(): gcd(a, 26) = 1 condition not satisfied for the given key tuple")
        return None
    
    text = []
    cipher = list(cipher)
    
    for char in cipher:
        text += __index_char[ (__inverse[key_a] * (__char_index[char] - key_b)) % 26 ]
        
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
    # text = input().replace(' ', '')
    # cipher = encrypt(text, 7, 5)
    # print(cipher)
    # print(decrypt(cipher, 7, 5))