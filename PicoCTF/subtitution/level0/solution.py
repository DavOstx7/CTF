MESSAGE_PATH = "./message.txt" 

def get_encrypted_flag() -> str:
	with open(MESSAGE_PATH, 'r') as r_file:
		return r_file.readlines()[-1].split(":")[1].strip()

def get_encryption_key() -> str:
	with open(MESSAGE_PATH, 'r') as r_file:
		return r_file.readlines()[0].strip()

def main():
	encryption_key = get_encryption_key()
	encrypted_flag = get_encrypted_flag()
	print(encryption_key)
	print(encrypted_flag)


if __name__ == "__main__":
	main()