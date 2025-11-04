from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.Cipher import PKCS1_OAEP, AES

pub  = RSA.import_key(open("kc_public.pem","rb").read())
priv = RSA.import_key(open("kc_private_key.pem","rb").read())

blob = open("encrypted_message.bin","rb").read()
sig  = open("signature.bin","rb").read()

klen = pub.size_in_bytes()        # 256 for 2048-bit
enc_sk = blob[:klen]
nonce  = blob[klen:klen+16]
tag    = blob[klen+16:klen+32]
ct     = blob[klen+32:]

bundle = enc_sk + nonce + tag + ct
pkcs1_15.new(pub).verify(SHA256.new(bundle), sig)  # raises if tampered

sk = PKCS1_OAEP.new(priv).decrypt(enc_sk)
pt = AES.new(sk, AES.MODE_EAX, nonce=nonce).decrypt_and_verify(ct, tag)
print(pt.decode())