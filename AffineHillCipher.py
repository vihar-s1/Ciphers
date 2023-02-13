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
    """makes an attempt to find the key used to encrypt plainText to cipherText

    Args:
        plainText (str): original message text which is encryted
        cipherText (str): cipher text corresponding to the plainText

    Returns:
        tuple[list[list[int]], list[int]]: key in a form of tuple (L, b) where y = xL + b. returns None if key is not found.
    """
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
            
            if MatrixInverse.inverse(L) is not None: # L is invertible over Z26 so it is valid key matrix
                return L.tolist(), b.tolist()
            
    # key not found so we return none
    # this can be because the text was not long enough or the plainText - cipherText pair provided was invalid
    return None
            
            
def encrypt(plainText: str, L: list[list], b:list[int]) -> str:
    """performs affine-hill cipher encryption process on given cipher text

    Args:
        plainText (str): plain text to be encrypted
        L (list[list]): matrix key L to multiplied with plain text matrix
        b (list[int]): vector key to shift the x*L product

    Returns:
        str: cipher text is returned in case successful encryption else returns None
    """
    keyDim = len(b)
    # replacing any non-alphabetic characters with empty string
    plainText = plainText.replace(r'[^a-zA-Z]+','')
    
    # basic checks to ensure valid key-dimensions
    if len(L) != keyDim:
        return
    for row in L:
        if len(row) != keyDim:
            return
    # key is not invertible over Z26 and hence cannot be used for encoding-decoding
    if MatrixInverse.inverse(L) is None:
        return
    
    #padding plaintext with letter z to ensure that it can be converted to a matrix    
    while len(plainText) % keyDim != 0:
        plainText += "z"
        
    plain_mat = []
    # converting plain text to plainText matrix in corresponding Z26 values
    for i in range(len(plainText)//keyDim):
        temp = plainText[ i*keyDim : i*keyDim + keyDim ]
        plain_mat.append( list( map(lambda x: __char_index[x], temp) ) )
    
    cipher_mat = ( np.array(plain_mat) @ np.array(L) + np.array(b) ) % 26
    
    if cipher_mat is None: # never possible condition
        return None
    
    cipher_mat = [ "".join(list(map(lambda x: __index_char[x], row))) for row in cipher_mat ]
    return "".join(cipher_mat)
      

def __main__():
    key = findKey("adisplayedequation", "dsrmsioplxljbzullm")
    
    if key is None:
        print("No key found")
        return
    
    L, m = key
    print(f"L: {L}")
    print(f"m: {m}")
    print()
    print("encrypted:", encrypt("adisplayedequation", L, m).upper())
    print("expected:  DSRMSIOPLXLJBZULLM")
    
    
if __name__ == "__main__":
    __main__()