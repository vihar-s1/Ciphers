'''
Calculating inverse of matrix over a finite ring.

IMP points:

- inverse of matrix A: A ^ -1 = adj(A) / det(A).
- ring: a set of integers inverible over addition but not neccesarily ove multiplication --> Zm.
- inverse exists for a in Zm iff gcd(a, m) = 1

- required modules
    - numpy
'''
import numpy as np

def inverse(matrix: list[list], m: int=26) -> list[list] | None:
    '''
    - Calculates matrix inverse over ring of size m.
    - default ring size is 26.
    - the function returns none while printing error string if matrix inverse is not calculated
    else it returns the inverse of the matrix
    '''
    A = np.array(matrix)
    
    dim = len(A)
    for row in A:
        if len(row) != dim:
            print(f"matrixInverse.py: inverse: [Error]: matrix A is not a square matrix and so inverse cannot be calculated")
            return None
            
    # matrix adjoint = matrix inverse * matrix determinant
    inv_A = np.linalg.inv(A)
    det_A = round(np.linalg.det(A))
    adj_A = inv_A * det_A
    
    if np.gcd(det_A, m) != 1:
        print(f"matrixInverse.py: inverse: [Error]: gcd(det(A), m) != 1 for det(A)={det_A} and m={m}")
        return None
    
    detA_inv_Zm = pow(round(np.linalg.det(A)), -1, m)
    inv_A_Zm = np.round_(detA_inv_Zm * adj_A) % m
    inv_A_Zm = inv_A_Zm.astype(int) # converting the matrix from float to integer
    
    return inv_A_Zm.tolist()
    
    
if __name__ == "__main__":
    P = [[1,17,4],[0,19,7],[19,0,10]]
    C = [[17,20,15],[14,19,4],[13,19,14]]
    
    P_inv = inverse(P)
    print(P_inv)
    print(np.matmul(P_inv, C) % 26)