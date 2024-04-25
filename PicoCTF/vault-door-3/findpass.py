'''public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        char[] buffer = new char[32];
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) { 
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        String s = new String(buffer);
        return s.equals("jU5t_a_sna_3lpm18gb41_u_4_mfr340");
    }
}
'''

#String passwrd = picoCTF{<passowrd>}
#We need to find a password that after scrambling, will give us jU5t_a_sna_3lpm18gb41_u_4_mfr340


def replace(string, index, value):
	l = list(string)
	l[index] = value
	return "".join(l)

def solution1(): #calculate the value of the indexes and where they match, and make appropriate replacements.
	end_pass = "jU5t_a_sna_3lpm18gb41_u_4_mfr340"
	len_pass = 32
	start_pass = ""

	'''
	for (i=0; i<8; i++) {
	            buffer[i] = password.charAt(i);
	        }
	'''

	for i in range(8): #just copy
		start_pass += end_pass[i]

	'''
	for (; i<16; i++) {
	            buffer[i] = password.charAt(23-i);
	        }
	'''

	for i in range(15, 7, -1): 
	#The 'i' of the buffer is going from 8 to 15, so it's like appending. 
	#But the value of 23-i is going from 15 down to 8 with jumps of 1.
		start_pass += end_pass[i]

	'''
	 for (; i<32; i+=2) { 
	            buffer[i] = password.charAt(46-i);
	        }
	'''

	for i in range(30, 15, -2):
	#The 'i' of the buffer is going from 16 to 30, so it's like appending the value + ' ' (empty because we don't yet fill it but we need to jump 2 indexes)
	#the value of 46-i is 30 going down to 16 with jumpes of 2
		start_pass+=f'{end_pass[i]} '

	'''
	  for (i=31; i>=17; i-=2) {
	            buffer[i] = password.charAt(i);
	        }
	'''

	for i in range(17, 32, 2): #just copy (could've also did for i in range(31, 16, -2):)
	#we need to use a function, because we can't do start_pass[i] = end_pass[i] (strings are immutable)
		start_pass = replace(start_pass, i, end_pass[i])

	flag = 'picoCTF{' + start_pass + "}"
	print("solution1: " + flag)


def solution2(): #This is easier to understand, just replace the values back
	end_pass = "jU5t_a_sna_3lpm18gb41_u_4_mfr340"
	len_pass = 32
	start_pass = ""

	for i in range(32):
		start_pass+="*"

	assert len(start_pass) == 32

	'''
	for (i=0; i<8; i++) {
	            buffer[i] = password.charAt(i);
	        }
	'''

	for i in range(8): #just copy
		start_pass = replace(start_pass, i, end_pass[i])

	'''
	for (; i<16; i++) {
	            buffer[i] = password.charAt(23-i);
	        }
	'''

	for i in range(8, 16): #do the opposite
		start_pass = replace(start_pass, 23-i, end_pass[i])

	'''
	 for (; i<32; i+=2) { 
	            buffer[i] = password.charAt(46-i);
	        }
	'''

	for i in range(16, 32, 2): #do the opposite
		start_pass = replace(start_pass, 46-i, end_pass[i])

	'''
	  for (i=31; i>=17; i-=2) {
	            buffer[i] = password.charAt(i);
	        }
	'''

	for i in range(31, 16, -2): #do the opposite
	#could've also did for i in range(17, 32, 2):
		start_pass = replace(start_pass, i, end_pass[i])

	flag = 'picoCTF{' + start_pass + "}"
	print("solution2: " + flag)

solution1()
solution2()