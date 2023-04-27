from Crypto.Cipher import Salsa20
import timeit
import os
import sys

def generate_random_string(size):
    return os.urandom(size)

print("Salsa 20")
message_size = 50
iterations = 10

try:
    if (sys.argv[1]):
        message_size = int(sys.argv[1])
    if (sys.argv[2]):
        iterations = int(sys.argv[2])
except:
    print ('No size passed, using default...')

print(message_size, 'KB')



plaintext = generate_random_string(message_size * 1000)
secret = b'*Thirty-two byte (256 bits) key*'
cipher = Salsa20.new(key=secret)

def enc():
    global ciphertext
    global msg_nonce
    msg = cipher.nonce + cipher.encrypt(plaintext)
    msg_nonce = msg[:8]
    ciphertext = msg[8:]

print('encryption time = ', timeit.timeit(enc, number=iterations) / iterations, ' seconds')

# print(ciphertext)

cipher = Salsa20.new(key=secret, nonce=msg_nonce)

# plaintext2 = cipher.decrypt(ciphertext)
def dec():
    global plaintext2
    plaintext2 = cipher.decrypt(ciphertext)

print('decryption time = ',  timeit.timeit(dec , number=iterations) / iterations, ' seconds')

# print(plaintext2)

if (plaintext == plaintext2 and plaintext != ciphertext):
    print('successful encryption and decryption')
