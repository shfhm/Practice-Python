#4Sum II
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
        if (A and B and C and D) == []:
            return 0
        else: 
            count=0
            AB = Counter(a+b for a in A for b in B)
            CD = Counter(c+d for c in C for d in D)
            for k1,v1 in AB.items():
                for k2,v2 in CD.items():        
                    if (k1 == k2):
                        count+=(v1)*(v2)
            return count

        
A=[-1,1,1,1,-1]
B=[0,-1,-1,0,1]
C=[-1,-1,1,-1,-1]
D=[0,1,0,-1,-1]       
# A= [1,2]
# B= [-2,-1]
# C= [-1,2]
# D= [0,2]
# A= [0]
# B= [0]
# C= [0]
# D= [0]
# A= [-1,-1]
# B= [-1,1]
# C= [-1,1]
# D= [1,-1]
s=Solution()
print(s.fourSumCount(A, B, C, D))

