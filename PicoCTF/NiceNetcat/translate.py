#!/usr/bin/env python3

s=""
f = open('./output.txt', 'r')
for line in f.readlines():
	line = line.strip()
	char = chr(int(line))
	s+=char
print(s)

