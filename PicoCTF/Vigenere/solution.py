from string import ascii_lowercase, ascii_uppercase

ASCII_LETTERS_COUNT = 26
CIPHER_MESSAGE_PATH = "./cipher.txt"
ENCRYPTION_KEY = "CYLAB"

def get_cipher_message() -> str:
	with open(CIPHER_MESSAGE_PATH, 'r') as ro_file_handler:
		return ro_file_handler.read().strip()


def decrypt(cipher_message: str) -> str:
	message = ""
	encryption_index = 0
	for cipher_char in cipher_message:
		encryption_char = ENCRYPTION_KEY[encryption_index % len(ENCRYPTION_KEY)]
		if cipher_char in ascii_lowercase:
			encryption_index+=1
			decrypted_char = ascii_lowercase[(ascii_lowercase.index(cipher_char) - ascii_uppercase.index(encryption_char)) % ASCII_LETTERS_COUNT]
		elif cipher_char in ascii_uppercase:
			decrypted_char = ascii_uppercase[(ascii_uppercase.index(cipher_char) - ascii_uppercase.index(encryption_char)) % ASCII_LETTERS_COUNT]
			encryption_index+=1
		else:
			decrypted_char = cipher_char
		message += decrypted_char
	return message

def main():
	cipher_message = get_cipher_message()
	print(f"[*] cipher: '{cipher_message}'")
	flag = decrypt(cipher_message)
	print(f"[*] flag: '{flag}'")

if __name__ == "__main__":
	main()
	print(f"{ascii_lowercase.index('i')} + {ascii_uppercase.index('Y')} {ascii_lowercase.index('g')}")