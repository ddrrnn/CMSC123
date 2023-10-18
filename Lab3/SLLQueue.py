class SLLNode:
    # Insert the 'SLLNode' class you created in Lab2, since they should be the same
    def __init__(self, value):
        self.value = value
        self.nextNode = None

    def setValue(self,value):
        self.value = value

    def getValue(self):
        return self.value

    def setNext(self,nextNode):
        self.nextNode = nextNode

    def getNext(self):
        return self.nextNode

class SLL:
    # Insert the 'SLL' class you created in Lab2, since they should be the same
    def __init__(self):
        self.size = 0
        self.frontNode = SLLNode(None)
        self.frontNode.setNext(SLLNode(None))

    def getSize(self):
        return self.size

    def isEmpty(self):
        return (self.size == 0)
   
class SLLQueue(SLL):
    # Note that class "SLLQueue" inherits the class "SLL" attributes and methods
    def front(self):
        if self.isEmpty():
            return SLLNode(None)
        else:
            return self.frontNode

    def enqueue(self, value):
        new_node = SLLNode(value)
        if self.isEmpty():
            self.frontNode = new_node
        else:
            current = self.frontNode
            while current.getNext() is not None:
                current = current.getNext()
            current.setNext(new_node)
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            raise Exception
        else:
            removed = self.front()
            self.frontNode = removed.getNext()
            removed.setNext(SLLNode(None))
            self.size -= 1
            return removed

