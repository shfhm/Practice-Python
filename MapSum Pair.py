

class Mapsum:
    def __init__(self):
        self.map={}
        
    def insert(self, key, val):
        self.map[key]=val
        print("Null")
        
    def sum(self, prefix):
        sum=0
        for key, val in self.map.items():
            if key.find(prefix) == 0:
                sum+=self.map[key]    #val
        return sum
    
    
T=Mapsum()
T.insert("darabe",3)
print(T.sum("da"))
print(T.insert("dara",2))
print(T.sum("da"))

