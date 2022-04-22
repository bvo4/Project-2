from skein import threefish

t = threefish(b'key of 32,64 or 128 bytes length', b'tweak: 16 bytes ')
(32, 256)
 c= t.encrypt_block(b'block of data,same length as key')
print (t.decrypt_block(c))
print('block of data,same length as key')
