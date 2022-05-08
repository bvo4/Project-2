
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
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# AES
aes_enc = []
aes_dec = []

def aes_scheme(data):
    start_time = datetime.now()

    key = get_random_bytes(16)
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


# IDEA CBC
# Block is 8 bytes, key is 16 byte
import ideacipher as ic
ic_enc = []
ic_dec = []
ic_key = bytes.fromhex("00010002000300040005000600070008")
ic_plain = ["0000000100020003", "11FBED2B01986DE5", "F129A6601EF62A47", "1234567890123456", "F129A14B1EF6FA47"
                "ABCD2EF123ADECBA", "AB3455DCFAB32432", "FADECA123DA890AC", "AABBCCDDEEFF1122", "2288080ADCEA8221"]

def idea_cipher(data, key):
    for i in data:
        start_time = datetime.now()
        cipher_text = ic.encrypt(bytes.fromhex("0000000100020003"), key)
        end_time = datetime.now()
        ic_enc.append(end_time-start_time)

        start_time = datetime.now()
        ic.decrypt(cipher_text, key)
        end_time = datetime.now()
        ic_dec.append(end_time-start_time)

# SIMON
# https://github.com/inmcm/Simon_Speck_Ciphers/tree/master/Python/simonspeckciphers

from simon import SimonCipher
sc_enc = []
sc_dec = []
simon_data = [0xCCCCAAAA555533332344325432524357, 0xBCDABDAA5555363323443D54325A4357, 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
       ,0x384956AB889C896F5213D54A567B012C, 0xADC748927890DD64324AC78989EF89FF, 0xAAAAAAAAAAAA9999999333333DDDEEEA
       ,0x3232789F5456757AD5679CDAAAD55A42, 0xDDDDDADADADADADCDCDFFEACFABFBAFE, 0x9435728975904237543AADD890CDAAB8
       ,0x23748907908789798FACBBADEBFDEA39]

def simon_cipher(plains):
    for data in plains:
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
    for i in range(10):
        data = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(32)]).encode('utf-8')
        aes_scheme(data)
        triple_des_scheme(data)
    idea_cipher(ic_plain, ic_key)
    simon_cipher(simon_data)

def average(lst):
    total = lst[0]
    for i in range(1, len(lst)):
        total += lst[i]
    ans = total/len(lst)
    return round(ans.total_seconds()*1000, 4)

def find_all():
    averages = []
    averages.append(average(aes_enc))
    averages.append(average(aes_dec))
    averages.append(average(t_des_enc))
    averages.append(average(t_des_dec))
    averages.append(average(ic_enc))
    averages.append(average(ic_dec))
    averages.append(average(sc_enc))
    averages.append(average(sc_dec))
    return averages

main()
labels = ["AES Encrypt", "AES Decrypt", "Triple DES Encrypt", "Triple DES Decrypt", "IDEA Encrypt", "IDEA Decrypt","Simon Encrypt","Simon Decrypt"]
plt.ylabel("Average operation in Microseconds")
plt.xlabel("Block Cipher")
plt.title("Average Encryption and Decryption Time for Block Cipher Schemes")
plt.bar(labels, find_all(), color=['green', 'green', 'blue', 'blue', 'red', 'red', 'orange', 'orange'])#, 'pink', 'pink'])
plt.yticks([0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4])
plt.show()




"""
# THREEFISH - 1024
import skein
import geesefly
geesefly.Threefish512
t = skein.threefish(b'key of 32,64 or 128 bytes length', b'tweak: 16 bytes ')
c = t.encrypt_block(b'block of data,same length as key')
t.decrypt_block(c)
"""
