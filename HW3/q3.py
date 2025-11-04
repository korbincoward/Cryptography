# q3.py
from sympy.ntheory.modular import crt

#Check square root existence p
def initial_check(x, p):
    if pow(x, (p - 1) // 2, p) != 1:
        return False
    return True

#check square root existence q
def initial_check_q(x, q):
    if pow(x, (q - 1) // 2, q) != 1:
        return False
    return True

#find square roots mod p
def sqr_root_p(x, p):
    root_p = pow(x, (p + 1) // 4, p)
    other_root = p - root_p
    return root_p, other_root

#find square roots mod q
def sqr_root_q(x, q):
    root_q = pow(x, (q + 1) // 4, q)
    other_root = q - root_q
    return root_q, other_root

#combined using CRT
def combined_roots(r1, r2, p, q):
    roots = []
    for i in r1:
        for j in r2:
            root, _ = crt([p, q], [i, j])
            roots.append(root)
    return roots

if __name__ == "__main__":
    p = 91689059391615735459809475744226276082656004847866561896994615680154741272351
    q = 106695181190409920707145778047953474615923687476150177257616248092564795457559
    x = 152306056642756
    N = p * q
    if initial_check(x, p) and initial_check_q(x, q):
        print("Square root exists.")
        r1 = sqr_root_p(x, p)
        r2 = sqr_root_q(x, q)
        print(f"Square roots mod p: {r1}")
        print(f"Square roots mod q: {r2}")
        roots = combined_roots(r1, r2, p, q)
        print(f"Combined square roots mod N: {roots}")
    else:
        print("No square root exists.")
             