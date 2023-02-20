# Ciphers

Consists of implementations of various classical and private key cryptographic algorithms.

## `NOTE`

> ___The `setup.py` file sets the `Extras` module globally on the system or the virtual environment on which the code will be running. This to allow access to the supporting modules in the `Extras` folder.___

> ___Make sure to run the following code from the terminal opened in the root folder:___

```bash
python setup.py install
```

## Classical Cryptography Ciphers

---

### ___1. Shift Cipher___

The most basic form of cipher. It involves shifting operation of the plain text to generate cipher text. Based on the key selected from 0 to 25, the alphabet is shifted by that much to obtain the encryted text.

- The encryption occurs as $C=P+k{\ }(mod{\ }26)$
- The encryption occurs as $P=C-k{\ }(mod{\ }26)$

```python
encrypt( text="Hello World", key=5 )  
# The function returns following string: "mjqqtbtwqi"

decrypt( text="mjqqt btwqi", key=5 )  
# The function returns following string: "helloworld"
```

### ___2. Affine Cipher___

Affine cipher uses a pair of numbers (a, b) as key where $a, b \in \Z_{26}$. For plain text $P$ and cipher text $C$,

- The encryption function is defined as $C = a*P + b{\ }(mod{\ }26)$.
- The decryption function is defined as $P = a^{-1} * (C - b)(mod{\ }26)$.

Note that as we use $a^{-1}$ here and $a\in\Z_{26}$ which a ring. So $a$ must be an invertible element of $\Z_{26}$. Otherwise, decryption is not possible.

```python
encrypt( text="Hello World", key_a=5, key_b=10 )  
# The function returns following string: "tenncqcrnz"

decrypt( text="tennc qcrnz", key_a=5, key_b=10 )  
# The function returns following string: "helloworld"
```

### ___3. Autokey Cipher___

- Auto-key cipher uses the plain text to generate shift key for the cipher text.
- The seed key is used to shift the first character of the text. The next character is shifted by the index of the previous character and so on.
- As it is a shifting operation, all 26 elements in $\Z_{26}$ can be used as keys.

```python
encrypt( text="Hello World", key=5 )
# The function returns following string: "mlpwzkkfco"

decrypt( text="mlpwzkkfco", key=5 )
# the function returns following string: "helloworld"
```

 ![Autokey Encryption Process](https://user-images.githubusercontent.com/96971096/219880843-d2ba1256-81e1-438e-a534-472e96b8849d.png)

### ___4. Hill Cipher___

- Hill Cipher performs encryption and decryption process using a square matrix as key.
 Here, $C$ is the cipher text, $P$ is the plain text, and $k$ is the key, all in matrix form.

- The encryption function is defined as $C = P*k$
- The decryption function is defined as $P = C*k^{-1}$

The module also contains an additional functionality called ___findKey___ which takes a cipher text plain text as input and attempts to find the corresponding encryption matrix using equation $k = P^{-1}*C$
  
- Key matrix used is $\begin{bmatrix}3&21&20\\4&15&23\\6&14&5\end{bmatrix}$

```python
encrypt( plainText="breathtaking", key=[[3,21,20],[4,15,23],[6,14,5]] )
# returns "rupotentoifv"

decrypt( cipherText="rupotentoifv", key=[[3,21,20],[4,15,23],[6,14,5]] )
# returns "breathtaking"

findKey( plainText="breathtaking", cipherText="rupotentoifv" )
# returns the key matrix: [[3,21,20],[4,15,23],[6,14,5]]  
```

### ___5. Affine-Hill Cipher___

Affine-Hill Cipher is the combination of Affine cipher and Hill cipher.
Instead of using integers as key elements in affine cipher, we use matrix and vector to perform encryption.

- The key $k=(a,b)$ is modified to $k=(L,b)$ where $L=[l_{ij}]_{n{\times}n}$ and $b=[b_{ij}]_{1{\times}n}$.

For the cipher text matrix $C$ and plain text matrix $P$,

- The encryption process is defined as $C=P{\times}L+b{\ }(mod{\ }26)$.
- The decryption process is defined as $P=(C-b)*L^{-1}(mod{\ }26)$.

- using following (L, b) pair for encryption,

$$L=\begin{bmatrix}3&6&4\\5&15&18\\17&8&5\end{bmatrix} {\ }and{\ } b=\begin{bmatrix}8&13&1\end{bmatrix}$$

```python
encrypt( plainText="adisplayedequation", L=[[3,6,4],[5,15,18],[17,8,5]], b=[8,13,1])
# returns encrypted string "dsrmsioplxljbzullm"

findKey( plainText="adisplayedequation", cipherText="dsrmsioplxljbzullm" )
# returns key pair L=[[3,6,4],[5,15,18],[17,8,5]] and b=[8,13,1]
```

## Private Key Cryptography

---

### ___1. Substitution Permutation Network (SPN)___

As the name suggests, SPN cipher performs two operations, namely, Substitution and Permutation operation on the input bitstream $P$.

- The Substitution Box $P_S$ maps L-bits long bitstream to another L-bits long bitstream.
- The Permutation Box $P_P$ contains mapping to permute the given $L*M$ bits long bitstream.
- This process is repeated for $N$ number of times, each time adding the corresponding round key $K_r$ in the beginning using $XOR$ operation.

```python
encrypt(x='0010011010110111', Ps, Pp, kr)
# Here Ps, Pp, and Kr are the substitution-box, permutation-box and the list of round-keys respectively.

# The value of N is determined on the basis of size of the list Kr
# The output returned is '1011110011010110' for the example in the code
```

### ___2. Data Encryption Standard (DES)___
