
# coding: utf-8

# In[ ]:


#convert decimal to binary string

class stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return self.len(items)
    
class solution:
    def dec_to_bin(dec_number):
        s=stack()
        while dec_number > 0:
            rem=dec_number%2
            s.push(rem)
            dec_number=dec_number // 2
            bin_str=""
        while not s.is_empty():
            bin_str = bin_str + str(s.pop())    #append to string
        return bin_str
    
print(solution.dec_to_bin(10))

