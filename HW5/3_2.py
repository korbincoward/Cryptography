from typing import Tuple

def elliptic_curve_addition(p, q, ec: Tuple[int, int, int]):
    """Adds points

    Args:
        p (tuple[int, int] | 0): a point, or 0 for the point at infinity
        q (tuple[int, int] | 0): a point, or 0 for the point at infinity
        ec (tuple[int, int, int]): an elliptic curve (a, b, m) such that y^2 = x^3 + ax + b (mod m)

    Returns:
        tuple[int, int] | 0: p+q
    """
    # your code here
    a, b, p = ec

    if p == 0:
        return q
    if q == 0:
        return p 
    if p != q:
        if p[0] == q[0] and p[1] != q[1]:
            return 0
        m = (q[1] - p[1]) * pow(q[0] - p[0], -1, p) % p
    else:
        if p[1] == 0:
            return 0
        m = (3 * p[0] * p[0] + a) * pow(2 * p[1], -1, p) % p

    x = (m * m - p[0] - q[0]) % p
    y = (m * (p[0] - x) - p[1]) % p

    return (x, y)


curve = (4, 3, 7)
points = [0, (1, 1), (1, 6), (3, 0), (5, 1), (5, 6)]

# right number of points?

print('⊕, ' + ', '.join(str(p) for p in points))
for p in points:
    print(str(p) + ', ' + ', '.join(str(elliptic_curve_addition(p, q, curve))
          for q in points))