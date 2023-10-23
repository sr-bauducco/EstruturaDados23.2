class Deque:
    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        self.items.pop()

    def removeRear(self):
        self.items.pop(0)

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []
    
    def getAll(self):
        return self.items
    
    def getRear(self):
        return self.items[0]
    
    def getFront(self):
        return self.items[-1]

deque = Deque()
deque.addFront(4)
deque.addFront(7)
deque.addRear(8)
deque.addRear(9)
print(deque.getAll())
print(deque.getRear())
print(deque.getFront())
