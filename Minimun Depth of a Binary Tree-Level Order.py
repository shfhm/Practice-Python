#Minimun Depth of a Binary Tree- Level Order
#The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

class treenode(object):
    def __init__(self, root):
        self.val=root
        self.left= None
        self.right= None

class solution(object):
    def mindepth(self, root):
        if (root == None):
            return 0
        q1 = []
        q1.append(root)
        depth=1
        while q1:
            q2=[]
            while q1:
                root=q1.pop()
                if (root.left):
                    q2.append(root.left)
                if (root.right):
                    q2.append(root.right)
                if ((root.left == None) and (root.right ==None)):
                    return depth
            q1=q2
            depth+=1
        return depth
s=solution()
root=treenode(1)
root.left=treenode(2)
root.left.left=treenode(3)
root.left.left.left=treenode(4)
root.left.left.left.left=treenode(5)
print(s.mindepth(root))

