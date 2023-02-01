#!/usr/bin/env python
import numpy as np
import MatrixInverse, math

'''
Performs Hill Cipher encryption, decryption operation given the key is known.
Can also determine the key if plain text and corresponding cipher text is known.
'''

__char_index = {chr(i+97):i for i in range(26)}
__char_index[' '] = ' '
__index_char = {v:k for (k,v) in __char_index.items()}


def findKey(plainText, cipherText) -> list[list] | None:
    '''
    Attempts to find the key for the given plainText-CipherText pair.
    If key is found, it returns the key, otherwise returns None.
    '''
    
    # key needs to be a sqr matrix of size m such that sqr(m) <= text length so that matrix inversion operations are possible
    maxKeyDim = math.floor(math.sqrt(len(plainText)))
    
    if len(plainText) != len(cipherText):
        print("findKey: [Error]: plain text length is not equal to cipher text")
        return None
    
    for keyDim in range(2, maxKeyDim + 1): # key dimension can be starting from 2 to maxKeyDim
        
        plain_mat, cipher_mat = [], []
        
        # forming a matrix of size keyDim from plain text and cipher text to try to decode the key
        # the matrix has to be of size same as key dimension. also maxKeyDim^2 <= len(plainText)
        # thus it is ensured that the loop does not access invalid memory location while accessing the list
        for i in range(keyDim):
            plain_mat.append( plainText[i*keyDim : i*keyDim+keyDim] )
            cipher_mat.append( cipherText[i*keyDim : i*keyDim+keyDim] )
        
        
        # Converting the characters to their corresponding index values in ring Z26
        for i in range(len(plain_mat)):
            plain_mat[i] = list( map(lambda x: __char_index[x], plain_mat[i]) )
            cipher_mat[i] = list( map(lambda x: __char_index[x], cipher_mat[i]) )
        
        # calculating plainText matrix inverse over ring Z26
        plain_mat_inv = MatrixInverse.inverse(plain_mat)
        
        # plain matrix inverse was calculated successfully, so we can get the key
        if plain_mat_inv:
            key = np.array(plain_mat_inv) @ np.array(cipher_mat) % 26
            return np.round_(key).astype(int).tolist()
        
    
    # key not found so we return none
    # this can be because the text was not long enough or the plainText - cipherText pair provided was invalid
    return None


def encrypt(plainText: str, key: list[list], padding='z') -> str | None:
    '''
    - Performs Encryption operation on Cipher text using key matrix 'key'.
    - returns cipher text if successfuly encrypted else returns none.
    - If the plain text length is not sufficient to form a matrix for multiplication with the key, 
    the plain text is padded at the end with the letter z.
    '''
    if (len(plainText) < 1):
        return None
    plain_mat = []
    keyDim = len(key)
    
    # if plaintext length is not a multiple of key dimension, then
    # we cannot form a proper plain text matrix with row length == key dimension
    # So we provide padding to the plain text matrix to fullfil the size mismatch
    if len(plainText) % len(key) != 0:
        missingLength = math.ceil(plainText / len(key)) * len(key) - len(plainText)
        plainText += padding * missingLength
        # padded with Zs
        
        
    # need to convert the plain Text to a matrix in-order to perform matrix multiplication with the key
    for i in range(len(plainText) // keyDim):
        plain_mat.append( plainText[i*keyDim : i*keyDim+keyDim] )
        
    for i in range(len(plain_mat)):
        plain_mat[i] = list( map(lambda x: __char_index[x], plain_mat[i]) )

    cipher_mat = np.array(plain_mat) @ np.array(key) % 26
    cipher = ""
    
    # converting the cipher text matrix to string.
    for row in cipher_mat:
        for val in row:
            cipher += __index_char[val]
    
    return cipher


def decrypt(cipherText: str, key: list[list]) -> str | None:
    '''
    - Performs Decryption operation on Cipher text using key matrix 'key'.
    - returns plain text if successfully decoded else returns none
    - The cipher wil have to be a multiple of the key dimension for proper decryption
    else it cannot be decrypted properly.
    '''
    cipher_mat = []
    keyDim = len(key)
    
    if (len(cipherText) % keyDim != 0):
        return None
    
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
    key = findKey(plainText, cipherText)
    print("\nKey:", key)
    
    
if __name__ == "__main__":
    __main__()