# Private Key Cryptography

## ___1. Substitution Permutation Network (SPN)___

As the name suggests, SPN cipher performs two operations, namely, Substitution and Permutation operation on the input bitstream $P$.

- The Substitution Box $P_S$ maps L-bits-long bitstream to another L-bits long bitstream.
- The Permutation Box $P_P$ contains mapping to permute the given $L*M$ bits long bitstream.
- This process is repeated for $N$ number of times, each time adding the corresponding round key $K_r$ in the beginning using $XOR$ operation.
- The decryption process is simply following these steps in reverse for N rounds.

    ```python
    encrypt(x='0010011010110111', Ps, Pp, kr)
    ```
    > Here Ps, Pp, and Kr are the substitution-box, permutation-box and the list of round-keys respectively.
    > The value of N is determined on the basis of size of the list Kr
    > The output returned is '1011110011010110' for the example in the code

    ```python
    decrypt(y="1011110011010110", Ps, Pp, Kr)
    ```
    > Here the Ps, Pp, and Kr are the substitution-box, permutation-box and the list of round-keys respectively used as it is for encryption.
    > The corresponding inverses are calculated before actually performing decryption
    > The value of N is determined on the basis of size of the list Kr
    > The out returns are '0010011010110111' for the example in the code

## ___2. Data Encryption Standard (DES)___
