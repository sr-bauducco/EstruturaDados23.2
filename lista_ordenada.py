class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext
        
class OrderedList:
    def __init__(self):
        self.head = None

    def add(self, item): # adiciona em ordem crescente
        if self.head is None or item < self.head.getData():
            new = Node(item)
            new.setNext(self.head)
            self.head = new
        else:
            current_node = self.head
            next_node = self.head.getNext()
            added = False
            while next_node:
                if item < next_node.getData():
                    new = Node(item)
                    current_node.setNext(new)
                    new.setNext(next_node)
                    added = True
                    break
                else:
                    current_node = next_node
                    next_node = next_node.getNext()
            if not added:
                current_node.setNext(Node(item))
    
    def remove(self, item): # remove um item assumindo que ele está na lista
        if self.head.getData() == item:
            self.head = self.head.getNext()
        else:
            previous_node = self.head
            current_node = self.head.getNext()
            while current_node:
                if current_node.getData() == item:
                    previous_node.setNext(current_node.getNext())
                    break
                else:
                    previous_node = current_node
                    current_node = current_node.getNext()
                
    def pop(self, pos=-1):
        # remove e retorna o item da posição pos, se pos não for informado ele remove
        # o último item da lista.
        if pos == 0:
            self.head = self.head.getNext()
        else:
            previous_node = self.head
            current_node = self.head.getNext()
            counter = 1
            while current_node:
                if counter == pos or current_node.getNext() is None:
                    previous_node.setNext(current_node.getNext())
                    return current_node.getData()
                else:
                    previous_node = current_node
                    current_node = current_node.getNext()
                    counter += 1
    
    def search(self, item):
        current_node = self.head
        found = False
        while current_node:
            if current_node.getData() == item:
                found = True
                break
            else:
                current_node = current_node.getNext()
        return found
    
    def index(self, item): # supõe que o item está na lista
        current_node = self.head
        counter = 0
        while current_node:
            if current_node.getData() == item:
                break
            else:
                current_node = current_node.getNext()
                counter += 1
        return counter

    def size(self):
        current_node = self.head
        counter = 0
        while current_node:
            current_node = current_node.getNext()
            counter += 1
        return counter
   
    def isEmpty(self):
        return self.head is None

    
    def get_items(self):
        items = []
        current_node = self.head
        while current_node:
            items.append(current_node.getData())
            current_node = current_node.getNext()
        return items
    
    
    
lista = OrderedList()
lista.add(85)
lista.add(3)
lista.add(5)
lista.add(8)
lista.add(56)
lista.add(12)
print(lista.size())
print(lista.index(12))
print(lista.get_items())