class SLLNode:
    def __init__(self, value):
        self.value = value
        self.nextNode = None  

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def setNext(self, nextNode):
        self.nextNode = nextNode

    def getNext(self):
        return self.nextNode

class SLL:
    def __init__(self):
        self.size = 0
        self.first = SLLNode(None)
        self.last = SLLNode(None)

    def isEmpty(self):
        return self.size == 0

    def addNode(self, value):
        new_node = SLLNode(value)
        lastNode = self.last #store current last node
        self.last = new_node #set new node as new last
        if self.isEmpty():
            self.first = new_node
        else:
            lastNode.setNext(new_node)
        self.size += 1

    def removeNode(self, x):
        if self.isEmpty():
            return

        #if x == first node
        if self.first.getValue() == x:
            new_first = self.first.getNext() #set the second node as the new first node
            self.first.setNext(SLLNode(None)) #break connection of the old first node and second node
            self.first = new_first

            if self.size == 1:
                self.first = SLLNode(None)
                self.last = SLLNode(None)
            self.size -= 1
            return

        #if x is in the middle/last of the list
        # using the previous node
        prev = self.first
        current = self.first.getNext()
        while current is not None: #iterate through the list until the last node
            if x == current.getValue():
                prev.setNext(current.getNext()) #connect left and right nodes of current
                current.setNext(SLLNode(None)) #current points to none
                if current == self.last: #last node
                    self.last = prev #last now becomes the left node of last
                self.size -= 1
                return
            prev = current
            current = current.getNext()
    
