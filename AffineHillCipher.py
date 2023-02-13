#!/usr/bin/env python
import numpy as np
import MatrixInverse, math

'''
Performs Encryption operation for affine-hill cipher.
Can also determine the key if a valid plain text - cipher text pair is given.
'''


__char_index = {chr(i+97):i for i in range(26)}
__index_char = {v:k for (k,v) in __char_index.items()}


def findKey(plainText: str, cipherText: str) -> tuple[list[list], list]:
    '''
    Attempts to find the key for the given plainText-CipherText pair.
    If key is found, it returns the key (L, b) as a tuple, otherwise returns None.
    The key returned will be of the smallest possible dimension in case multiple keys are found.
    '''
    plainText, cipherText = plainText.lower(), cipherText.lower()
    
    # key component L needs to be a sqr matrix of size m such that sqr(m) <= text length so that matrix inversion operations are possible
    maxKeyDim = math.floor(math.sqrt(len(plainText)))
    
    if len(plainText) != len(cipherText):
        print("findKey: [Error]: plain text length is not equal to cipher text")
        return None
    
    
    # keyDim is limited to maxKeyDim - 1 so as to be able to form 2 plain-matrices such that x1 - x2 != 0-matrix
    for keyDim in range(2, maxKeyDim):
        # two plain matrix, cipher matrix needed to implement L = (x1 - x2)^-1 * (y1 - y2)
        plain_mat_1, cipher_mat_1 = [], []
        plain_mat_2, cipher_mat_2 = [], []
    
        # forming a matrix of size keyDim from plain text and cipher text to try to decode the key
        # the matrix has to be of size same as key dimension. also maxKeyDim^2 <= len(plainText)
        # thus it is ensured that the loop does not access invalid memory location while accessing the list
        for i in range(keyDim):
            plain_mat_1.append( plainText[i*keyDim : i*keyDim + keyDim] )
            plain_mat_2.append( plainText[i*keyDim + keyDim: i*keyDim + 2*keyDim] )     # offseted by a single row
            cipher_mat_1.append( cipherText[i*keyDim : i*keyDim + keyDim] )
            cipher_mat_2.append( cipherText[i*keyDim + keyDim: i*keyDim + 2*keyDim] )   # offseted by a single row
        
        # Converting the characters to their corresponding index values in ring Z26
        for i in range(len(plain_mat_1)):
            plain_mat_1[i] = list( map(lambda x: __char_index[x], plain_mat_1[i]) )
            plain_mat_2[i] = list( map(lambda x: __char_index[x], plain_mat_2[i]) )
            cipher_mat_1[i] = list( map(lambda x: __char_index[x], cipher_mat_1[i]) )
            cipher_mat_2[i] = list( map(lambda x: __char_index[x], cipher_mat_2[i]) )
            
        plain_mat_inv = MatrixInverse.inverse( (np.array(plain_mat_1) - np.array(plain_mat_2)).tolist() )
        cipher_mat = (np.array(cipher_mat_1) - np.array(cipher_mat_2)).tolist()
        
        # plain matrix inverse successfully calculated so we can move ahead
        if plain_mat_inv:
            L = ( np.array(plain_mat_inv) @ np.array(cipher_mat) ) % 26
            
            # now using Lx + b = y (mod 26)
            b = ( np.array(cipher_mat_1[0]) - np.array(plain_mat_1[0]) @ L ) % 26
            if L is not None and b is not None:
                return L.tolist(), b.tolist()
            
    # key not found so we return none
    # this can be because the text was not long enough or the plainText - cipherText pair provided was invalid
    return None
            
            
def encrypt(plainText: str, L: list[list], b:list) -> str:
    pass            
      

def __main__():
    L, m = findKey("adisplayedequation", "dsrmsioplxljbzullm")
    print(f"L: {L}")
    print(f"m: {m}")

if __name__ == "__main__":
    __main__()