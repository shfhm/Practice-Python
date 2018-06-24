#Aanagram detection
#Big-O is o(n^2)

"""
the anagram problem will check to see that each character in the first
string actually occurs in the second
"""

def sol(s1,s2):
    l1=list(s1)
    l2=list(s2)
    l1.sort()
    l2.sort()
    index=0
    matches = True
    while index < len(s1) and matches:
        if l2[index] == l1[index]:
            index=index+1
        else:
            matches = False
    return matches
    
    
print(sol('snbgf','fbsng'))
print(sol('snbgl','fbsng'))

