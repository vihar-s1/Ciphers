#!/usr/bin/env python

'''
Substituition - Permutation Network (SPN) Cipher.
- The cipher performs series of enryption rounds.
- In each of the rounds, the input stream undergoes a substitution operation followed by a permutation operation.
- The process is reversed during decryption.

Contains function to perform SPN encryption
'''

# defining custom exception handling classes
class SubstitutionBoxMappingError(Exception):
    """Custom error raised when the substitution box does not contain L-bit to L-bit mapping

    Args:
        Exception (_type_): Extends class Exception
    """
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        
class SubstitutionBoxLengthError(Exception):
    """Custom error raisd when the substitution box is not of appropriate length, i.e., 2^L

    Args:
        Exception (_type_): Extends class Exception
    """
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        

def __xor(s1: str, s2: str) -> str:
    s = ""
    for (i, j) in zip(s1, s2):
        s += str((int(i) + int(j)) % 2)
    
    return s


def encrypt(x: str, Ps: dict, Pp: list[int], k: list[str]):
    """Performs SPN encryption on Bit-Stream of length which is multiple of L * M

    Args:
        x (str): The message bit-stream to be encoded. If length is not a multiple of L*M, message is padded with 0s at beginning.
        Ps (dict): The Substitution Box of size 2^L consisting of all permutation of all L-bit long strings
        Pp (list[int]): The Permutation Box of size L * M used to permute the bitstream
        k (list[str]): N+1 round keys list

    Raises:
        SubstitutionBoxLengthError: Raises exception when Substitution-Box dimensions are not satisfied
        SubstitutionBoxMappingErro: Raises exception when Substitution-Box does not contain L-bit to L-bit mapping

    Returns:
        _type_: returns encrypted bitstream on successful encryption.
    """
    L = len( list(Ps.keys())[0] )
    M = len(Pp) // L
    
    ########################################## performing input sanity checks ##########################################
    for (key, val) in Ps.items():
        if len(key) != L or len(val) != L:
            raise SubstitutionBoxMappingError("Substitution-Box must map L-bit sequence to another L-bit sequence")
    
    if len(Ps) != 2**L:
        raise SubstitutionBoxLengthError("Substitution-Box must contain mapping for all 2^L combinations")
    
    unitLength = M*L
    while len(x) % unitLength != 0:
        x = "0" + x
        
    ###################################### performing input sanity checks complete ######################################
    
    
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


def decrypt(y: str, Ps: dict[str, str], Pp: list[int], k: list[str]):
    """Performs SPN decryption on Bit-Stream of length which is multiple of L * M

    Args:
        y (str): The message bit-stream to be decoded. If length is not a multiple of L*M, decoding is not performed
        Ps (dict): The Substitution Box of size 2^L consisting of all permutation of all L-bit long strings.
        Pp (list[int]): The Permutation Box of size L * M used to permute the bitstream.
        k (list[str]): N+1 round keys list.
        
        Note that Ps, Pp, and k are supposed to be the same as those used during encryption and NOT the inverses.

    Raises:
        Exception: Raises exception when Substitution-Box dimensions are not satisfied
        Exception: Raises exception when Substitution-Box does not contain L-bit to L-bit mapping

    Returns:
        _type_: returns encrypted bitstream on successful encryption.
    """
    L = len( list(Ps.keys())[0] )
    M = len(Pp) // L
    
    ########################################## performing input sanity checks ##########################################
    for (key, val) in Ps.items():
        if len(key) != L or len(val) != L:
            raise SubstitutionBoxMappingError("Substitution-Box must map L-bit sequence to another L-bit sequence")
    
    if len(Ps) != 2**L:
        raise SubstitutionBoxLengthError("Substitution-Box must contain mapping for all 2^L combinations")
    
    # while len(y) % unitLength != 0:
    #     y = "0" + y
        
    ###################################### performing input sanity checks complete ######################################
    
    #################################### inverting Substitution and Permutation Boxes ###################################
    Ps_inv = {v:kk for (kk,v) in Ps.items()}
    Pp_inv = [0]*len(Pp)
    for i in range(len(Pp)):
        Pp_inv[Pp[i]] = i
    #################################### inverting Substitution and Permutation Boxes ###################################

    #TODO: decryption code here
    N = len(k) - 1
    unitLength = M*L
    
    y_vec = [ y[i*unitLength : i*unitLength + unitLength] for i in range(len(y)//unitLength) ]
    x_vec = []
    
    for y in y_vec:
        # Nth round roll-back
        # y = v^N XOR k[N]
        v = __xor(y, k[N])
              
        u = "" # declaring u global for the next 2 for-loops
        for i in range(M):
            u += Ps_inv[ v[i*L : i*L + L] ]
        
        # running 0 to N-1 rounds in reverse
        w = ""
        for r in range(N-1, -1, -1):
            # w(r-1) = ur XOR kr
            w = __xor(u, k[r])  # inverting key addition
            v = ""
            
            for i in range(L*M):
                v += w[Pp_inv[i]] # inverting permutation 
            
            u = ""
            for i in range(M): # inverting substitution
                u += Ps_inv[ v[i*L : i*L + L] ]
        
        x_vec.append(w)
    
    return ''.join(x_vec)


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
    x_decrypted = decrypt(y, Ps, Pp, kr)
    print(x_decrypted == x)
    

if __name__ == "__main__":
    __main__()
