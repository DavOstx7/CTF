import string
import itertools

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	return enc

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

ciphertext = "ioffdcjbfjmcifelcaloifgcjecgpgiebpfeiafhgajafkmlfcbpfbioflgcmacg"
flagX = "abcdef0123456789"
keyX = "abcdefghijklmnop"




'''
flag = "10f3dbf"
assert all([c in "abcdef0123456789" for c in flag])

key = "phal"
assert all([k in ALPHABET for k in key]) and len(key) < 15

b16 = b16_encode(flag)
enc = ""
for i, c in enumerate(b16):
	print(c)
	enc += shift(c, key[i % len(key)])
print(enc)
'''
d = {}
for char in flagX:
	x = b16_encode(char)
	for option in itertools.permutations(keyX, 2):
		m = ""
		k = "".join([c for c in option])
		m+= shift(x[0], k[0])
		m+= shift(x[1], k[1])
		if(m not in d):
			d[m] = [k]
		else:
			d[m].append(k)

#print(d)

def find_row(analyze, x):
	saveR = []
	r = 0
	for arr in analyze:
		for value in arr:
			if(value == x):
				saveR.append(r)
				break
		r+=1
	return saveR

s = {}
analyze = []
for i in range(0, len(ciphertext), 2):
	duo = ciphertext[i] + ciphertext[i+1]
	x = d[duo]
	s[duo] = x
	analyze.append(x)

done = []
good = []
for arr in analyze:

	for value in arr:
		if(value in done):
			continue
		done.append(value)
		times = find_row(analyze, value)
		if(len(times) < 3):
			continue

		diff = times[1] - times[0]
		test = True
		for i in range(2, len(times)):
			if(times[i] - times[i-1] != diff):
				test = False
				break
		if(test == True):
			good.append((value, times[0], diff, len(times))) #key, first appearence, jumps, amount

# print(good)
# [('fk', 0, 9, 4), ('fj', 0, 9, 4), ('fi', 0, 9, 4), ('ap', 2, 9, 4), ('ao', 2, 9, 4), ('an', 2, 9, 4), ('am', 2, 9, 4), ('gl', 3, 9, 4), ('jc', 5, 9, 3), ('ok', 7, 9, 3), ('oj', 7, 9, 3), ('oi', 7, 9, 3), ('oh', 7, 9, 3), ('og', 7, 9, 3), ('dj', 11, 9, 3)]


# ~~~~~~~~~THIS IS WRONG~~~~~~~~~~ #
# Now we know the key length is probably 9
# We know that the firs two lettes are either fk, fj, or fi. we know that the next are either ap, ao, an, am or maybe even dj.
# Then we don't know the next three ones (we should randomize), and then we know the last two which are ok, oj, oi, oh, og
'''
zero_one = ["fk", "fj", "fi", "dj"]
two_three = ["ap", "ao", "an", "am"]
four_six = []
seven_eight = ["ok", "oj", "oi", "oh", "og"]

for option in itertools.product(keyX, repeat = 3):
	x = "".join([c for c in option])
	four_six.append(x)

add = [two_three, four_six, seven_eight]
KEYS = zero_one

for arr in add:
	n = []
	for KEY in KEYS:
		for value in arr:
			n.append(KEY+value)
	KEYS = n
'''

# ~~~~~~~~~~~~~~~~~ NOT WORKING ~~~~~~~~~~~~~ #
KEYS = [""]
for i in range(4):
	n = []
	arr = analyze[i]
	for key in KEYS:
		for value in arr:
			n.append(key + value)
	KEYS = n
n = []
for key in KEYS:
	for value in keyX:
		n.append(key + value)
KEYS = n
print(KEYS)

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

def unshift(value, k): #no use
	x = ALPHABET.index(value) # = (t1 + t2) % len(ALPHABET)
	t2 = ord(k) - LOWERCASE_OFFSET
	t1 = x - t2
	if(t1 < 0):
		t1+=16
	return chr(t1 + LOWERCASE_OFFSET)

def decrypt(key, z):
	dec = ""
	for i, c in enumerate(ciphertext):
		dec += unshift(c, key[i % len(key)])
	flag = b16_decode(dec)

	valid = True
	for c in flag:
		if(c not in flagX):
			valid = False
			break
	if(valid):
		print(key + flag)
		z.append(key, flag)
               

z = []
for key in KEYS:
	#print("[+] trying key " + key)
	decrypt(key, z)
print(z)
