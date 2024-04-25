#!/usr/bin/env python3
from binascii import hexlify, unhexlify
from random import randint
import string
import itertools
from pwn import xor

#with open('flag.txt', 'rb') as f:
#    flag = f.read()

#with open('secret-key.txt', 'rb') as f:
#    key = f.read()

def encrypt(ptxt, key): #this function xor's every Nth byte of ptxt with every Nth byte of key (when key ends it starts from the start of key again)
    ctxt = b''
    #print(type(ptxt[1]))
    for i in range(len(ptxt)):
        a = ptxt[i] # a = ord(char)
        b = key[i % len(key)]
     #   print(f'{a} | {b}')
     #   print(f'{type(a)} {type(b)}')
     #   print(bytes([a ^ b]))
        ctxt += bytes([a ^ b]) # ^ = xor
    return ctxt

'''
x = (encrypt(b'hearme', b'1'))
print(hexlify(x))
x = encrypt(x, b'1')
print(hexlify(x))
x = encrypt(x, b'1')
print(hexlify(x))
x = encrypt(x, b'1')
print(hexlify(x))

after running this check, I found out that x returns to it's original state, since the ciphertext isn't a flag after we turn it to ascii, 
it means the flag didn't reverse to it's original state, and it's like we just used encrypt once. so we need to use recursion
'''	

#MY stupid ass forgot about the secret key at the start, thats why this script didn't work smh.
'''
def decrypt(ciphertext, t): 

	if(len(t) == 0):
		if(b"pico" in ciphertext):
			print("~~~~~~~~~~~\n~~~~~~~~~~~\n~~~~~~~~~~~\nFOUND IT\n~~~~~~~~~~~\n~~~~~~~~~~~\n~~~~~~~~~~~")
			print(ciphertext.decode('utf-8'))
		return

	c1 = ciphertext
	c2 = encrypt(ciphertext, t[0])
	decrypt(c1, t[1:])
	decrypt(c2, t[1:])
'''
def decrypt(ciphertext, t, store_keys): 

	if(len(t) == 0):
		#now we need to check if we can get the key.
		flag_start = b"picoCTF{" #start of flag
		c_start = ciphertext[:len(flag_start)] #start of ciphertext
		key_start = encrypt(flag_start, c_start) #start of key
		key_start = key_start.decode()
		if(key_start.isprintable() == True):
			#print("~~~~~~~~~~~~~~~~~~~~~~\n~~~~~~~~~~~\nFOUND POSSIBLE START OF KEY\n~~~~~~~~~~~\n~~~~~~~~~~~~~~~~~~~~~~")
			#print(key_start)
			store_keys[key_start] = ciphertext
		return

	c1 = ciphertext
	c2 = encrypt(ciphertext, t[0])
	decrypt(c1, t[1:], store_keys)
	decrypt(c2, t[1:], store_keys)


c = "57657535570c1e1c612b3468106a18492140662d2f5967442a2960684d28017931617b1f3637"
ciphertext = unhexlify(c)
t = (b'break it',b'ever',b'and you will never',b'is absolutely impenetrable',b'my encryption method')
store_keys = {}
decrypt(ciphertext, t, store_keys)
#print(store_keys.keys())
#result = ['Fbrzm7-G', "Bhr~a'0R", 'Nm7mf":L', "Jg7ij2'Y", 'Ii7~ht6J', 'Mc7zdd+_', 'Africa!A', 'Elrmoq<T']
#The best key is 'Africa!A', and we can see that it actually looped again to A, meaning that it's probably only 'Africa!' (it xor '{' with 'A' because it reached the end of the key)

key = 'Africa!A'
ciphertext = store_keys[key]
key = key[:-1].encode('utf-8')
flag = encrypt(ciphertext, key)
flag = flag.decode('utf-8')
print(flag)














def main():
	#ctxt = encrypt(flag, key)

	random_strs = [
	    b'my encryption method',
	    b'is absolutely impenetrable',
	    b'and you will never',
	    b'ever',
	    b'ever',
	    b'ever',
	    b'ever',
	    b'ever',
	    b'ever',
	    b'break it'
	]

	for random_str in random_strs:
	    for i in range(randint(0, pow(2, 8))):
	        for j in range(randint(0, pow(2, 6))):
	            for k in range(randint(0, pow(2, 4))):
	                for l in range(randint(0, pow(2, 2))): #4
	                    for m in range(randint(0, pow(2, 0))): #always one time	                 
	                        ctxt = encrypt(ctxt, random_str)

	#with open('output.txt', 'w') as f:
	#    f.write(ctxt.hex())

#main()