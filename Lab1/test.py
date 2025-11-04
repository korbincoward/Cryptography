from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes

message = b'cyber202{Korbin Coward: This a great class!}'

recipient_key = RSA.import_key(open("kc_public.pem").read())
session_key = get_random_bytes(16)

cipher_rsa = PKCS1_OAEP.new(recipient_key)
enc_session_key = cipher_rsa.encrypt(session_key)

cipher_aes = AES.new(session_key, AES.MODE_EAX)
ciphertext, tag = cipher_aes.encrypt_and_digest(message)

with open("encrypted_message.bin", "wb") as f:
    f.write(enc_session_key)
    f.write(cipher_aes.nonce)
    f.write(tag)
    f.write(ciphertext)

bundle = enc_session_key + cipher_aes.nonce + tag + ciphertext

key_private = RSA.import_key(open("kc_private_key.pem").read())
h = SHA256.new(bundle)
signature = pkcs1_15.new(key_private).sign(h)

with open("signature.bin","wb") as f:
    f.write(signature)
    
print('signature:', signature)
