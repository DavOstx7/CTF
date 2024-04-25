import string

MAPPER = string.ascii_uppercase + string.digits + "_"
MOD = 37
FLAG_PATH = "./message.txt"

def get_encrypted_message(path: str) -> str:
	with open(path, "r") as file_handler:
		return file_handler.read()

def decrypt_encrypted_message(ciphertext: str) -> str:
	message = ""
	encrypted_characters = ciphertext.split()
	for encrypted_char in encrypted_characters:
		numeric_value = int(encrypted_char)
		message += MAPPER[numeric_value % MOD]
	return message

encrypted_message = get_encrypted_message(FLAG_PATH)
decrypted_message = decrypt_encrypted_message(encrypted_message)
print(f"The flag is: picoCTF{{{decrypted_message}}}")
