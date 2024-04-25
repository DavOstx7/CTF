KEY_LEN = 50000
encflag = "0345376e1e5406691d5c076c4050046e4000036a1a005c6b1904531d3941055d"

"""
kf = open(KEY_FILE, "rb").read()

	if stop >= KEY_LEN:
		stop = stop % KEY_LEN
		key = kf[start:] + kf[:stop]
	else:
		key = kf[start:stop]
	key_location = stop
"""

# from this we can understand that if we give input at the length of (KEY_LEN - len(originalflag)) characters,
# we will get to the second padding (second padding is like the first padding, which was on the flag)

def generate(ourstring):
	s= ""
	for i in range(KEY_LEN - 32): #the encrypted flag length is 64, so the original is 32
		s+="x"

	# piping to nc mercury.picoctf.net 41934 with "\n" doesn't change anything, it dismiss it so we don't need to print(..., end = ""). (I checked it)
	# from here this will go to the second padding
	print(s)

	s=ourstring #adding the orignal length of the flag (right now it will encrypt it with the same key as it did for the unencrypted flag)

	print(s) #stdout then piping it to nc

	#the result will be our encrypted 32 'y's

ourstring = ""
for i in range(32): #adding the orignal length of the flag
		ourstring+="y" #it could be a trick to use the first couple chars as picoCTF because it will probably be it, and then we could compare it to the encflag.

generate(ourstring) #- this will get the make stop reach 50,000, and then add an additional 32




result = "1b5e2825011a1b2501411825011b4d2501494d25011f41250149490225011d1d" #for visuality




"""
result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), flag, key))
in our case, result = result, flag = ourstring, key = ?
so now we need to find key
"""
storeK = []
for i in range(0, len(result), 2):
	hexa = result[i] + result[i+1] #"{:02x}"
	dec = int(hexa,16) # ord(p) ^ k

	#dec = ord("y") ^ k
	"""
	
	1000  # 8 (binary) ---> k
	0011  # 3 (binary) ---> ord(p)
	----  # APPLY XOR ('vertically')
	1011  # result = 11 (binary) --> dec
	
	to get k we need to do dec ^ ord("y")
	"""

	k = dec ^ ord("y")
	storeK.append(k)

print(storeK)

# Now we have all of the k values, the and the encrypted key so we can decrypt it.

flag = ""
counter = 0
for i in range(0, len(encflag), 2):
	hexa = encflag[i] + encflag[i+1] #"{:02x}"
	dec = int(hexa,16)

	k = storeK[counter]
	counter+=1
	#we know that dec = ord(?) * k
	ordX = dec ^ k
	char = chr(ordX)
	flag+=char

print(flag)




