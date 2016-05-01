'''
Created on 14/feb/2016

@author: Matteo
'''
# p = "GGGCCGTTGGT"
# q = "GGACCGTTGAC"
Pattern = "CCA"
Text = "CCACCT"
d = 0

def ApproximatePatternMatching(Pattern, Text, d):
    positions = [] # initializing list of positions
    # your code here
    for i in range (len(Text)-len(Pattern)+1):
        print(Text[i:i+len(Pattern)])
        if HammingDistance(Text[i:i+len(Pattern)], Pattern) <= d:
            positions.append(i)
    return positions

def HammingDistance(p, q):
    # your code here
    count = 0
    for i in range (0, len(p)):
        
        if p[i] != q[i]:
                count = count+1
                
    return count

# x = HammingDistance(p, q)
# print(x)

y = ApproximatePatternMatching(Pattern, Text, d)
print(y)
