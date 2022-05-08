
from datetime import datetime
# AES = https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import sys
import os
import json
import random 
import string

# AES
aes_enc = []
aes_dec = []



def aes_scheme(data):

    #data = b"secret"
    #print(data)

    start_time = datetime.now()

    key = get_random_bytes(16)
    #print(key)
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    result = json.dumps({'iv':iv, 'ciphertext':ct})

    end_time = datetime.now()
    aes_enc.append(end_time-start_time)

    # We assume that the key was securely shared beforehand
    start_time = datetime.now()
    try:
        b64 = json.loads(result)
        iv = b64decode(b64['iv'])
        ct = b64decode(b64['ciphertext'])
        cipher = AES.new(key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
    #    print("The message was: ", pt)
    except (ValueError, KeyError):
        print("Incorrect decryption")
    end_time = datetime.now()
    aes_dec.append(end_time-start_time)

# Triple DES
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

t_des_enc = []
t_des_dec = []

def triple_des_scheme(data):
    while True:
        try:
            key = DES3.adjust_key_parity(get_random_bytes(16))
            break
        except ValueError:
            pass

    start_time = datetime.now()
    key = get_random_bytes(16)
    cipher = DES3.new(key, DES3.MODE_CBC)
    #plaintext = b'We are no longer knights who say ni!'
    plaintext = data
    plaintext_padded = pad(plaintext, 8)
    end = cipher.encrypt(plaintext_padded)
    end_time = datetime.now()
    t_des_enc.append(end_time-start_time)

    start_time = datetime.now()
    cipher = DES3.new(key, DES3.MODE_CBC, cipher.iv)
    dec =unpad(cipher.decrypt(end), DES3.block_size)
    end_time = datetime.now()
    t_des_dec.append(end_time-start_time)


"""
found IDEA-CBC in cpp idk how to compile it
https://www.cryptopp.com/wiki/IDEA

No IDEA wtf this is 

https://cryptography.io/en/latest/development/custom-vectors/idea/?highlight=IDEA

# IDEA
import binascii

from cryptography.hazmat.primitives.ciphers import algorithms, base, modes # Cannot find the source to this not on the github


def encrypt(mode, key, iv, plaintext):
    cipher = base.Cipher(
        algorithms.IDEA(binascii.unhexlify(key)),
        mode(binascii.unhexlify(iv)),
    )
    encryptor = cipher.encryptor()
    ct = encryptor.update(binascii.unhexlify(plaintext))
    ct += encryptor.finalize()
    return binascii.hexlify(ct)


def build_vectors(mode, filename):
    with open(filename, "r") as f:
        vector_file = f.read().splitlines()

    count = 0
    output = []
    key = None
    iv = None
    plaintext = None
    for line in vector_file:
        line = line.strip()
        if line.startswith("KEY"):
            if count != 0:
                output.append(
                    "CIPHERTEXT = {0}".format(
                        encrypt(mode, key, iv, plaintext)
                    )
                )
            output.append("\nCOUNT = {0}".format(count))
            count += 1
            name, key = line.split(" = ")
            output.append("KEY = {0}".format(key))
        elif line.startswith("IV"):
            name, iv = line.split(" = ")
            iv = iv[0:16]
            output.append("IV = {0}".format(iv))
        elif line.startswith("PLAINTEXT"):
            name, plaintext = line.split(" = ")
            output.append("PLAINTEXT = {0}".format(plaintext))

    output.append("CIPHERTEXT = {0}".format(encrypt(mode, key, iv, plaintext)))
    return "\n".join(output)


def write_file(data, filename):
    with open(filename, "w") as f:
        f.write(data)


CBC_PATH = "tests/hazmat/primitives/vectors/ciphers/AES/CBC/CBCMMT128.rsp"
write_file(build_vectors(modes.CBC, CBC_PATH), "idea-cbc.txt")
OFB_PATH = "tests/hazmat/primitives/vectors/ciphers/AES/OFB/OFBMMT128.rsp"
write_file(build_vectors(modes.OFB, OFB_PATH), "idea-ofb.txt")
CFB_PATH = "tests/hazmat/primitives/vectors/ciphers/AES/CFB/CFB128MMT128.rsp"
write_file(build_vectors(modes.CFB, CFB_PATH), "idea-cfb.txt")
"""

# SIMON
# https://github.com/inmcm/Simon_Speck_Ciphers/tree/master/Python/simonspeckciphers

from simon import SimonCipher
sc_enc = []
sc_dec = []
data = 0xCCCCAAAA555533332344325432524357

def simon_cipher(data):
    start_time = datetime.now()
    key = 0x525354
    simon_iv = 0x999999
    my_simon = SimonCipher(key, mode='CBC', init=simon_iv)
    my_plaintext = data
    simon_ciphertext = my_simon.encrypt(my_plaintext)
    end_time = datetime.now()
    sc_enc.append(end_time-start_time)

    start_time = datetime.now()
    my_simon = SimonCipher(key, mode='CBC', init=simon_iv)
    simon_plaintext = my_simon.decrypt(simon_ciphertext)
    #print(simon_plaintext)
    end_time = datetime.now()
    sc_dec.append(end_time-start_time)


def main():
    for i in range(20):
        data = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(32)]).encode('utf-8')
        aes_scheme(data)
        triple_des_scheme(data)

main()
print(aes_dec[0])
"""
# THREEFISH - 1024
from skein import threefish
import geesefly
geesefly.Threefish512
t = threefish(b'key of 32,64 or 128 bytes length', b'tweak: 16 bytes ')
c = t.encrypt_block(b'block of data,same length as key')
t.decrypt_block(c)
"""

