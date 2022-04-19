from Crypto.Cipher import AES

# AES = https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html

key = b'Sixteen byte key'
cipher = AES.new(key, AES.MODE_EAX)
data = b'testing1'

nonce = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(data)
print(data)
print(ciphertext)
