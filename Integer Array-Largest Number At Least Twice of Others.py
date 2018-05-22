
# coding: utf-8

# In[1]:


__author__ = 'Sahar'


def max(a):
    x=0
    for x in range(0,2):
        if a[x+1] > a[x]:
            max=a[x+1]        
    print(max)
    for i in a:
        if i*2 == max:
            return True
    return False
    
  

