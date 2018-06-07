
# coding: utf-8

# In[5]:


class solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count=0
        for i in S:
            for x in J:
                if x==i:
                    count+=1
        return count
    
J='aA'
S='aAAbbb'
s=solution()
print(s.numJewelsInStones(J,S))

