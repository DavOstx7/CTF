import pwn
import re
import hashlib

HOST, PORT = "saturn.picoctf.net", 63116
ANSWER_IDENTIFIER = b"Answer:"
QUESTIONS_COUNT = 3

def seperator() -> str:
	return ('-' * 50 + '\n') * 2

def get_connection(host: str, port: int) -> pwn.tubes.remote.remote:
	return pwn.remote(HOST, PORT)

def get_hashed_string(conn: pwn.tubes.remote.remote) -> str:
	full_question = conn.recvuntil(ANSWER_IDENTIFIER).decode()
	print(f"[*]The received question is:\n{full_question}")
	[string_to_hash] = re.findall(".*'(.*?)'.*", full_question)
	print(f"[*] Extracted: {string_to_hash}")
	hashed_string = hashlib.md5(string_to_hash.encode()).hexdigest()
	return hashed_string

def submit_hashed_string(conn: pwn.tubes.remote.remote, answer: str):
	print(f"[+] Sending answer: {answer}")
	conn.sendline(answer.encode())

def get_flag(conn: pwn.tubes.remote.remote) -> str:
	a = conn.recvuntil(b"Correct.\r\n")
	flag = conn.recvline().decode()
	return flag

if __name__ == "__main__":
	connection = get_connection(HOST, PORT)
	print(seperator())
	for _ in range(QUESTIONS_COUNT):
		hashed_string = get_hashed_string(connection)
		submit_hashed_string(connection, hashed_string)
	print(seperator())
	flag = get_flag(connection)
	print(flag)


