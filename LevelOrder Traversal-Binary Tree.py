
# coding: utf-8

# In[ ]:


class treenode(object):  
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class solution(object):
    def levelorder(self, root):
        if not root:
            return False 
        q1 = []
        q2 = []
        res=[]
        q1.append(root)
        
        while((q1 is not None) or (q2 is not None)):
            level = []
            while(len(q1) > 0):
                root = q1.pop()
                if (root):
                    level.append(root.val)
                    if (root.left):
                        q2.append(root.left)
                    if (root.right):
                        q2.append(root.right)
            res.append(level)
                
            level = []    
            while(len(q2) > 0):
                
                root=q2.pop()
                if (root):
                    level.append(root.val)
                if (root.right):
                    q1.append(root.right)
                if (root.left):
                    q1.append(root.left)
                    
            if (len(level) > 0):
                res.append(level)
        
            if(len(q1) == 0 and len(q2) == 0):
                break
        return res

