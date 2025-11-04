from typing import Tuple

def elliptic_curve_validate(point, ec: Tuple[int, int, int]) -> bool:
    if point == 0:
        return True
    a, b, p = ec
    x,y = point
    if (y ** 2) % p == (x * x * x + a * x + b) % p:
        return True
    return False

    """Checks if point is on curve

    Args:
        point (tuple[int, int] | 0): a point, or 0 for the point at infinity
        ec (tuple[int, int, int]): an elliptic curve (a, b, m) such that y^2 = x^3 + ax + b (mod m)

    Returns:
        bool: True if the point is on the curve, False otherwise
    """


curve = (4, 3, 7)
points = [0, (1, 1), (1, 6), (3, 0), (5, 1), (5, 6)]

# are all the points valid?
print(all([elliptic_curve_validate(p, curve) for p in points]))