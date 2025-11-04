
from Crypto.Util.number import bytes_to_long, long_to_bytes

# Given message
message = b'This is a message in bytes'

# Encode message to integer
encoded_message = bytes_to_long(message)

# Given integer to decode
encoding = 433214554660702248614242519417251105
decoded_message = long_to_bytes(encoding)

encoded_message, decoded_message

print(f"Encoded message: {encoded_message}")
print(f"Decoded message: {decoded_message}")    