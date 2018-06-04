#Maximum Depth of Binary Tree-Recursion 

class treenode(object):
    def __init__(self, root):
        self.val=root
        self.left = None
        self.right = None
        
class solution(object):
    def MaxDepth(self, root):
        if(root == None):
            return 0 
        return 1+max(self.MaxDepth(root.left), self.MaxDepth(root.right))
    
s=solution()   
root=treenode(1)
root.left=treenode(2)
root.right=treenode(5)
root.left.left=treenode(3)
root.left.rigth=treenode(4)
root.right.right=treenode(6)
print(s.MaxDepth(root))

