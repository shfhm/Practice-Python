
# coding: utf-8

# In[ ]:


#path sum

class treenode(object):
    def __init__(self, root):
        self.val = root
        self.left = None
        self.right = None
class solution(object):
     def pathsum(self, root, sum):
        if root is None:
            return False
        if(root.left is None and root.right is None and root.val == sum):
            return True
        if root.left != None or root.right != None:
            return self.pathsum(root.left, sum - root.val) or self.pathsum(root.right, sum - root.val)
        return False
        
s=solution()
root=treenode(5)
root.left=treenode(4)
root.right=treenode(8)
root.left.left=treenode(11)
root.right.right=treenode(4)
root.right.left=treenode(13)
root.left.left.left=treenode(7)
root.left.left.right=treenode(2)
root.right.right.right=treenode(1)
print(s.pathsum(root,22))

