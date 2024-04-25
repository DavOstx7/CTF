#!/usr/bin/env python3

'''
	// I made myself dizzy converting all of these numbers into different bases,
    // so I just *know* that this vault will be impenetrable. This will make Dr.
    // Evil like me better than all of the other minions--especially Minion
    // #5620--I just know it!

byte[] myBytes = {
            106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
            0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
            0142, 0131, 0164, 063 , 0163, 0137, 0143, 061 ,
            '9' , '4' , 'f' , '7' , '4' , '5' , '8' , 'e' ,
        };
'''
'''
hexpassword = ''
decpassword = ''
'''
base = None
password = [ 'BASE10', '106' , '85'  , '53'  , '116' , '95'  , '52'  , '95'  , '98'  , #base 10?
             'BASE16', '0x55', '0x6e', '0x43', '0x68', '0x5f', '0x30', '0x66', '0x5f', #base 16?
             'BASE8', '0142', '0131', '0164', '063' , '0163', '0137', '0143', '061' , #base 8?
             'READY', '9' , '4' , 'f' , '7' , '4' , '5' , '8' , 'e'] #they are already translated (value does not translate to ascii)

flag = ''
ready = False
for value in password:
	if(value == 'BASE10'):
		base = 10
		continue
	if(value == 'BASE16'):
		base = 16
		continue
	if(value == 'BASE8'):
		base = 8
		continue
	if(value == 'READY'):
		ready = True
		continue
	if(ready):
		flag+=value
		continue
	if(value[0] == '0'):
		if(value[1] == 'x'):
			value = value[2:]
		else:
			value = value[1:]
	'''
	if(base == 10):
		print("[10] value: " + value)
		hexpassword += hex(int(value)).split('x')[1]
		decpassword += value
	if(base == 16):
		print("[16] value: " + value)
		hexpassword += value
		decpassword += str(int(value, base))
	'''
	#after looking at the hint, it talks about ascii characters, so this is not the solution we need
	#instead, we need to translate all of the values to int, then use the chr() to make them ascii, and add them to the password

	x = value
	if(base == 8):
		x = int(value, base)
	if(base == 16):
		x = int(value, base)

	x = int(x)
	flag += chr(x)

flag = "picoCTF{" + flag + "}"
print(flag)
'''
print('decpassword: picoCTF{' + decpassword + '}')
print('hexpassword: picoCTF{' + hexpassword + '}')
'''



