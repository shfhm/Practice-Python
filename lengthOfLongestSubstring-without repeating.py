
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen={}
        start=0
        max_len=0
        for end in range(len(s)):
            if s[end] not in seen:
                seen[s[end]]=end
                max_len=max(max_len, end-start+1)
            else:
                start= max(start,seen[s[end]]+1 )
                max_len=max(max_len, end-start+1)
                seen[s[end]]=end
        return(max_len)
 

#s="jxdlnaaij"
s="tmmzuxt"
t=Solution()
print(t.lengthOfLongestSubstring(s))

