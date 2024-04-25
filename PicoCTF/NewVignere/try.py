# import string
import string

# constants
LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

# see caesar cipher for what these are
def b16_decode(cipher):
    dec = ""

    for c in range(0, len(cipher), 2):

        b = ""
        b += "{0:b}".format(ALPHABET.index(cipher[c])).zfill(4)
        b += "{0:b}".format(ALPHABET.index(cipher[c+1])).zfill(4)

        dec += chr(int(b,2))
    
    return dec

def unshift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 - t2) % len(ALPHABET)]

# tries to decrypt
def get_key(s, matrix):
    # if we can't go further down
    if len(matrix) == 1:
        # add the last value
        for a in ALPHABET:
            k = str(s) + str(a)
            pt = ""
            for i,c in enumerate(enc):
                pt += unshift(c, k[i%len(k)])

            pt = b16_decode(pt)

            # if the plain text is good then print it
            if all(c in "abcdef0123456789" for c in pt):
                print(pt)
                print(k)
        return
    
    # recursively build key string
    for x in matrix[0]:
        s2 = str(s) + str(x)
        get_key(s2, matrix[1:len(matrix)])

# encrypted text
enc = "ioffdcjbfjmcifelcaloifgcjecgpgiebpfeiafhgajafkmlfcbpfbioflgcmacg"


keys = []

# create array
[keys.append([]) for i in range(0,32)]

# loop through alphabet twice
for a in ALPHABET:
    for b in ALPHABET:
        # generate key pair
        key = str(a) + str(b)
        
        # store plain text      
        pt = ""

        # unshift all values with key pair
        for i,c in enumerate(enc):
            pt += unshift(c, key[i%len(key)])

        # decode
        pt = b16_decode(pt)

        # loop through decrypted plaintext
        for cur in range(0, len(pt)):

            # check each plaintext char to see if its valid, if it is then add the arrays
            if pt[cur] in "abcdef0123456789":
                keys[cur].append(key)

# print the possible key pairs
#for key in keys:
    #print(key)

# decrypt the code
get_key("", keys[0:5])