import itertools
import math
from Crypto.Util.number import inverse
from Crypto.Util.number import long_to_bytes

c = 964354128913912393938480857590969826308054462950561875638492039363373779803642185
n = 1584586296183412107468474423529992275940096154074798537916936609523894209759157543
e = 65537


def check_is_prime(x):
	for i in range(2, x//2): #no need to do x//2 + 1, because if a number like 10 is dividable by 5, it will already find it at 2 (with x//2, it will iterate only till 4)
		if(x % i == 0):
			return False
	return True


def generate_prime_nums(maxxx):
	prime = []
	for i in range(maxxx + 1):
		if(check_is_prime(i)):
			prime.append(i)
	return prime

#From googling, I found that in RSA, n = p * q, where p and q are prime numbers. n will only equal to n * 1, and p * q as far as factorization.

''' I tried creating a script to find p and q, but it takes too long for me, so I looked on yt and found
that I can use factorzing (the factor of 6 for example are, 6,1 <obvious>, and 3,2)
A good website to calculate these values are factordb, and since our n value is relatively small, we can use it to calculate p and q
'''

p = 2434792384523484381583634042478415057961
q = 650809615742055581459820253356987396346063


# Next step, is calculating this totient of n, which is (p-1) * (q-1)

totient = (p-1) * (q-1) #e has to be between 1 and totient of n ---> 1<e<totient(n)

# Next step, is calculating d which is used to derive the private/public key. d = e^(-1) (mod totient(n))
d = inverse(e, totient)

m =  pow(c,d,n) #pow(c,d,n) is the same as math.pow(c, d) % n. m--> message (origina/unenecrypted message)

#c = pow(m,e,n) #pow(m,e,n) is the sane as math.pow(c, d) % n. c--> ciphertext (encrypted text)

flag = long_to_bytes(m) #This will translate the long number to string

print(flag)












