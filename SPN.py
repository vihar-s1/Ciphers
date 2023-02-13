#!/usr/bin/env python

'''
Substituition - Permutation Network (SPN) Cipher.
Contains function to perform SPN encryption.
'''

__char_index = {chr(i+97): i for i in range(26)}


def __xor(s1: str, s2: str) -> str:
    s = ""
    for (i, j) in zip(s1, s2):
        s += str((int(i) + int(j)) % 2)
    
    return s


def encrypt(x: str, Ps: dict, Pp: list[int], k: list[str]):
    '''
    - Performs Substitution Permutation Network Encryption on Bit-Stream of Length is multiple of L * M .

    - x: The nessage bit-stream to be encoded. if length is not a multiple of L * M, message is padded with z at the end.
    - Ps: The Substitution Box - maps vector of length L to vector of length L
    - Pp: The Permutation Box - returns permutation of the  L*M long bitstream
    - K: List of N+1 round keys
    
    - returns cipher text on successful encryption else returns None.
    
    - returns cipher text on successful encryption else returns None.
    '''
    L = len( list(Ps.keys())[0] )
    M = len(Pp) // L
    
    # performing input sanity checks
    for (key, val) in Ps.items():
        if len(key) != L or len(val) != L:
            raise Exception("SPN: encrypt: [Error] Substitution-Box must map L-bit sequenc to another L-bit sequence")
    
    if len(Ps) != 2**L:
        raise Exception("SPN: encrypt: [Error] Substitution-Box must contain mapping for all 2^L combinations")
    
    unitLength = M*L
    if len(x) % unitLength != 0:
        missing = (len(x) // unitLength) * unitLength - len(x)
        x = x + 'z'*missing # padding with 'z' to adjust for missing length
    
    # performing input sanity checks
    for (key, val) in Ps.items():
        if len(key) != L or len(val) != L:
            raise Exception("SPN: encrypt: [Error] Substitution-Box must map L-bit sequenc to another L-bit sequence")
    
    if len(Ps) != 2**L:
        raise Exception("SPN: encrypt: [Error] Substitution-Box must contain mapping for all 2^L combinations")
    
    unitLength = M*L
    if len(x) % unitLength != 0:
        missing = (len(x) // unitLength) * unitLength - len(x)
        x = '0'*missing + x # padding with '0' to adjust for missing length
    
    # Round keys K^1, K^2, ..., K^(N+1) equivalently K[0], K[1], ..., k[N]
    N = len(k) - 1
    
    w_vec = []  # breaking message x in chunks of length L * M
    for i in range(len(x)//unitLength):
        w_vec.append( x[i*unitLength : i*unitLength + unitLength] )
        
    y_vec = []
    
    # performing SPN operation for each chunk of length L * M
    for w in w_vec:
        for r in range(N):  # performing N Substitution Permutation Rounds
            u = __xor(w, k[r])  # u^r = w^r-1 XOR k^r
            v = ""

            for i in range(M):
                v += Ps[ u[i*L: i*L + L] ]  # performing M substitution operations
            
            w = ""  # calculating w^r = Pp(v^r)
            for i in range(L*M):
                w += v[Pp[i]]

        y_vec.append( __xor(v, k[N]) )  # cipher text y = v^N XOR K^(N+1) = v^N XOR K[N]
        
    return ''.join(y_vec)


def __main__():
    # L = M = N = 4
    Ps = {
        '0000': '1110', '0001': '0100', '0010': '1101', '0011': '0001',
        '0100': '0010', '0101': '1111', '0110': '1011', '0111': '1000',
        '1000': '0011', '1001': '1010', '1010': '0110', '1011': '1100',
        '1100': '0101', '1101': '1001', '1110': '0000', '1111': '0111'
    }  # replace the key with its value --> Substitution box
    
    # permutation box
    Pp = [0, 4, 8, 12, 1, 5, 9, 13, 2 ,6 ,10, 14, 3, 7, 11, 15] # value at position i goes to position Pp[i] 
    
    # 32 bit seed key -> 3A94D63F
    k = '00111010100101001101011000111111'
    # 16-bit round keys generated by taking 16 bits from seed key shifted by 4 bits
    kr = [k[0:16], k[4:20], k[8:24], k[12:28], k[16:32]] 
    
    # plain text --> 26B7
    x = '0010011010110111'
    # expected cipher text --> BCD6
    y_expected = '1011110011010110'
    # cipher text --> obtained by encrypting plain text
    
    y = encrypt(x, Ps, Pp, kr)
    
    print("x  :",x)
    print("y* :",y_expected)
    print("y  :",y)
    

if __name__ == "__main__":
    __main__()
