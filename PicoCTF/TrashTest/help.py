from pwn import *
context.log_level = 'error'
host, port = "jupiter.challenges.picoctf.org", 42953
for i in range(101):
	r = remote(host, port)
	r.recvuntil("guess?\n")
	r.sendline(str(i))
	response = r.recvline().strip().decode()
	print(f'{i} - {response}')

#the solution is 84.


