from uu import Error

class SLLNode:
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
    def __init__(self):
        self.size = 0
        self.topNode = SLLNode(None)
        self.topNode.setNext(SLLNode(None))

    def isEmpty(self):
        return (self.size == 0)

class SLLStack(SLL):
    def top(self):
        if self.size == 0:
            return SLLNode(None)
        else:
            return self.topNode
       
    def push(self, value):
        new_node = SLLNode(value)
        if self.isEmpty():
            self.topNode = new_node
        else:
            new_node.setNext(self.topNode)
            self.topNode = new_node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception('Empty Stack')
        removed = self.topNode
        self.topNode = self.topNode.getNext()
        self.size -= 1
        return removed

