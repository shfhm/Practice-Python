
# coding: utf-8

# In[2]:


def strStr(haystack, needle):
    if needle in haystack:
        return haystack.index(needle)
    else:
        return -1

