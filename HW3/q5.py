#q5 generators generator (mod p), assume p = 2q + 1
from sympy.ntheory import factorint

#Smallerst Generator
def smallest_generator(p):
    factors = factorint(p - 1)
    for g in range(2, p):
        is_generator = True
        for q, e in factors.items():
            if pow(g, (p - 1) // q, p) == 1:
                is_generator = False
                break
        if is_generator:
            return g
    return None

def largest_generator(p):
    large = p-1
    return large

def sorted_all_generators(p, lg):
    generators = []
    for g in range(2, p):
        if pow(g, (p - 1) // 2, p) != 1:  # Check if g is a generator
            generators.append(g)
    return sorted(generators)


if __name__ == "__main__":
    p = 42443
    lg = largest_generator(p)
    all_gens = sorted_all_generators(p, lg)
    print(f"All generators (mod {p}) are: {all_gens}")