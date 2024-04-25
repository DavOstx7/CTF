import hashlib

POSSIBLE_PASSWORDS_PATH = "./dictionary.txt"

correct_pw_hash = open('level5.hash.bin', 'rb').read()


def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()


if __name__ == "__main__":
	with open(POSSIBLE_PASSWORDS_PATH) as f:
		for possible_password in f:

			possible_password_hash = hash_pw(possible_password.strip())
			if possible_password_hash == correct_pw_hash:
				print("The correct password is: ", possible_password)
				break