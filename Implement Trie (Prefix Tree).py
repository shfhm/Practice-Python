#Trie

class Trienode:
    def __init__(self):
        self.children = {}
        self.endofword = False
        
class Trie:
    def __init__(self):
        self.root = Trienode()
    def insert(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char]=Trienode()
            cur=cur.children[char]
        cur.endofword = True
        
    def search(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            cur=cur.children[char]
        return cur.endofword
    
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur=self.root
        for char in prefix:
            if char not in cur.children:
                return False
            cur=cur.children[char]
        return True
    
    
T=Trie()
T.insert("adab")
T.insert("dara")
T.search("Dara")
T.search("adab")
T.startsWith("ad")

