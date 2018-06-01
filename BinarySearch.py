
# coding: utf-8

# In[2]:



class node:
    def __init__(self, data=None, left=None, rigth=None):
        self.data=data
        self.left=left
        self.rigth=rigth

class BinarySearchTree(object):        
    def __init__(self, root=None):
        self.root = root
    def get_root(self):
        return self.root
    def insert(self, item):
        if self.root is None:
            self.root=Node(item)
        else:
            nd=self.root
            while nd is not None:
                if item < nd.data:
                    if nd.left is None:
                        nd.left=Node(item)
                        return
                    else:
                        nd=nd.left
                else:
                    if nd.rigth is None:
                        nd.rigth=Node(item)
                        return
                    else: 
                        nd=nd.rigth
    def search(self, node, item):
        if node is None:
            return False
        else:
            if node.data == item:
                return True
            if node.data > item:
                return self.search(node.left, item)
            else:
                return self.search(node.rigth, item)
            
    def size(self, node):
         if node is None:
            return 0
         else:
            return 1+ self.size(node.left)+self.size(node.rigth)
     
    #left,root,rigth
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print (node.data)
            self.inorder(node.rigth)
            
    #root,left,rigth
    def preorder(self, node):
        if node:
            print (node.data)
            self.preorder(node.left)
            self.preorder(node.rigth)
     
    #left,rigth,root
    def postorder(self, node):
            self.postorder(node.left)
            self.postorder(node.rigth)
            print(node.data)
            
    def get_min(self, node):
          if node.left is None:
               return node.data
          else:
               return self.get_min(nod.left)
            
    def get_max(self, node):
        if node.rigth is None:
            return node.data
        else:
            return self.get_max(node.rigth)
        

