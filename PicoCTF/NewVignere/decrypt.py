ciphertext = 'ioffdcjbfjmcifelcaloifgcjecgpgiebpfeiafhgajafkmlfcbpfbioflgcmacg'
flagX = "abcdef0123456789"
keyX = "abcdefghijklmnop"

import string
from itertools import product, permutations

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16] #first 16 alphabet letters

def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	return enc

def b16_decode(ciphertext):
	s=""
	for i in range(0, len(ciphertext), 2):
		f1 = ciphertext[i] # = ALPHABET[int(binary[:4], 2)]
		f2 = ciphertext[i+1] # = ALPHABET[int(binary[4:], 2)]
		i1 = ALPHABET.index(f1) # = int(binary[:4], 2
		i2 = ALPHABET.index(f2) # = int(binary[4:], 2)
		b1 = "{0:04b}".format(i1) # = binary[:4]
		b2 = "{0:04b}".format(i2) # = binary[4:]
		binary = b1 + b2 # = "{0:08b}".format(ord(c))
		x = int(binary, 2) # = ord(c)
		s += chr(x) # = c
	return s

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]


def unshiftbrute(value): #no use
	x = ALPHABET.index(value) # = (t1 + t2) % len(ALPHABET)
	options = keyX
	for k in options:
		t2 = ord(k) - LOWERCASE_OFFSET
		t1 = x - t2
		if(y < 0):
			t1+=16
		result.append(chr(t1 + LOWERCASE_OFFSET))
	return result

def unshift(value, k): #no use
	x = ALPHABET.index(value) # = (t1 + t2) % len(ALPHABET)
	t2 = ord(k) - LOWERCASE_OFFSET
	t1 = x - t2
	if(t1 < 0):
		t1+=16
	return chr(t1 + LOWERCASE_OFFSET)

def analasys():
	d = {}
	counter = 2
	Found = True
	while Found:
		Found = False
		for i in range(0, len(ciphertext) - (counter-1), 1):
			x1 = ""
			for k in range(counter):
				x1+=ciphertext[i+k]
			for j in range(0, len(ciphertext) - (counter-1), 1):
				if(i == j):
					continue
				x2 = ""
				for k in range(counter):
					x2+=ciphertext[j+k]
				if(x1 == x2):
					Found = True
					if(counter in d):
						if((x1, abs(j - i) - 1) in d[counter]):
							continue
						d[counter].append((x1, abs(j - i) - 1))
					else:
						d[counter] = [(x1, abs(j - i) - 1)]
		counter+=1
	final = []
	for x in d:
		arr = d[x]
		for seq, distance in arr:
			if(distance < 15):
				print(f'sequence length = {x} | sequence = {seq} | distance = {distance}')
				final.append(distance)
	return final

def segments(values):
	x = []
	for _, value in values:
		for i in range(4, value // 2):
			if(value % i == 0):
				x.append(i)
		x.append(value)
	result = []
	for value in x:
		if(x.count(value) > 1 and value not in result):
			result.append(value)
	return result

def trying():
	d = analasys() # This array contains the length of the key
	print(d)
	valid = []
	for key_length in d:
		for key in product(keyX, repeat = key_length):
			key = "".join([c for c in key])
			print("trying key: " + key)
			dec = ""
			for i, c in enumerate(ciphertext):
				dec += unshift(c, key[i % len(key)])
			flag = b16_decode(dec)
			is_valid = True
			for c in flag:
				if (c not in flagX):
					is_valid = False
					break
			if(is_valid):
				print(f'key = {key} ---> flag = {flag}')
				valid.append(flag)
		

# I just realized that the maximum key length 14


'''
flag = "abd"
assert all([c in flagX for c in flag])

key = "afdd"
assert all([k in keyX for k in key]) and len(key) < 15

b16 = b16_encode(flag)
enc = ""

for i, c in enumerate(b16):
	#print(f'i = {i} | c = {c} | key[i % len(key)] = {key[i % len(key)]} | shift(c, key[i % len(key)]) = {shift(c, key[i % len(key)])}')
	enc += shift(c, key[i % len(key)])
#print(enc)
'''
analasys()
def solution(key, index, flag, max_key, z):
	if(index + 1 > len(ciphertext) -1 or len(key) == max_key):
		print(f'key = {key} ---> flag = {flag}')
		z.append(key)
		return
		
	duo = ciphertext[index] + ciphertext[index + 1]
	d = duo
	save = []
	print(duo)
	for x in product(keyX, repeat = 2):
		k = "".join([c for c in x])
		#print("trying k value of: " + k)
		m = ""
		m+=unshift(d[0], k[0])
		m+=unshift(d[1], k[1])
		duo = m
		single = b16_decode(duo)

		if(single in flagX):
			save.append((key + k, index + 2, flag+single))
	if(len(save) == 0):
		print("couldn't decrypt the value of: " + d)

	for k, i, f in save:
		solution(k, i, f, max_key, z)

def try_solve():
	valid = []
	for max_key_length in range(2, 10, 2):
		print("~~~~~~~~~~~~~~~~~~~~~~max_key_length = " + str(max_key_length) + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		z = []
		solution("", 0, "", max_key_length, z)
		print(z)
		n = [] #because we cant calcualte for odd numbers, we just try every possibility of odd numbers
		for key in z:
			n.append(key)
			for k in keyX:
				n.append(key + k)
		z = n
		print(z)
		for key in z:
			print("trying key: " + key)
			dec = ""
			for i, c in enumerate(ciphertext):
				dec += unshift(c, key[i % len(key)])
			flag = b16_decode(dec)
			is_valid = True
			for c in flag:
				if (c not in flagX):
					is_valid = False
					break
			if(is_valid):
				print(f'key = {key} ---> flag = {flag}')
				valid.append(flag)
				break
	print(valid)



keyY = []
for c in keyX:
	keyY.append(b16_encode(c))
for option in permutations(keyY, 1):
	y = "".join([c for c in option])
	print(ciphertext.count(y))
