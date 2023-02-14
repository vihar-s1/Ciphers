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
- The encryption function is defined as $ y = a*x + b (mod 26) $ where $x$ is plain text and $y$ is the cipher text.
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

 ![Alt text](CipherDiagrams.png)

### ___4. Hill Cipher___

## Private Key Cryptography

---
