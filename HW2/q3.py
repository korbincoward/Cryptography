from Crypto.Util.number import bytes_to_long
from Crypto.Random import get_random_bytes

# Pad using PKCS 1.5 (usethe get random bytes function)
def pad_message(m):
    padding = get_random_bytes(6)
    padded_message = b'\x00\x02' + padding + b'\x00'  + m
    return padded_message

# Send to integer
def to_integer(padded_message):
    integer_message = bytes_to_long(padded_message)
    return integer_message

# Encrypt
#CHANGE VARIABLES
def rsa_encrypt(integer_message, e, n):
    encrypted = integer_message**e % n
    return encrypted


# This is the main function
if __name__ == "__main__":
    p = 335910234816891326223689712258364224799
    q = 287921464271584130823331845246834817939
    n = p * q
    e = 65537
    m = b'Does this need padding?'

    padded = pad_message(m)

    integer = to_integer(padded)

    encrypted = rsa_encrypt(integer, e, n)

    print(encrypted)