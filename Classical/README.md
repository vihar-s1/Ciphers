# Classical Cryptography Ciphers

## ___1. Shift Cipher___

The most basic form of cipher. It involves shifting operation of the plain text to generate cipher text. Based on the key selected from 0 to 25, shift the alphabet by that many places to get the corresponding encrypted character.

- The encryption occurs as $C=P+k{\ }(mod{\ }26) $
  - The encryption occurs as $P=C-k{\ }(mod{\ }26) $

    ```python
    encrypt( text="Hello World", key=5 )  
    # The function returns following string: "mjqqtbtwqi"
        
    decrypt( text="mjqqt btwqi", key=5 )  
    # The function returns following string: "helloworld"
    ```

## ___2. Affine Cipher___

Affine cipher uses a pair of numbers (a, b) as key where $a, b \in Z_{26}$. For plain text $P$ and cipher text $C$,

- The encryption function is defined as $C = a*P + b{\ }(mod{\ }26) $.
- The decryption function is defined as $P = a^{-1} * (C - b)(mod{\ }26) $.

Note that as we use $a^{-1}$ here and $a\in Z_{26}$ which a ring. So $a$ must be an invertible element of $Z_{26}$. Otherwise, decryption is not possible.

  ```python
  encrypt( text="Hello World", key_a=5, key_b=10 )  
  # The function returns following string: "tenncqcrnz"
  
  decrypt( text="tennc qcrnz", key_a=5, key_b=10 )  
  # The function returns following string: "helloworld"
  ```

## ___3. Autokey Cipher___

- Auto-key cipher uses the plain text to generate a shift-key for the cipher text.
- The seed key is used to shift the first character of the text. The next character is shifted by the index of the previous character and so on.
- As it is a shifting operation, all 26 elements in $\Z_{26}$ can be used as keys.

  ```python
  encrypt( text="Hello World", key=5 )
  # The function returns following string: "mlpwzkkfco"
  
  decrypt( text="mlpwzkkfco", key=5 )
  # the function returns following string: "helloworld"
  ```

![Autokey Encryption Process](https://user-images.githubusercontent.com/96971096/219880843-d2ba1256-81e1-438e-a534-472e96b8849d.png)

## ___4. Hill Cipher___

- Hill Cipher performs an encryption and decryption process using a square matrix as a key.
  Here, $C$ is the cipher text, $P$ the plain text, and $k$ is the key, all in matrix form.

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

## ___5. Affine-Hill Cipher___

Affine-Hill Cipher is the combination of Affine cipher and Hill cipher.
Instead of using integers as key elements in affine cipher, we use matrix and vector to perform encryption.

- The key $k=(a, b)$ is modified to $k=(L, b)$ where $L=[l_{ij}]_{n{\times}n}$ and $b=[b_{ij}]_{1{\times}n}$.

For the cipher text matrix $C$ and plain text matrix $P$,

- The encryption process is defined as $C=P{\times}L+b{\ }(mod{\ }26) $.
- The decryption process is defined as $P=(C-b)*L^{-1}(mod{\ }26) $.

- using the following (L, b) pair for encryption,

$$L=\begin{bmatrix}3&6&4\\5&15&18\\17&8&5\end{bmatrix} {\ }and{\ } b=\begin{bmatrix}8&13&1\end{bmatrix}$$

  ```python
  encrypt( plainText="adisplayedequation", L=[[3,6,4],[5,15,18],[17,8,5]], b=[8,13,1])
  # returns encrypted string "dsrmsioplxljbzullm"
  
  findKey( plainText="adisplayedequation", cipherText="dsrmsioplxljbzullm" )
  # returns key pair L=[[3,6,4],[5,15,18],[17,8,5]] and b=[8,13,1]
  ```