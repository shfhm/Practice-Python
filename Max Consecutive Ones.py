__author__ = 'Sahar'

count=0
list=[]
for i in a:
    if target == i:
        count+=1
    else:
        list.append(count)
        count=0
print(max(list)) 

