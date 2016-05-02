'''
Created on 09/feb/2016

@author: Matteo
'''
sequence = "abcd"

def reverse(sequence):
    reversed_sequence = []
    i = len(sequence)-1
    #print (i)
    while i>=0:
        #print (i)
        reversed_sequence.append(sequence[i])
        i = i-1
    
    return reversed_sequence
        
x = reverse(sequence)

for i in x:
    print (i, end = '')
    
########oppure###########
sequence = "abcd"
def reverse_2nd_version(sequence):
    reversed_sequence = []
    i = len(sequence)-1
    #print (i)
    while i>=0:
        #print (i)
        reversed_sequence.append(sequence[i])
        i = i-1
    reverse = ""
    for i in reversed_sequence:
        reverse = reverse+i
    return reverse
