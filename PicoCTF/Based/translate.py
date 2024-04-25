from pwn import *


def IsLetter(num):
	l = "abcdef"
	for letter in l:
		if(letter in num):
			return True
	return False

r = remote('jupiter.challenges.picoctf.org',  29221)
while True:
	try:
		x = r.recvuntil(b'the')
		#print("[*] " + x.decode('utf-8'))
		value = r.recvuntil(b'as', drop = True).decode('utf-8').strip()
		value = value.split(" ")
		print("[-] value list is " +  str(value))
		highest = -1
		base = ""
		x = r.recvuntil(b"Input:")
		#print("[*] " + x.decode('utf-8'))
		crashed = False
	except:
		crashed = True

	if(crashed == True):
		flag = r.recv()
		print("[+] " + flag.decode('utf-8'))
		r.close()
		break
	for num in value:
		if(num == " " or num == "  "):
			continue
		if(IsLetter(num)):
			highest = 15
			break
		for digit in num:
			d = int(digit)
			if(d > highest):
				highest = d
	if(highest < 2):
		base = 2
	elif(highest < 8):
		base = 8
	elif(highest >= 8 and highest <= 9):
		base = 10
	elif(highest == 15):
		base = 16
	print("[-] base is: " + str(base))
	if(base == 16): #I did this because it told me the value I tried to convert to int was too big
		bytes_object = bytes.fromhex("".join([hexa for hexa in value]))
		word = bytes_object.decode("ASCII")
	else:
		word = "".join([chr(int(num, base)) for num in value])
	print("[-] word is: " + word)
	r.sendline(word.encode('utf-8'))
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
	

