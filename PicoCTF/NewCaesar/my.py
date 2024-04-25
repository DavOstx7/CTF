import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

encflag = "ihjghbjgjhfbhbfcfjflfjiifdfgffihfeigidfligigffihfjfhfhfhigfjfffjfeihihfdieieih"

def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	return enc

def b16_decode(encrypted):
	dec = ""
	for i in range(0, len(encrypted), 2):
		index1 = ALPHABET.index(encrypted[i]) #this is equal to int(binary[:4], 2)
		index2 = ALPHABET.index(encrypted[i+1]) #this is equal to int(binary[4:], 2)
		bin1 = "{0:04b}".format(index1) #this equals to binary[:4]
		bin2 = "{0:04b}".format(index2) #this equals to binary[4:]
		binary = bin1 + bin2 #this equals to binary
		ordchar = int(binary, 2) #this is equal to ord(c)
		char = chr(ordchar) #this is equal to c
		dec+=char
	return dec #this is equal to plain

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

def unshift(x, k):
	index = ALPHABET.index(x) #this is equal to (t1 + t2) % len(ALPHABET)

	t2 = ord(k) - LOWERCASE_OFFSET #t2 = t2
	t1 = index - t2 #
	if(t1 < 0):
		t1+=len(ALPHABET)
	# t1 is now equal to ord(c) - LOWERCASE_OFFSET
	ordc = t1 + LOWERCASE_OFFSET
	c = chr(ordc)
	return c



def main():
	flag = "..."
	key = "..."
	assert all([k in ALPHABET for k in key])
	assert len(key) == 1

	b16 = b16_encode(flag)
	enc = ""
	for i, c in enumerate(b16):
		enc += shift(c, key[i % len(key)]) #key[i % len(key)] = key[number % 1] = key[0] = key (because key is only one char)
	print(enc)


def unmain(encflag):
	# There are 16 possiblites for what the key could be
	for key in ALPHABET:
		decflag = ""
		for char in encflag:
			decflag += unshift(char, key) #unshifting
		decflag = b16_decode(decflag) #decoding

		#checking if the flag is printable, if it's not than it can't be our flag
		isPrintable = True
		for x in decflag:
			if(x not in string.printable):
				isPrintable=  False
				break
		if(isPrintable):
			print(decflag)

unmain(encflag) #we get two option's for the flag (we need to try the both)


