from pwn import *
import string
chars = string.ascii_lowercase + "CTF" + "{}_0123456789" #I know the answer already, so this makes it run faster


#EXPLANATION:
'''
Basically, if we give the program a, it will give us 1
If we give it  ab, it will give us 12 or 21
If we give it b, it will give us 3
If we give it ba, it will give us 34 or 43
so what we need to do is loop through all the letters, and remove all of the previous ones that we already know to be true.
For example, if 12 is the flag.
we would first encrypt a which is 1, and see  that it's in 12.
then we could encrypt aa which is 31 or 13, we would remove 1 (a) and see that 3 is not in 12.
then we would encrypt ab which is  21 or 12, we would remove 1 (a) and see that 2 is in 12.
and so on.
so for the start we nee to encrypt one letter, see if it's in the flag,
when we do find one, we add it to our current flag, and store it's encryption value in a list.
then we make a test flag which is the current flag + char, and then remove from it's encryption value every value which is in the list, and check if what's left is in the flag.
if yes we add the value to the list, and add the char to the flag.
we do this untill we reach "}"
'''
r = remote('mercury.picoctf.net', 6276)

flag = r.recvline().decode('utf-8').strip()

chunks = []
r.recvuntil(b'e: 65537\n') #get rid of all of the start
known_flag = b''

while b"}" not in known_flag:	
	r.recvuntil('I will encrypt whatever you give me:') #get rid of all of the info it gives at the start
	found = False
	try:
		for char in chars:
			test_flag=known_flag + char.encode('utf-8')
			print(test_flag)

			r.sendline(test_flag)
			r.recvuntil(b"Here you go: ")

			result = r.recvline().decode().strip()

			for chunk in chunks:
				result = result.replace(chunk, '')

			if(result in flag):
				known_flag=test_flag
				chunks.append(result)
				print(known_flag.decode('utf-8'))
				found = True
				break

		if(found == False):
			print("Something isn't right...")
			break
	except:
		r = remote('mercury.picoctf.net', 6276)

print("the flag is: " + known_flag.decode('utf-8'))

