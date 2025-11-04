from random import randint
from typing import Tuple
def find_generator(P: int) -> int:
    q = (P-1) // 2
    for g in range(2, P):
        if pow(g, 2, P) != 1 and pow(g, q, P) != 1:
            return g

def generate_keys(p: int, g: int) -> Tuple[int, int]:
    priv = randint(2, p-2)
    pub = g ** priv % p
    return priv, pub

def encrypt(m: int, p: int, g: int, pub: int) -> Tuple[int, int]:
    k = randint(2, p-2)
    gamma = g ** k % p
    delta = (m * pub ** k) % p
    c = (gamma, delta)
    return c

def decrypt(c: Tuple[int, int], p: int, priv: int) -> int:
    gamma, delta = c
    d = delta * (gamma ** (p - 1 - priv)) % p
    return d
    


P = 1000667
G = find_generator(P)
Bob_Priv, Bob_Pub = generate_keys(P, G)
# Alice wants to encrypt the number 5 using Bob's public key.
M = 5
print(f"encrypt {M} with {Bob_Pub}")
C = encrypt(M, P, G, Bob_Pub)
print(f"ciphertext: {C}")
print(f"decrypt with {Bob_Priv}")
d = decrypt(C, P, Bob_Priv)
print(f"decrypted: {d}")
# decrypted text should match original message
print(M == d)