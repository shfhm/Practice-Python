__author__ = 'Sahar'


def max(a):
    x=0
    for x in range(0,len(a)-1):
        if a[x+1] > a[x]:
            max=a[x+1] 
        else:
            max=a[x]
    print(max)
    index=0
    for i in a:
        mul2=i*2
        if max == mul2:
            print(index)
            break
        index+=1
    if index > len(a)-1:
        return -1
    
  

