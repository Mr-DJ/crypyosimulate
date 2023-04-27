from Crypto.Cipher import Salsa20
from datetime import datetime as dt
import os

def generate_random_string(size):
    return os.urandom(size)

print("Salsa 20")
message_size = 5344
print(message_size, 'KB')
plaintext = generate_random_string(message_size*1000)
secret = b'*Thirty-two byte (256 bits) key*'
cipher = Salsa20.new(key=secret)

start_time = dt.now()
msg = cipher.nonce + cipher.encrypt(plaintext)
msg_nonce = msg[:8]
ciphertext = msg[8:]
end_time = dt.now()
time_elapsed = (start_time-end_time).microseconds / 1000

print('encryption time = ', time_elapsed, ' milliseconds')

cipher = Salsa20.new(key=secret, nonce=msg_nonce)
start_time = dt.now()
plaintext2 = cipher.decrypt(ciphertext)
end_time = dt.now()
time_elapsed = (start_time-end_time).microseconds / 1000

print('decryption time = ', time_elapsed, ' milliseconds')

if (plaintext == plaintext2 and plaintext != ciphertext):
    print('successful encryption and decryption')
