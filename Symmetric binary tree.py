#symmetric binary tree. Given a binary tree, check whether it is a mirror of itself.
__author__='Sahar'

from collections import deque
class treenode(object):
    def __init__(self, root):
        self.val=root
        self.left=None
        self.right=None
        
class solution(object):
    def symmetric(self, root):
        if (root == None):
            return True
        q=deque()    #q=[]
        q.append(root.left)
        q.append(root.right)
        while q:
            left=q.pop()
            right=q.pop()
            if (left is None) and (right is None):
                continue  
            if (left is None) or (right is None):
                return False
            if left.val == right.val:
                q.append(left.left)
                q.append(right.right)
                q.append(left.right)
                q.append(right.left)
            else:
                return False
        return True
    
s=solution()
root=treenode(1)
root.left=treenode(2)
root.right=treenode(2)
root.left.left=treenode(3)
root.right.right=treenode(3)
root.left.right=treenode(4)
root.right.left=treenode(4)
print(s.symmetric(root))

