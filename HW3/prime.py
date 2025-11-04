
from sympy.ntheory.modular import crt
from sympy import isprime, sqrt_mod

def initial_check(x, N):
    if pow(x, (N - 1) // 2, N) != 1:
        return False
    return True

def sqr_root(x, N):
    if N % 4 != 3:
        raise ValueError("This square root method requires N ≡ 3 (mod 4)")
    root = pow(x, (N + 1) // 4, N)
    other_root = N - root
    return root, other_root

def square_roots_mod_N(x, p, q):
    # Verify inputs
    N = 1635957203043154274708445330334049124282456311405668071331837876976511901458765646240912421221627
    if p * q != N:
        raise ValueError(f"p * q = {p * q} does not equal N = {N}")
    if N % p != 0 or N % q != 0:
        raise ValueError("p and q must divide N")
    if not (isprime(p) and isprime(q)):
        raise ValueError("p and q must be prime")
    if p <= 2 or q <= 2 or p % 2 == 0 or q % 2 == 0:
        raise ValueError("p and q must be odd primes greater than 2")
    
    # Check if x is a quadratic residue mod p and q
    if not (initial_check(x, p) and initial_check(x, q)):
        return []
    
    # Compute square roots mod p and q
    try:
        # Use provided sqr_root if p, q ≡ 3 (mod 4)
        p_roots = sqr_root(x, p) if p % 4 == 3 else sqrt_mod(x, p, all_roots=True)
        q_roots = sqr_root(x, q) if q % 4 == 3 else sqrt_mod(x, q, all_roots=True)
    except ValueError as e:
        # Fallback to sympy's sqrt_mod for general primes
        p_roots = sqrt_mod(x, p, all_roots=True)
        q_roots = sqrt_mod(x, q, all_roots=True)
    
    # Combine using CRT
    roots = []
    for rp in p_roots:
        for rq in q_roots:
            s = crt([p, q], [rp, rq])[0]
            roots.append(s % N)
    
    return sorted(roots)

if __name__ == "__main__":
    x = 152306056642756
    N = 1635957203043154274708445330334049124282456311405668071331837876976511901458765646240912421221627
    
    # User must provide p and q (from Question 2)
    # Example placeholders (replace with actual factors)
    p = 94224140758709045574439817763475554001183567290945416659001127166105278949619 # Placeholder; replace with actual p
    q = N // p if N % p == 0 else None
    
    try:
        if q is not None and p * q == N:
            roots = square_roots_mod_N(x, p, q)
            print(f"Square roots of {x} mod {N} are: {roots}")
            # Verify
            for s in roots:
                assert (s * s) % N == x, f"Verification failed for s={s}"
        else:
            print("Please provide valid prime factors p and q from Question 2 such that p * q = N.")
    except Exception as e:
        print(f"Error: {e}. Provide odd prime factors p, q > 2 such that p * q = N and N mod p = N mod q = 0.")