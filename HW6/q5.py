### AES Info
from Crypto.Util import Counter
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# Message to encrypt
KEY = b'fefd47cb7691a801'
message = b'Good idea! Counter mode is much safer!'
# Instantiate cipher
iv = b'0000000000000000'
count = Counter.new(128, initial_value=int.from_bytes(iv, "big"))
ctr = AES.new(KEY, AES.MODE_CTR, counter=count)
# Pad the message to 16 bytes
padded_message_c = pad(message, 16)

### Your code here
# Encrypt
CIPHERTEXT = ctr.encrypt(padded_message_c)
print(CIPHERTEXT)

ctr_d = AES.new(KEY, AES.MODE_CTR, counter=count)
m = ctr_d.decrypt(CIPHERTEXT)
print(m)