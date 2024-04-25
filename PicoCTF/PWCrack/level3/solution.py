import hashlib

POSSIBLE_PASSWORDS = ["f09e", "4dcf", "87ab", "dba8", "752e", "3961", "f159"]
correct_pw_hash = open('level3.hash.bin', 'rb').read()


def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()


if __name__ == "__main__":
	for possible_password in POSSIBLE_PASSWORDS:
		possible_password_hash = hash_pw(possible_password)
		if possible_password_hash == correct_pw_hash:
			print("The correct password is: ", possible_password)
			break