# find all square roots of x (mod p)

#Check existence of square root
def initial_check(x, q):
    if pow(x, (q - 1) // 2, q) != 1:
        return False
    return True

def sqr_root (x,q):
    root = pow(x, (q + 1) // 4, q)
    other_root = q - root
    return root, other_root


if __name__ == "__main__":
    x = 99999980000001
    q = 17362399804022031833

    if initial_check(x, q):
        print("Square root exists.")
        root, other_root = sqr_root(x, q)
        print(f"Square roots are: {root}, {other_root}")
    else:
        print("No square root exists.")
