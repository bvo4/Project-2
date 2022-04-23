
from datetime import datetime
# AES = https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import json

data = b"secret"
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_CBC)
ct_bytes = cipher.encrypt(pad(data, AES.block_size))
iv = b64encode(cipher.iv).decode('utf-8')
ct = b64encode(ct_bytes).decode('utf-8')
result = json.dumps({'iv':iv, 'ciphertext':ct})
print(result)

# We assume that the key was securely shared beforehand
try:
    b64 = json.loads(result)
    iv = b64decode(b64['iv'])
    ct = b64decode(b64['ciphertext'])
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    print("The message was: ", pt)
except (ValueError, KeyError):
    print("Incorrect decryption")


key = b'Sixteen byte key'
cipher = AES.new(key, AES.MODE_CBC)
data = b'testing1'
"""
# Encrypting
start_time = datetime.now()
#once = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(data)
end_time = datetime.now()
print(end_time - start_time)

# Decrypting
start_time = datetime.now()
cipher = AES.new(key, AES.MODE_CBC)
data = cipher.decrypt_and_verify(ciphertext, tag)
end_time = datetime.now()
print(end_time - start_time)
print(data)
"""
# Triple DES
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

while True:
    try:
        key = DES3.adjust_key_parity(get_random_bytes(24))
        break
    except ValueError:
        pass
key = get_random_bytes(16)
cipher = DES3.new(key, DES3.MODE_CBC)
plaintext = b'We are no longer knights who say ni!'
plaintext_padded = pad(plaintext, 8)
end = cipher.encrypt(plaintext_padded)
cipher = DES3.new(key, DES3.MODE_CBC)
dec =unpad(cipher.decrypt(end), DES3.block_size)
#dec = cipher.decrypt(end)
print(dec, DES3.block_size)
