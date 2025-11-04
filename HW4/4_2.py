from typing import Tuple, List
from random import randint
import random
import math

def find_generator(P: int) -> int:
    q = (P-1) // 2
    for g in range(2, P):
        if pow(g, 2, P) != 1 and pow(g, q, P) != 1:
            return g

def generate_keys(Prime: int, g: int) -> Tuple[int, int]:
    priv_key = randint(2, Prime-2)
    pub = g ** priv_key % Prime
    return priv_key, pub

def elgamal_mult(p: int, c1: Tuple[int, int], c2: Tuple[int, int]) -> Tuple[int, int]:
    gamma1, delta1 = c1
    gamma2, delta2 = c2
    gamma = (gamma1 * gamma2) % p
    delta = (delta1 * delta2) % p
    return (gamma, delta)

def encrypt(m: int, p: int, g: int, pub: int) -> Tuple[int, int]:
    k = randint(2, p-2)
    gamma = g ** k % p
    delta = (m * pub ** k) % p
    c = (gamma, delta)
    return c

class Ballot:
    def __init__(self, prime, generator, pub_key):
        self.p = prime
        self.g = generator
        self.pub = pub_key

    def mark(self, choice: bool) -> Tuple[int, int]:
        return encrypt(int(choice)+1, self.p, self.g, self.pub)

def tabulate(Prime: int, votes: List[Tuple[int, int]]):
    # Sanity check
    tally = (1, 1)  # could/should be encrypted
    for v in votes:
        tally = elgamal_mult(Prime, tally, v)

    return tally

#returns the number of True votes
def reveal(ciphertext: Tuple[int, int], p: int, priv_key: int) -> int:
    gamma, delta = ciphertext
    d = delta * (gamma ** (p - 1 - priv_key)) % p
    count = int(math.log(d, 2))
    return count

# Setup ElGamal
Prime = 1000667
g = find_generator(Prime)
Priv_Key, pub_key = generate_keys(Prime, g)
# Get voting machine
ballots = Ballot(Prime, g, pub_key)
# Get 10 random votes
Votes = random.choices([True, False], k=10)
print(f"Votes: {Votes}")
Encrypted = [ballots.mark(v) for v in Votes]
print(f"Encrypted: {Encrypted}")
Tally = tabulate(Prime, Encrypted)
print(f"Tally: {Tally}")
