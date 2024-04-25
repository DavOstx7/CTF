from Crypto.Cipher import DES
import binascii
import itertools
import random
import string
# IMPORTANT TO REMEMBER FOR ME - encode/decode is just adding/removing the b'', hexlify/unhexlify is translating.


# I gave the nc the value of 61, and copied the returned values.
enc_flag = "5bbff2ab58c331ddaddb7b781cadf1fd81de472fba2cf5323a7330db70c71f339b36f9b3cc38abf3"
enc_flag = binascii.unhexlify(enc_flag)
text = '61'
text = binascii.unhexlify(text).decode()
ciphertext = "96860d62a72535a5"
ciphertext = binascii.unhexlify(ciphertext)

print(f'enc_flag = {enc_flag} \ntext = {text} \nciphertext = {ciphertext}')

def pad(msg):
    block_len = 8
    over = len(msg) % block_len
    pad = block_len - over
    return (msg + " " * pad).encode()

def double_encrypt(m, KEY1, KEY2):
    msg = pad(m)

    cipher1 = DES.new(KEY1, DES.MODE_ECB)
    enc_msg = cipher1.encrypt(msg)
    cipher2 = DES.new(KEY2, DES.MODE_ECB)
    return binascii.hexlify(cipher2.encrypt(enc_msg)).decode()

def double_decrypt(enc_flag, key1, key2):
	cipher2 = DES.new(key2, DES.MODE_ECB)
	X = cipher2.decrypt(enc_flag)
	cipher1 = DES.new(key1, DES.MODE_ECB)
	flag = cipher1.decrypt(X)
	# return binascii.hexlify(flag).decode() - this WAS THE MISTAKE! why would i hexlify this smh 
	#this is what it gives: 36643465303633643136643235306239353364303039653265663037653234312020202020202020
	#we are supposed to do it the opposite way of the double_encrypt method:
	#instead of the value coming to us as unhexlifyand we return it as hexlify, we need the value to come to us as hexlify (alread does) and return it as unhexlify (also better to decode)
	return flag.decode()
	

#We need to execute meet in the middle attack:
'''
text ---enc---> X ---enc---> ciphertext.
* What we can do, is encrypt the text with all the possibilites <X>
* Then, decrypt the ciphertext with all the possibilies <X> try to find a match.
*This reduces the complexity by a lot. Because we do not need to encrypt twice with every possibility.
instead of O((10^6)^2) ---> O(10^12) we get O(2*10^6)
'''
save = {} # format of <X:KEY> (X is the value after the first encryption)
text = pad(text)
key1 = None; key2 = None

#This takes like 30 seconds so best to save the time! the result are after this commented block
print('[+] starting encryption')
for num in itertools.product(string.digits, repeat=6):
	num = "".join(num)
	num = pad(num)
	cipher = DES.new(num, DES.MODE_ECB)
	X = cipher.encrypt(text)
	save[X] = num 

print('[+] starting decryption')
key_list = []
#there may be more than one possibility (we can do break after finding the first (which will give us the result), but it's cool to see the keys found!)
# p.s at the start I didn't know that all the key combinations I found produce the same flag (so it was better for safety). 
for num in itertools.product(string.digits, repeat=6):
	num = "".join(num)
	num = pad(num)
	cipher = DES.new(num, DES.MODE_ECB)
	X = cipher.decrypt(ciphertext)
	if (X in save):
		key1 = save[X]
		key2 = num
		key_list.append((key1, key2))
		#break - uncomment this for faster execution

print(key_list)
result = []
for key1, key2 in key_list:
	flag = double_decrypt(enc_flag, key1, key2)
	if(flag not in result):
		result.append(flag)

for flag in result:
	print("flag = " + flag)

#flag = 36643465303633643136643235306239353364303039653265663037653234312020202020202020
	






	




























