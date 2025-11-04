from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


# From Alice
ciphertext = b'\x9bI\xc9up\xb66\x9ei\xd0\xad|9\x83\x90\x15\xdaC\x91\xb4\x0c\x1f\x1b\x94\xe1|XT\xac}H\xe1\x16 \n\xf8q\x85\x88\x8f\xd7\x1f$1"h\xe1\x9f\xc9_-1\xb1\xb1\xf6\xf2j\x1f7\x17h\x90J\xda$\nBq\r\x82\x81\xa5\x94C\x1cs\xab|\xf2\xed'
# Instantiate cipher
KEY = b'fefd47cb7691a801' #OUR ANSWER FROM PROBLEM 2 HERE
ecb = AES.new(KEY, AES.MODE_ECB)
# Decrypt
plaintext = ecb.decrypt(ciphertext)
print(plaintext)

