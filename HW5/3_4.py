from typing import Tuple
def elliptic_curve_addition(p, q, ec: Tuple[int, int, int]):
    a, b, m = ec
    if p == 0:
        return q
    if q == 0:
        return p
    
    x1, y1 = p
    x2, y2 = q
    if x1 == x2 and (y1 != y2 or y1 == 0):
        return 0
    
    if p != q:
        lam = (((y2 - y1) % m)) * pow((x2 - x1) % m, -1, m) % m
    else:
        lam = ((3 * x1 * x1 + a) % m) * pow((2 * y1) % m, -1, m) % m

    x3 = (lam * lam - x1 - x2) % m
    y3 = (lam * (x1 - x3) - y1) % m
    return (x3, y3)

def elliptic_curve_scalar_multiplication(n, p, ec):
    if n == 0 or p == 0:
        return 0
    if n < 0:
        raise ValueError("Negative scalar not supported")
    result = 0
    addend = p

    while n:
        if n & 1:
            result = elliptic_curve_addition(result, addend, ec)
        addend = elliptic_curve_addition(addend, addend, ec)
        n >>= 1

    return result

curve = (4, 3, 7)
points = [0, (1, 1), (1, 6), (3, 0), (5, 1), (5, 6)]

# Test out scalar multiplication
for p in points: print(elliptic_curve_scalar_multiplication(5, p, curve))