from sympy.ntheory.modular import crt

def square_root_p(m, p):
    root_p = pow(m, (p + 1) // 4, p)
    other_root = p - root_p
    return root_p, other_root

def square_root_q(m, q):
    root_q = pow(m, (q + 1) // 4, q)
    other_root = q - root_q
    return root_q, other_root

def combined_roots(r1, r2, p, q):
    roots = []
    for i in r1:
        for j in r2:
            root, _ = crt([p, q], [i, j])
            roots.append(root)
    return roots

def rabin_sig_small(c, p, q):
    r1 = square_root_p(c, p)
    r2 = square_root_q(c, q)
    return min(combined_roots(r1, r2, p, q))

if __name__ == "__main__":
    m = 29145765213596037567933908110811738031693497264838408123352236406610909163848314214108271238945108258420996669781007382750276075890920252250448539800909071
    p = 10740819841097751335499586682618798237457266465572129738235918253106012974830421448470148776104908084511065829564871464692573846675336610937250884901101371
    q = 11757968468377935899868299609744702022188683024633696955181982801388587923875501094690676011523282681500510891352437295808775918005080566975777467820475631
    N = p * q

    signature = rabin_sig_small(m, p, q)
    print(f"Signature (smallest root): {signature}")