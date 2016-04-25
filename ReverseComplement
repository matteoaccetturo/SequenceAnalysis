'''
Created on 09/feb/2016

@author: Matteo
'''
# Input:  A DNA string Pattern
# Output: The reverse complement of Pattern
#from Esercizi.reverse import reverse

sequence = "acgt"
Pattern = "aaaacccggt"

def ReverseComplement(Pattern):
    revComp = '' # output variable
    # your code here
    revComp = reverse_2nd_version(Pattern)
    revComp = complement(revComp)
    
    
    return revComp


# Copy your reverse function from the previous step here.
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

# HINT:   Filling in the following function is optional, but it may come in handy when solving ReverseComplement
# Input:  A character Nucleotide
# Output: The complement of Nucleotide

Nucleotide = reverse_2nd_version(sequence)
def complement(Nucleotide):
    
    comp = '' # output variable
    # your code here
    for i in Nucleotide:
        if i == "a":
            comp = comp+"t"
        if i == "c":
            comp = comp+"g"
        if i == "t":
            comp = comp+"a"
        if i == "g":
            comp = comp+"c"
    return comp

# Pattern = complement(Nucleotide)
# x = ReverseComplement(sequence)
# print (x)
# 
# y = complement(Nucleotide)
# print(y)

z = ReverseComplement(Pattern)
print(z)


