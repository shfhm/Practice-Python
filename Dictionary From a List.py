import operator
s="OHHNAAA"
list=[]
dic={}
for i in range(len(s)):
    list.append(s[i])
    for j in range(len(list)):
        dic[list[i]]=list.count(list[i])
        
print(dic)

