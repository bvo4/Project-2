import sys

#https://www.geeksforgeeks.org/decision-tree-implementation-python/
from skein import threefish

def _tf_encrypt(key, iv, data):
	# adso always uses JSON, so we pad the message with JSON whitespace.
	while len(data) % 64 != 0:
		data += b' '
	cipher = skein.threefish(derive_key(key, iv, 1024), _tf_tweak_ctr(0))
	output = b''
	for k in range(0, len(data), 64):
		cipher.tweak = _tf_tweak_ctr(k) 
		output += cipher.encrypt_block(data[k : k + 64])
	return output
    


if __name__ == "__main__":
    key = 'B&E(H+MbQeThWmZq4t7w!z%C*F-JaNcRfUjXn2r5u8x/A?D(G+KbPeSgVkYp3s6v9y$B&E)H@McQfTjWmZq4t7w!z%C*F-JaNdRgUkXp2r5u8x/A?D(G+KbPeShVmYq'

    _tf_encrypt(key, 4, b'ffhfdfdjfjkfhjhfjadhjfkjkfldahjfdahkfhajfkd')
