
# coding: utf-8

# In[15]:


#Insert Delete GetRandom O(1)

import random
class solution(object):
    def __init__(self):
        self.set=[]
        self.index={}
    def insert(self, val):
        if val in self.set:
            return False
        self.set.append(val)
        self.index[val]=len(self.set)-1
        return self.set, self.index
        #return True
        
    def remove(self, val):
        if val not in self.set:
            return False
        
        self.index[self.set[-1]]=self.index[val]
        
        self.set.pop()
        self.index.pop(val)
        return self.set, self.index
       
    def Getrandom(self):
        return self.set[random.randint(0, len(self.set))]
        
    
s=solution()
print(s.insert(0))
print(s.insert(1))
print(s.insert(3))
print(s.remove(3))
print(s.Getrandom())

