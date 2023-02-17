# Ciphers

Consists of implementations of various classical and private key cryptographic algorithms.

## Classical Cryptography Ciphers

---

### ___1. Shift Cipher___

The most basic form of cipher. It involves shifting operation of the plain text to generate cipher text. Based on the key selected from 0 to 25, the alphabet is shifted by that much to obtain the encryted text.

> - encrypt( text="Hello World", key=5 )  
> - The function returns following string: "mjqqt btwqi" (without space)

> - decrypt( text="mjqqt btwqi", key=5 )  
> - The function returns following string: "hello world" (without space)

### ___2. Affine Cipher___

- Affine cipher uses a pair of numbers (a, b) as key where $a, b \in \Z_{26}$.
- The encryption function is defined as $y = a*x + b (mod 26)$ where $x$ is plain text and $y$ is the cipher text.
- Similarly decryption function performs following operation $ x = a^{-1} * (y - b) (mod 26) $.
- Note that as we use $a^{-1}$ here and $a\in\Z_{26}$ which a ring. So $a$ must be an invertible element of $\Z_{26}$. Otherwise, decryption is not possible.

> - encrypt( text="Hello World", key_a=5, key_b=10 )  
> - The function returns following string: "tennc qcrnz" (without space)

> - decrypt( text="tennc qcrnz", key_a=5, key_b=10 )  
> - The function returns following string: "hello world" (without space)

### ___3. Autokey Cipher___

- Auto-key cipher uses the plain text to generate shift key for the cipher text.
- The seed key is used to shift the first character of the text. The next character is shifted by the index of the previous character and so on.
- As it is a shifting operation, all 26 elements in $\Z_{26}$ can be used as keys.

> - encrypt( text="Hello World", key=5 )
> - The function returns following string: "mlpwzkkfco"

> - decrypt( text="mlpwzkkfco", key=5 )
> - the function returns following string: "helloworld"

 ![AutoKey Encryption Process](AutoKeyEncryption.png)

### ___4. Hill Cipher___

- Hill Cipher performs encryption and decryption process using a square matrix as key.
- $C = P*k$ &nbsp;or&nbsp; $P = C*k^{-1}$
- Here, $C$ is the cipher text, $P$ is the plain text, and $k$ is the key, all in matrix form.
- The module also contains an additional functionality called ___findKey___ which takes a cipher text plain text as input and attempts to find the corresponding encryption matrix using equation $k = P^{-1}*C$
  
- Key matrix used is $KEY=\begin{bmatrix}3&21&20\\4&15&23\\6&14&5\end{bmatrix}$

> - encrypt( plainText="breathtaking", key=KEY )
> - returns "rupotentoifv"

> - decrypt( cipherText="rupotentoifv", key=KEY )
> - returns "breathtaking"

> - findKey( plainText="breathtaking", cipherText="rupotentoifv" )
> - returns the key matrix: $\begin{bmatrix}3&21&20\\4&15&23\\6&14&5\end{bmatrix}$  

### ___5. Affine-Hill Cipher___

## Private Key Cryptography

---
