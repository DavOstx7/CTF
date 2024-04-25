import random
import os
import enchant
import itertools

d = enchant.Dict("en_US") #d.check(string) ---> return True if string is a word, else return False
alphabet = list('abcdefghijklmnopqrstuvwxyz')


#file names: originalflag.txt  originalstudy-guide.txt

#~~~~~~~~~~~~~~~~~CODE~~~~~~~~~~~~~~~~~#

def solution1():
    #The idea is to try decode the bee quiz study file with the same method it was encoded, and check if the decoded word is an actual word.

    head = []
    counter = 1
    f = open("../originalstudy-guide.txt", "r")
    for word in f.readlines():
        if(counter == 0):
            break
        head.append(word.strip())  #first original 3 words - best performance wise and accuracy
        counter-=1

    print(f'original head {head}')

    for alphabet_combo in list(itertools.islice(itertools.permutations(alphabet), 5000000)):

        dictionary = dict(zip(alphabet, alphabet_combo))
        '''
        #Produce a dictionary that hopefully is the decoder  
        random.shuffle(shuffled := alphabet[:])                      ~~~THIS TAKES TOO LONG~~~
        dictionary = dict(zip(alphabet, shuffled))
        '''

        #Produce a different dictionary each time
        newhead = []
        for word in head:
            newhead.append("".join(dictionary[c] if c in dictionary else c for c in word))

        

        print(newhead)
        Work = True
        #Checking if the decoder works on the first 15 words.
        for word in newhead:
            if(d.check(word) == False):
                Work = False
                break

        if(Work == True):
            print("Found a decoder dictionary: " + str(dictionary))
            break
solution1() # - takes too long

