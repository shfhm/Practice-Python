#Anagram Detection-Count and Compare

def Solution(s1,s2):
    c1=[0]*26
    c2=[0]*26
    
    for i in range(len(s1)):
        index1=ord(s1[i])-ord('a')
        c1[index1]=s1.count(s1[i])
        
    for i in range(len(s2)):
        index2=ord(s2[i])-ord('a')
        c2[index2]=s2.count(s2[i])

    pos=True
    j=0 
    for j in range(0,25):
        if c1[j] != c2[j]:
             pos = False
        else:
            continue
    return pos

print(Solution('apple','peapl'))
print(Solution('apple','peapk'))

