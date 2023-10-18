class DLLNode:
    def __init__(self, value, nextNode=None, prevNode=None):
        self.value = value
        self.nextNode = nextNode
        self.prevNode = prevNode

    def setValue(self, value):
        self.value = value


    def getValue(self):
        return self.value


    def setNext(self, nextNode):
        self.nextNode = nextNode


    def getNext(self):
        return self.nextNode


    def setPrev(self, prevNode):
        self.prevNode = prevNode


    def getPrev(self):
        return self.prevNode

class DLL:
    def __init__(self):
        self.first = DLLNode(None)
        self.last = DLLNode(None)
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def addNode(self, value):
        new_node = DLLNode(value)
        if self.isEmpty():
            self.first = new_node
            self.last = new_node
        else:
            new_node.setPrev(self.last)
            self.last.setNext(new_node)
            self.last = new_node
        self.size += 1

    def removeNode(self, value):
        current = self.first
        while current is not None:
            if current.getValue() == value:  
                if current.getPrev() is None: #first node
                    self.first = current.getNext()
                else:
                    current.getPrev().setNext(current.getNext()) #prev will point to next of current
                
                if current.getNext() is None: #last node
                    self.last = current.getPrev() #change last to second as the last node
                else:
                    current.getNext().setPrev(current.getPrev()) #connect right node and left node of current


                current.setNext(DLLNode(None))
                current.setPrev(DLLNode(None))


                self.size -= 1


                if self.isEmpty():
                    self.first = DLLNode(None)
                    self.last = DLLNode(None)
                return
            current = current.getNext()
