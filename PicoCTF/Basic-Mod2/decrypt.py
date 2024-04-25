import string

FLAG_PATH = "./message.txt"
MOD = 41
MAPPER = " " + string.ascii_uppercase + string.digits + "_"

def get_encrypted_message(path: str) -> str:
	with open(path, "r") as file_handler:
		return file_handler.read()

def decrypt_encrypted_message(ciphertext: str) -> str:
	message = ""
	encrypted_characters = ciphertext.split()
	for encrypted_char in encrypted_characters:
		numeric_value = int(encrypted_char)
		message += MAPPER[pow(numeric_value, -1, MOD)]
	return message

encrypted_message = get_encrypted_message(FLAG_PATH)
decrypted_message = decrypt_encrypted_message(encrypted_message)
print(f"The flag is: picoCTF{{{decrypted_message}}}")
