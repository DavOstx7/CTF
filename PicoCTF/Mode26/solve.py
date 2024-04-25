#!/usr/bin/env python3
import sys

#string = sys.argv[1]

def add13(char):
	newchar = ord(char) + 13
	if(ord(char) > 96): #lowercase
		if(newchar > 122):
			newchar-=26
	else: #uppercase
		if(newchar > 90):
			newchar-=26
	return chr(newchar)
	
def rot13(string):
	newstring = ""
	for char in string:
		if(char.isalpha() == True):
			newstring+=add13(char)
		else:
			newstring+=char
	return newstring

if __name__ == "__main__":
	decoded = rot13(sys.argv[1])
	print(decoded)

