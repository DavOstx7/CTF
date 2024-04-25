from string import ascii_lowercase, ascii_uppercase


ENCRYPTED_FLAG = "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"

def rot13(message: str) -> str:
	cipher = ""
	for char in message:
		if char in ascii_lowercase:
			cipher += ascii_lowercase[(ascii_lowercase.index(char) + 13) % len(ascii_lowercase)]
		elif char in ascii_uppercase:
			cipher += ascii_uppercase[(ascii_uppercase.index(char) + 13) % len(ascii_uppercase)]
		else:
			cipher += char

	return cipher

print(f"The decrypted flag is: {rot13(ENCRYPTED_FLAG)}")
