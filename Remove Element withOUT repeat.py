__author__ = 'Sahar'

list=[]
for j in a:
    if a.count(j) == 1:
        list.append(j)
    if a.count(j) > 1:
        if j != target:
            if j not in list:  
                list.append(j)   
print(list)

