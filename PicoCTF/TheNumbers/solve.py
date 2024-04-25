x = "16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }"
x = x.split(" ")
flag = ""
letter = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for num in x:
	if(num == "{" or num == "}"):
		flag+=num
	else:
		flag+=letter[int(num)]

print(flag)

flag = ""

for char in x:
	if(char == "{" or char == "}"):
		flag+=char
	else:
		flag+=chr(64 + int(char)) #65 in hex to ascii is A
print(flag)



