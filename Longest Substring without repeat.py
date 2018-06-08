
# coding: utf-8

# In[13]:


import numpy as np
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        list=[]
        count=0
        j=0
        i=0
        temp=0
        for j in range(len(s)-1):
            t=s.count(s[j])
            if (t >1):
                for i in range(len(s)-1):
                    list.append(s[i])
                    if s[j] == s[i]:
                        count+=1
                        if count > 1:
                            return np.size(list)-1
                        else:
                            continue
            else:
                continue
                       
                            

s="abcabc"
#s="bbbbb"
S=Solution()
print(S.lengthOfLongestSubstring(s))

