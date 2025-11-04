from Crypto.Util.number import inverse, long_to_bytes

def rsa_private_exponent(e, p, q):
    phi = (p - 1) * (q - 1)
    d = inverse(e, phi)                 # integer-only modular inverse
    assert (e * d) % phi == 1
    return d

def rsa_decrypt_crt(c, p, q, d):
    # Fast CRT decryption
    dp = d % (p - 1)
    dq = d % (q - 1)
    q_inv = inverse(q, p)               # q^{-1} mod p

    m_p = pow(c % p, dp, p)             # residue mod p
    m_q = pow(c % q, dq, q)             # residue mod q
    h   = ((m_p - m_q) * q_inv) % p
    m   = (m_q + h * q) % (p * q)       # recombined plaintext
    # sanity: residues must match
    assert m % p == m_p and m % q == m_q
    return m

def unpad_pkcs1_v15(em_bytes):
    # Expect: 0x00 0x02 | PS(nonzero) | 0x00 | message
    if not (len(em_bytes) >= 11 and em_bytes[0:2] == b"\x00\x02"):
        raise ValueError("invalid PKCS#1 v1.5 block header")
    sep = em_bytes.find(b"\x00", 2)
    if sep == -1 or sep < 10:           # PS must be at least 8 bytes
        raise ValueError("invalid PKCS#1 v1.5 padding")
    return em_bytes[sep + 1 :]

if __name__ == "__main__":
    p = 10673585719279665473310785388809669669827495362644286487427766542984809154391774765485854883610369756608204700790356517751387480698580878567593785856635021
    q = 6801334650131872745100299405831872371467187219746984573007166981820210520799713374997311752074140392395671619494333585234488533763864323057595123498456717
    e = 65537
    c = 31029421912610013193482419338216502952367283645622657889245995909297764437818596436114368253165886669215669070940614892768690061512166984939183394299457806809026671545515156113505614812843993899123893076060950591176892398940431231398895335882540136212152702621891181190657264054423923779948236979386187588460

    n = p * q
    d = rsa_private_exponent(e, p, q)

    # Decrypt with CRT
    m = rsa_decrypt_crt(c, p, q, d)

    # Optional: cross-check (should match original ciphertext)
    assert pow(m, e, n) == c

    # Convert to full-length block (keep leading zeros)
    k = (n.bit_length() + 7) // 8
    em = long_to_bytes(m, k)

    # Unpad and print
    msg = unpad_pkcs1_v15(em)
    try:
        print(msg.decode("utf-8"))
    except UnicodeDecodeError:
        print(msg)  # raw bytes if not UTF-8