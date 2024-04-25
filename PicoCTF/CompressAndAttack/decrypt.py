#!/usr/bin/python3 -u
import codecs
import zlib
from random import randint
import os
from Crypto.Cipher import Salsa20
import binascii
import itertools
from pwn import *

# Okay, so after googling for the solution, I understand that I wasn't close.
# The way to decrypt this, is by exploiting the zlib and the fact the Salsa is a stream cipher and not block cipher (length of text = length of ciphertext)
# The thign with zlib is it used entropy encoding it doesn't computes the entropy on single characters, but on subsequences.
# Basically meaning, if we give it repeated stuff, the length of the compressed data will be smaller than random data.
# I found out by giving the netcat input, that every 4 right chars, vs 4 not right chars, the difference is 1 length.

alphabet = string.ascii_letters + string.digits + "_}"
flag = "picoCTF{"

r = remote("mercury.picoctf.net", 29350)
value = 48 #this is the value for picoCTF{
while (flag[-1] != "}"):
    found = False
    for char in alphabet:
        try:
            r.sendline(flag + char)
            for i in range(3):
                response = r.recvline()
            if(int(response.decode().strip()) == value):
                flag+=char
                print("found a good char! " + flag)
                found = True
                break
        except:
            found = True
            r = remote("mercury.picoctf.net", 29350)
    if(found == False):
        value+=1

print(flag)

#This code works, but another option is just checking which 'int(response.decode().strip())' is the the smallest, and adding it at the end to the flag



