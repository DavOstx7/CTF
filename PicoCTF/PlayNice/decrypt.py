'''
Here is the alphabet: 0uxtb3w4kj26q9m8gioe7nvahplr5dy1fzcs
Here is the encrypted message: xj5c181ropf5xjmyujnv0wlqrjdrbz
'''
from time import sleep
import signal
SQUARE_SIZE = 6

alphabet = "0uxtb3w4kj26q9m8gioe7nvahplr5dy1fzcs"
encrypted = "xj5c181ropf5xjmyujnv0wlqrjdrbz" #length is 30 

m = [['0', 'u', 'x', 't', 'b', '3'], ['w', '4', 'k', 'j', '2', '6'], ['q', '9', 'm', '8', 'g', 'i'], ['o', 'e', '7', 'n', 'v', 'a'], ['h', 'p', 'l', 'r', '5', 'd'], ['y', '1', 'f', 'z', 'c', 's']]

def get_index(letter, matrix):
	for row in range(SQUARE_SIZE):
		for col in range(SQUARE_SIZE):
			if matrix[row][col] == letter:
				return (row, col)
	print("letter not found in matrix.")
	exit()

def encrypt_pair(pair, matrix):
	p1 = get_index(pair[0], matrix) #gives (row,col) of the letter in the matrix
	p2 = get_index(pair[1], matrix) #gives (row, col) of the letter in the matrix

	if p1[0] == p2[0]:  #If they are on the same row
		return matrix[p1[0]][(p1[1] + 1)  % SQUARE_SIZE] + matrix[p2[0]][(p2[1] + 1)  % SQUARE_SIZE] #return matrix[row, <p1col> +1 % 6] + matrix[row, <p2col>+1 % 6]
	elif p1[1] == p2[1]: #If they are on the same col
		return matrix[(p1[0] + 1)  % SQUARE_SIZE][p1[1]] + matrix[(p2[0] + 1)  % SQUARE_SIZE][p2[1]] #return matrix[<p1row> +1 % 6, col] + matrix[<p2row> +1 % 6, col]
	else: #If they are neither
		return matrix[p1[0]][p2[1]] + matrix[p2[0]][p1[1]] #return matrix[<p1row>, <p2col>] + matrix[<p2row>, <p1col>]


def decrypt_pair(pair, matrix):
	p1 = get_index(pair[0], matrix) 
	p2 = get_index(pair[1], matrix) 

	if (p1[0] == p2[0]):
		#return the column values to the original forms
		col1 = p1[1] - 1
		col2 = p2[1] - 1

		if(col1 == -1):
			col1 = 5
		if(col2 == -1):
			col2 = 5
		
		return matrix[p1[0]][col1] + matrix[p2[0]][col2]

	elif (p1[1] == p2[1]):
		#Return the row values to the original forms
		row1 = p1[0] -1
		row2 = p2[0] - 1

		if(row1 == -1):
			row1 = 5
		if(row2 == -1):
			row2 = 5
	
		return matrix[row1][p1[1]] + matrix[row2][p2[1]]

	
	return matrix[p1[0]][p2[1]] + matrix[p2[0]][p1[1]] #Switch back the collums

def encrypt_string(s, matrix):
	result = ""
	if len(s) % 2 == 0:
		plain = s #This is the relevant one for us
	else:
		plain = s + "0uxtb3w4kj26q9m8gioe7nvahplr5dy1fzcs"[0] #--> plain = s+'0' (not relevant for us)
	for i in range(0, len(plain), 2):
		result += encrypt_pair(plain[i:i + 2], matrix) #result+=(encrypt_pair[plain[i], plain[i+1]])
	return result

def decrypt_string(s, matrix):
	result = ""
	if len(s) % 2 == 0:
		plain = s #This is the relevant one for us
	else:
		plain = s + "0" #--> plain = s+'0' (not relevant for us)

	for i in range(0, len(plain), 2):
		result+=decrypt_pair([plain[i], plain[i+1]], matrix)

	return result

#Basically, we don't care about the string its self, but the index of it.
#What the encryption does is it takes the index of the original value, changes the INDEX, and returns the new value that matches the new index.
#To reverse this process, we take the new value and new index, change the INDEX, and return the original value that matches the original index.

print(decrypt_string(encrypted, m))

