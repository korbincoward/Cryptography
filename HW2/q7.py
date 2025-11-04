import math
from Crypto.Util.number import inverse
from Crypto.Util.number import long_to_bytes

def rsa_d (e, phi_n):
    k = 1
    while True:
        d = (1 + (k * (phi_n))) / e
        if d.is_integer():
            return int(d)
        k += 1

# Split ciphertext (mod p) and (mod q)
def split_cipher (c, p, q):
    split_p = c % p
    split_q = c % q
    return split_p, split_q

# Perform RSA decryption (mod p) and (mod q)
def rsa_decrypt(split_p, split_q, d, n):
    decrypted_p = pow(split_p, d, n)
    decrypted_q = pow(split_q, d, n)
    return decrypted_p, decrypted_q

# Use CRT code to re-combine the answer (mod N)
def crt(p, q, d, decrypted_p, decrypted_q):
    # recombine residues (decrypted_p ≡ m (mod p), decrypted_q ≡ m (mod q))
    # q_inv is inverse of q modulo p
    q_inv = inverse(q, p)
    # h fixes the difference so that m = decrypted_q + h*q satisfies m ≡ decrypted_p (mod p)
    h = (q_inv * (decrypted_p - decrypted_q)) % p
    m = (decrypted_q + h * q) % (p * q)
    return m

#Decode the result to see the padded message
def unpad_pkcs1_v15(em_bytes):
    # em_bytes should be exactly k bytes
    if not em_bytes.startswith(b'\x00\x02'):
        raise ValueError("invalid padding")
    sep = em_bytes.find(b'\x00', 2)
    if sep < 10:
        raise ValueError("invalid padding/PS too short")
    return em_bytes[sep+1:]

if __name__ == "__main__":

    p = 10673585719279665473310785388809669669827495362644286487427766542984809154391774765485854883610369756608204700790356517751387480698580878567593785856635021
    q = 6801334650131872745100299405831872371467187219746984573007166981820210520799713374997311752074140392395671619494333585234488533763864323057595123498456717
    e = 65537
    c = 31029421912610013193482419338216502952367283645622657889245995909297764437818596436114368253165886669215669070940614892768690061512166984939183394299457806809026671545515156113505614812843993899123893076060950591176892398940431231398895335882540136212152702621891181190657264054423923779948236979386187588460
    n = p * q
    phi_n = (p-1) * (q-1)
    d = rsa_d (e, phi_n)
    split_p, split_q = split_cipher (c, p, q)
    decrypted_p = rsa_decrypt(split_p, d, p, n)
    decrypted_q = rsa_decrypt(split_q, d, q, n)
    decrypted = crt(p, q, d, decrypted_p, decrypted_q)
    unpad = unpad_pkcs1_v15(long_to_bytes(decrypted))

    print(unpad)




    