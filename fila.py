class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        self.items.pop(0)

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []
    
    def getAll(self):
        return self.items
    
fila = Queue()
fila.enqueue(5)
fila.enqueue(7)
fila.enqueue(9)
print(fila.getAll())
fila.dequeue()
print(fila.getAll())