lowercase_letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
uppercase_letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
digits = [i for i in range(10)]

USERSNAMES_PATH = "leak/usernames.txt"
PASSWORDS_PATH = "leak/passwords.txt"

TARGET_USER = "cultiris"

class UserNotExists(Exception):
	pass

def get_lines_in_file(path: str) -> list:
	with open(path) as file_handler:
		return [line.strip() for line in file_handler.readlines()]

def get_username_and_password_for_user(user: str) -> tuple:
	usernames = get_lines_in_file(USERSNAMES_PATH)
	passwords = get_lines_in_file(PASSWORDS_PATH)
	for username, password in zip(usernames, passwords):
		if username == user:
			return username, password

	raise UserNotExists(f"The user '{user} does not exist")

def ceaser_cipher(string: str, shift_index: int) -> str:
	shifted_string = ""
	for char in string:
		if char in lowercase_letters:
			shifted_string += lowercase_letters[(lowercase_letters.index(char) + shift_index) % len(lowercase_letters)]
		elif char in uppercase_letters:
			shifted_string += uppercase_letters[(uppercase_letters.index(char) + shift_index) % len(uppercase_letters)]
		else:
			shifted_string += char
	return shifted_string

def get_decrypted_ceaser(encrypted_ceaser: str, target_text: str) -> str:
	for i in range(26):
		decrypted_ceaser = ceaser_cipher(encrypted_ceaser, i)
		if target_text in decrypted_ceaser:
			return decrypted_ceaser
	return None

if __name__ == "__main__":
	username, password = get_username_and_password_for_user(TARGET_USER)
	flag = get_decrypted_ceaser(password, "picoCTF")
	print(flag)
	# Another option
	possible_flags = [ceaser_cipher(password, i) for i in range(26)]
	[correct_flag] = filter(lambda flag: "picoCTF" in flag, possible_flags)
	print(correct_flag)
