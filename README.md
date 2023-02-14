# Ciphers

Consists of implementations of various classical and private key cryptographic algorithms.

## Classical Cryptography Ciphers
<hr>

### Shift Cipher
The most basic form of cipher. It involves shifting operation of the plain text to generate cipher text. Based on the key selected from 0 to 25, the alphabet is shifted by that much to obtain the encryted text.

> - encrypt( text="Hello World", key=5 ) <br>
> - The function returns following string: "mjqqt btwqi" (without space)

> - decrypt( text="mjqqt btwqi", key=5 ) <br>
> - The function returns following string: "hello world" (without space)


### Affine Cipher
- Affine cipher uses a pair of numbers (a, b) as key where $a, b \in \Z_{26}$.
- The encryption function is defined as $ y = a*x + b (mod 26) $ where $x$ is plain text and $y$ is the cipher text.
- Similarly decryption function performs following operation $ x = a^{-1} * (y - b) (mod 26) $.
- Note that as we use $a^{-1}$ here and $a\in\Z_{26}$ which a ring. So $a$ must be an invertible element of $\Z_{26}$. Otherwise, decryption is not possible.

> - encrypt( text="Hello World", key_a=5, key_b=10 ) <br>
> - The function returns following string: "tennc qcrnz" (without space)

> - decrypt( text="tennc qcrnz", key_a=5, key_b=10 ) <br>
> - The function returns following string: "hello world" (without space)

## Private Key Cryptography
<hr>