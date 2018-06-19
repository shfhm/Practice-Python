
class Trienode(object):
    def __init__(self):
        self.dict={}
        self.ends=False
        
class AddWords(object):
    def __init__(self):
        self.root=Trienode()
        
    def insert(self, word):
        cur = self.root
        for char in word:
            child=cur.dict.get(char)
            if child is None:
                child=Trienode()
                cur.dict[char]=child  
            cur=child
        cur.ends=True
        
    def search(self, word):
        cur=self.root
        for char in word:
            child=cur.dict.get(char)
            if child is None:          #search whole word
                return False
            else:
                cur=child
        return cur.ends
    
    
s=AddWords()
print(s.insert('ab'))
print(s.search('ab'))
print(s.search('a'))         

