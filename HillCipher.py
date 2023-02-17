#!/usr/bin/env python

'''
Performs Hill Cipher encryption, decryption operation given the key is known.
Can also determine the key if plain text and corresponding cipher text is known.
- The realtion between plain text matrix P, cipher text matrix C, and key k is C = P * k or P = C * inv(k)
'''
import numpy as np
import MatrixInverse, math

__char_index = {chr(i+97):i for i in range(26)}
__index_char = {v:k for (k,v) in __char_index.items()}


def findKey(plainText: str, cipherText: str) -> list[list[int]]:
    """Attempts to find the key for the given plain-Text and Cipher-Text pair.

    Args:
        plainText (str): The plain text string
        cipherText (str): The cipher text string

    Returns:
        list[list[int]]: returns the key if the plainText-cipherText pair is valid pair of appropriate length.
    """
    
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


def encrypt(plainText: str, key: list[list[int]], padding:str='z') -> str:
    """performs encryption on the text 'plainText' using the square key matrix 'key' of order n.

    Args:
        plainText (str): the text string to be encryted
        key (list[list[int]]): the encrytion key matrix
        padding (str, optional): the character used to pad the text string if length is not suitable for matrix-multiplication. Defaults to 'z'.

    Returns:
        str: returns encrypted string if successful else returns None/
    """
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

    # encryption process Cipher = Plain * Key
    cipher_mat = np.array(plain_mat) @ np.array(key) % 26
    cipher = ""
    
    # converting the cipher text matrix to string.
    for row in cipher_mat:
        for val in row:
            cipher += __index_char[val]
    
    return cipher


def decrypt(cipherText: str, key: list[list[int]]) -> str:
    """performs decryption process on the text 'cipherText' using the key matrix 'key' of order n.

    Args:
        cipherText (str): the text string to be decrypted
        key (list[list[int]]): the key matrix

    Returns:
        str: returns the decrypted text string.
    """
    cipher_mat = []
    keyDim = len(key)
    
    # if the the cipher text is not a multiple of key dimension, cipher text matrix cannot be build
    if (len(cipherText) % keyDim != 0):
        return None
    
    # building text into matrix
    for i in range(len(cipherText) // keyDim):
        cipher_mat.append( cipherText[i*keyDim : i*keyDim+keyDim] )
        
    for i in range(len(cipher_mat)):
        cipher_mat[i] = list( map(lambda x: __char_index[x], cipher_mat[i]) )

    # checking if key is invertible. If the key is not ivertible, encryption cannot be done
    key_inv = MatrixInverse.inverse(key)
    if key_inv is None:
        return None
    
    # Plain = Cipher * Key_Inv
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