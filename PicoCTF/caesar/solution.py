from string import ascii_lowercase, ascii_uppercase


cipher_path = "./ciphertext"

with open(cipher_path, "r") as f:
	cipher_message = f.read()

def rot_decryptor(cipher_message: str, rot_number: int) -> str:
	og_message = ""
	for char in cipher_message:
		if char in ascii_lowercase:
			og_message += ascii_lowercase[(ascii_lowercase.index(char) - rot_number) % len(ascii_lowercase)]
		elif char in ascii_uppercase:
			og_message += ascii_uppercase[(ascii_uppercase.index(char) - rot_number) % len(ascii_uppercase)]
		else:
			og_message += char
	return og_message


curly_bracket_index = cipher_message.index('{')
inside_curly_brackets =  cipher_message[curly_bracket_index + 1:-1]
print('-' * 50)
for i in range(25):
	decrypted_inside_brackets = rot_decryptor(inside_curly_brackets, i)
	print("[+] picoCTF{" + decrypted_inside_brackets + '}')
print('-' * 50)