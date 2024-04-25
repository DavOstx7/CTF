#!/usr/bin/env python3
import hashlib

import string
import random

def id_generator(size):
	chars=string.ascii_uppercase + string.digits
	return ''.join(random.choice(chars) for _ in range(size))

string1=""
string2=""

size=1
counter = 0
while (not(string1 != "" and string2 != "")):
	if(size>=30):
		size = 1
	if(counter>=1000):
		size+=1
		counter=0
	rnd = id_generator(size)
	result = hashlib.md5(rnd.encode('utf-8')).hexdigest()
	if(result[0] == '0' and result[1] == 'e'):
		if(string1 == ""):
			string1 = rnd 
		else:
			string2 = rnd 

	counter+=1

if(string1 == "" and string2 == ""):
	print("couldn't find any strings that give 0e collision hashes")
else:
	print(f'string1 = {string1} | string2 = {string2}')
