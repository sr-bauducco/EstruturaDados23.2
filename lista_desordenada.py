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
        
class UnorderedList:
    def __init__(self):
        self.head = None

    def __len__(self):
        return self.size()

    def __repr__(self):
        current_node = self.head
        items = list()
        counter = 0
        while current_node:
            counter += 1
            items.append(current_node.getData())
            current_node = current_node.getNext()
        return f"{self.__class__.__name__}(size: {counter}, items: {items})"

    def get_items(self):
        items = []
        current_node = self.head
        while current_node:
            items.append(current_node.getData())
            current_node = current_node.getNext()
        return items

    def add(self, item): # adiciona no começo da lista
        new = Node(item)
        new.setNext(self.head)
        self.head = new
    
    def append(self, item): # adiciona no final da lista
        current_node = self.head
        if self.head is None:
            self.head = Node(item)
        while current_node:
            if current_node.getNext() is None:
                current_node.setNext(Node(item))
                break
            else:
                current_node = current_node.getNext()
    
    def insert(self, pos, item): # adiciona na posição pos
        if pos == 0:
            self.add(item)
        elif pos >= self.size():
            self.append(item)
        else:
            previous_node = self.head
            current_node = self.head.getNext()
            counter = 1
            while current_node:
                if counter == pos:
                    new = Node(item)
                    previous_node.setNext(new)
                    new.setNext(current_node)
                    break
                else:
                    previous_node = current_node
                    current_node = current_node.getNext()
                    counter += 1
    
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
        if pos == 0 or len(self.get_items()) == 1:
            c = self.head.getData()
            self.head = self.head.getNext()
            return c
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
    
lista = UnorderedList()
lista.add(2)
lista.add(3)
lista.add(5)
lista.add(8)
lista.add(12)
lista.add(56)
lista.append(58)
print(lista.size())
print(lista.index(12))
print(lista.get_items())
