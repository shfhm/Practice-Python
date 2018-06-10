
# coding: utf-8

# In[164]:


from collections import Counter
class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        AB=Counter((a+b) for a in A for b in B)
        return (sum(AB[-c-d] for c in C for d in D))

A=[-1,1,1,1,-1]
B=[0,-1,-1,0,1]
C=[-1,-1,1,-1,-1]
D=[0,1,0,-1,-1]  
# A= [1,2]
# B= [-2,-1]
# C= [-1,2]
# D= [0,2]
s=Solution()
print(s.fourSumCount(A, B, C, D))

