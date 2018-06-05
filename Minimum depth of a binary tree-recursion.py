#minimum depth of a binary tree-recursion

class treenode(object):
    def __init__(self, root):
        self.val=root
        self.left= None
        self.right = None
class solution(object):
    def mindepth(self, root):
        if root == None:
            return 0
        if((root.left == None) and (root.right == None)):
            return 1
        return 1+min(self.mindepth(root.left), self.mindepth(root.right))

s=solution()
root=treenode(1)    
root.left=treenode(2)
root.right=treenode(5)
root.left.left=treenode(3)
root.left.right=treenode(4)
print(s.mindepth(root))

