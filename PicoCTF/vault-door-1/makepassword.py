f = open('password.txt', 'r')
flag = ""
for i in range(32):
	flag+="x"

for line in f:
	line = line.strip()
	index = int(line.split("(")[1].split(")")[0] )
	value = line.split('==')[1].replace("'", "").split("&&")[0]
	
	tmp = list(flag)
	tmp[index]=value
	flag = ''.join(tmp)


flag = "picoCTF{" + flag + "}"
print(flag)




"""
password.charAt(0)=='d'&&
password.charAt(29)=='3'&&
password.charAt(4)=='r'&&
password.charAt(2)=='5'&&
password.charAt(23)=='r'&&
password.charAt(3)=='c'&&
password.charAt(17)=='4'&&
password.charAt(1)=='3'&&
password.charAt(7)=='b'&&
password.charAt(10)=='_'&&
password.charAt(5)=='4'&&
password.charAt(9)=='3'&&
password.charAt(11)=='t'&&
password.charAt(15)=='c'&&
password.charAt(8)=='l'&&
password.charAt(12)=='H'&&
password.charAt(20)=='c'&&
password.charAt(14)=='_'&&
password.charAt(6)=='m'&&
password.charAt(24)=='5'&&
password.charAt(18)=='r'&&
password.charAt(13)=='3'&&
password.charAt(19)=='4'&&
password.charAt(21)=='T'&&
password.charAt(16)=='H'&&
password.charAt(27)=='f'&&
password.charAt(30)=='b'&&
password.charAt(25)=='_'&&
password.charAt(22)=='3'&&
password.charAt(28)=='6'&&
password.charAt(26)=='f'&&
password.charAt(31)=='0'&&
"""