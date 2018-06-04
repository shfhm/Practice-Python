#maxdepth-level order 

from collections import deque

class treenode(object):
    def __init__(self, root):
        self.val=root
        self.left = None
        self.right = None

class solution(object):
    def maxdepth(self, root):
        if root == None:
            return 0
        q1=deque()   #q1=[] 
        count=0
        q1.append(root)
        while q1:
            q2=deque()    #q2=[]
            while q1:
                root=q1.pop()
                if (root.left):
                    q2.append(root.left)
                if (root.right):
                    q2.append(root.right)
            q1=q2     
            count+=1
        return count
   

s=solution()
root=treenode(1)
root.left=treenode(2)
root.right=treenode(5)
root.left.left=treenode(3)
root.left.right=treenode(4)
root.right.right=treenode(6)
print(s.maxdepth(root))

