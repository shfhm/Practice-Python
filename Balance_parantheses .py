#problem solving with algorithms and data structures

class Stack:
    def __init__(self):
        self.items = [] 
    def is_empty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

class solution:   
    def check_parantheses(string):
        s=Stack()
        index=0
        balance=True
        while index < len(string) and balance:
            item=string[index]
            if item == "(":
                s.push(item)
            else:
                if s.is_empty():
                    balance = False
                else:
                    s.pop()
            index=index+1
        if balance and s.is_empty():
            return True
        else:
            return False
 

cp=solution.check_parantheses('((()))')
print(cp)
cp=solution.check_parantheses('(()')
print(cp)    

