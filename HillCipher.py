#!/usr/bin/env python
import numpy as np
import MatrixInverse

__char_index = {chr(i+97):i for i in range(26)}
__char_index[' '] = ' '
__index_char = {v:k for (k,v) in __char_index.items()}


def findKey(plainText, cipherText, keyDim):
    if len(plainText) != len(cipherText):
        print("findKey: [Error]: plain text length is not equal to cipher text")
        return None
    if len(plainText) % keyDim != 0:
        print("findKey: [Error]: plain text length not multiple of key dimension")
        print(f"plainText length: {len(plainText)}, key-dimension: {keyDim}")
        return None
    
    plain_mat, cipher_mat = [], []
    for i in range(len(plainText) // keyDim):
        plain_mat.append( plainText[i*keyDim : i*keyDim+keyDim] )
        cipher_mat.append( cipherText[i*keyDim : i*keyDim+keyDim] )
    
    for i in range(len(plain_mat)):
        plain_mat[i] = list( map(lambda x: __char_index[x], plain_mat[i]) )
        cipher_mat[i] = list( map(lambda x: __char_index[x], cipher_mat[i]) )
    
    if len(plain_mat) > keyDim:
        plain_mat = plain_mat[:keyDim]
        cipher_mat = cipher_mat[:keyDim]
    elif len(plain_mat) < keyDim:
        print("findKey: [Error]: textSize needs to be atleast dimSize^2 to get key.")
        return None
    
    plain_mat_inv = MatrixInverse.inverse(plain_mat)
    
    if plain_mat_inv is None:
        return None
    
    key = np.array(plain_mat_inv) @ np.array(cipher_mat) % 26
    
    return np.round_(key).astype(int).tolist()


def encrypt(plainText: str, key: list[list]):
    plain_mat = []
    keyDim = len(key)
    
    for i in range(len(plainText) // keyDim):
        plain_mat.append( plainText[i*keyDim : i*keyDim+keyDim] )
        
    for i in range(len(plain_mat)):
        plain_mat[i] = list( map(lambda x: __char_index[x], plain_mat[i]) )

    cipher_mat = np.array(plain_mat) @ np.array(key) % 26
    cipher = ""
    for row in cipher_mat:
        for val in row:
            cipher += __index_char[val]
    
    return cipher


def decrypt(cipherText: str, key: list[list]):
    cipher_mat = []
    keyDim = len(key)
    
    for i in range(len(cipherText) // keyDim):
        cipher_mat.append( cipherText[i*keyDim : i*keyDim+keyDim] )
        
    for i in range(len(cipher_mat)):
        cipher_mat[i] = list( map(lambda x: __char_index[x], cipher_mat[i]) )

    key_inv = MatrixInverse.inverse(key)
    if key_inv is None:
        return None
    
    plain_mat = np.array(cipher_mat) @ np.array(key_inv) % 26
    plain = ""
    for row in plain_mat:
        for val in row:
            plain += __index_char[val]
    
    return plain
        

def __main__():
    plainText = "breathtaking"
    cipherText = "rupotentoifv"
    key = findKey(plainText, cipherText, 3)
    print("\nKey:", key)
    
    
if __name__ == "__main__":
    __main__()