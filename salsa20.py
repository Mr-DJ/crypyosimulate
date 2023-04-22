import os
import datetime
from Crypto.Cipher import Salsa20


# generate a random string of a given size in bytes
def generate_random_string(size):
    return os.urandom(size)


# check if plain text matches decrypted text
def decryption_success(plaintext, decryptedtext):
    return (plaintext == decryptedtext)


# 1. create text
# plaintext = b'I am sending the encrypted message.'
plaintext = generate_random_string(53452800)

# get the start datetime
st = datetime.datetime.now()

# 2. create a key
key = b'*Thirty-two byte (256 bits) key*'

# 3. encrypt the message by key
cipher = Salsa20.new(key=key)
msg = cipher.nonce + cipher.encrypt(plaintext)
msg_nonce = msg[:8]  # randomly generated number
ciphertext = msg[8:]

# get the end datetime
et = datetime.datetime.now()

# get execution time
elapsed_time = et - st
elapsed_time = elapsed_time.total_seconds() * 1000
print('Encryption time:', elapsed_time, 'milliseconds')

# print(plaintext)   receiver can see only after decoding ciphertext
# print(cipher.nonce)   a byte string you must send to the receiver too to decrypt, cipher = Salsa20.new(key=key, nonce=msg_nonce)
# print(ciphertext)   encoded ciphertext received by receiver

decryptedtext = cipher.decrypt(ciphertext)

cipher = Salsa20.new(key=key, nonce=msg_nonce)
plaintext2 = cipher.decrypt(ciphertext)
print(decryption_success(plaintext, plaintext2))
