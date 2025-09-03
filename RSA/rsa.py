import math

# RSA Encryption, finds the encryption key
# Sets e to 2 since e must be greater than 1
# Uses a while loop to find e
def rsa_e(n ,phi_n):
    e = 2
    while e < phi_n:
        gcd = math.gcd(e, phi_n)
        if gcd == 1:
            return e
        e += 1
# This function finds the decryption key value
def rsa_d (e, phi_n):
    k = 1
    while True:
        d = (1 + (k * (phi_n))) / e
        if d.is_integer():
            return int(d)
        k += 1
# This function encrypts a message
def rsa_encrypt(m, e, n):
    encrypted = m**e % n
    return encrypted
# This function decrypts a message
def rsa_decrypt(c, d, n):
    decrypted = c**d % n
    return decrypted
#This is the main function with the given values from Homework 1
if __name__ == "__main__":
    p = 53
    q = 61
    n = p * q
    phi_n = (p-1) * (q-1)
    e = rsa_e(n, phi_n)
    d = rsa_d(e, phi_n)
    m = 1514 
    c = 1121
# Print statements to show the values of N, Phi(N), e, d, C, and M
    print ("N=", n)
    print ("Phi(N)=", phi_n)
    print ("e = ", e)
    print ("d = ", d)
    print ("C = ", rsa_encrypt(m, e, n))
    print ("M = ", rsa_decrypt(c, d, n))
