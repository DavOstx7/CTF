#!/usr/bin/env python3

#from string import ascii_lowercase
#from string import ascii_uppercase

from itertools import combinations

string = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸強㕤㐸㤸扽'

def testing(flag):
	result = ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
	return result

def mytesting(flag): #Made this for easier understanding of the code and how to reverse it.
	s = ""
	for i in range(0, len(flag), 2):
		char = flag[i]
		nextchar = flag[i+1]
		#print(f'ord of char: {ord(char)} | ord of nextchar: {ord(nextchar)}')
		neword = (ord(char) << 8) + ord(nextchar)
		newchar = chr(neword)
		#print('ord of new char: ' + str(neword))
		s+=newchar
	return s


def reverse(string):
	possible = [i for i in range(128)]
	result = ""

	for char in string:
		cord = ord(char)
		found = False

		for combo in combinations(possible, 2):
			charord, nextcharord = combo
			if((charord << 8) + nextcharord == cord):
				found = True
				char = chr(charord); nextchar = chr(nextcharord)
				result+=f'{char}{nextchar}'
				break

			if((nextcharord << 8) + charord == cord):
				found = True
				char = chr(charord); nextchar = chr(nextcharord)
				result+=f'{nextchar}{char}'
				break
		if(found == False):
			print("couldn't find a possible way to get: " + char)
	print(result)


def solutionguess(string):
	possible = ''.join(chr(i) for i in range(128))
	reveresed = ""
	for char in string:
		found = False
		for combo in combinations(possible, 2):
			x,y = combo
			if(mytesting([x,y]) == char):
				reveresed+=f'{x}{y}'
				found = True
				break
			if(mytesting([y,x]) == char):
				reveresed+=f'{y}{x}'
				found = True
				break
		if(found == False):
			print(f"couldn't find a pair that matches {char}")

	print(reveresed)

def try_reverse(string):
	'''
	ord of char: 80 | ord of nextchar: 105
	ord of new char: 20585
	'''
	for c in string():
		ordchar = ord(c)

def extra1(string):
	"""
	this solution is really smart. 
	the reason this works is because every char in string is basically 'chr((ord(flag[i]) << 8) + ord(flag[i + 1])'
	the code takes a value of ascii char, moves the bits of it to the left 8 times, then adds the value of the other ascii var.
	every ascii is represented by a byte, which is 2 hexa characters.
	so it basically means every char in the string is <{HEX-VALUE}{HEX-VALUE}>
	"""
	for char in string:	
		hexa = hex(ord(char)) #representing the char in hexa
		print(bytes.fromhex(hexa.split('x')[1]).decode('utf-8'), end = "") #translating the hexa char in ascii
	print()

def extra2(string):
	for i in range(len(string)):
		#ord(char) = ord(originalchar1) << 8 + ord(originalchar2)

		#moving the char 8 times to the right will give us originalchar1
		originalchar1 = chr(ord(string[i])>>8)
		print(originalchar1, end="") 

		#now we know ord(originalchar2) = ord(char) - ord((orginalchar1) << 8)
		originalchar2 = chr(ord(string[i]) - ((ord(originalchar1) << 8)))
		print(originalchar2, end = "")
	print()



extra1(string)
extra2(string)
solutionguess(string)
reverse(string) #this solution is faster