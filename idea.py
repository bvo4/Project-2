import random, unittest
from typing import Callable, List, Tuple
import cryptocommon

#https://www.nayuki.io/page/cryptographic-primitives-in-plain-python

class CipherTest(unittest.TestCase):
	def test_idea_cipher(self) -> None:
		import ideacipher
		self._check_invertibility(ideacipher.encrypt, ideacipher.decrypt, 8, 16)
		self._check_cipher(ideacipher.encrypt, ideacipher.decrypt, [
			("0000000100020003", "00010002000300040005000600070008", "11FBED2B01986DE5"),
			("DB2D4A92AA68273F", "000102030405060708090A0B0C0D0E0F", "0011223344556677"),
			("F129A6601EF62A47", "2BD6459F82C5B300952C49104881FF48", "EA024714AD5C4D84"),
		])
    	# Private utilities
	
	def _check_cipher(self,
			encfunc: Callable[[bytes,bytes],bytes],
			decfunc: Callable[[bytes,bytes],bytes],
			cases: List[Tuple[str,str,str]]) -> None:
		
		global num_test_cases
		
		for (plaintext_hex, key_hex, expectciphertext_hex) in cases:
			key_bin: bytes = bytes.fromhex(key_hex)
			plaintext_bin: bytes = bytes.fromhex(plaintext_hex)
			actualciphertext_bin: bytes = encfunc(plaintext_bin, key_bin)
			expectciphertext_bin: bytes = bytes.fromhex(expectciphertext_hex)
			decrypted_bin: bytes = decfunc(actualciphertext_bin, key_bin)
			
			self.assertEqual(actualciphertext_bin, expectciphertext_bin)
			self.assertEqual(decrypted_bin, plaintext_bin)
			num_test_cases += 1
	
	
	def _check_invertibility(self,
			encfunc: Callable[[bytes,bytes],bytes],
			decfunc: Callable[[bytes,bytes],bytes],
			blocklen: int, keylen: int) -> None:
		
		global num_test_cases
		TRIALS = 300
		for _ in range(TRIALS):
			key = bytes(random.randrange(256) for _ in range(keylen))
			message = bytes(random.randrange(256) for _ in range(blocklen))
			encrypted: bytes = encfunc(message, key)
			decrypted: bytes = decfunc(encrypted, key)
			self.assertEqual(decrypted, message)
			num_test_cases += 1

if __name__ == "__main__":
	num_test_cases: int = 9
	unittest.main(exit=False)
	print(f"Tested {num_test_cases} vectors")