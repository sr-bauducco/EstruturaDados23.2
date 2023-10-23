class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def isEmpty(self) -> bool:
        return self.items == []
    
    def getAll(self):
        return self.items
    
pilha_1 = Stack()
pilha_2 = Stack()
pilha_1.push(4)
pilha_1.push(2)
pilha_1.push(7)
print(pilha_1.getAll())
print(pilha_2.getAll())
pilha_1.pop()
pilha_2.push(5)
print(pilha_1.getAll())
print(pilha_2.getAll())
print(pilha_1.peek())
print(pilha_2.peek())