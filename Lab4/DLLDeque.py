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
    # Insert the 'DLL' class you created in Lab1, since they should be the same
    def __init__(self):
        self.size = 0
        self.headNode = DLLNode(None)
        self.tailNode = self.headNode
        self.tailNode.setNext(None)
        self.headNode.setPrev(None)

    def getSize(self):
        # returns the size of the queue
        # REQUIRED
        return self.size

    def isEmpty(self):
        # The isEmpty() operation returns true if the queue is empty and false if the queue is not empty
        # REQUIRED
        return self.size == 0

class DLLDeque(DLL):
    # Note that class "DLLQueue" inherits the class "DLL" attributes and methods
    def first(self):
        # The first() operation returns a reference value to the first element of the deque, but doesn’t remove it
        # REQUIRED
        if self.isEmpty():
            return DLLNode(None)
        else:
            return self.headNode

    def last(self):
        # The last() operation returns a reference value to the last element of the deque, but doesn’t remove it
        # REQUIRED
        if self.isEmpty():
            return DLLNode(None)
        else:
            return self.tailNode

    def insertFirst(self, value):
        # The insertFirst() operation inserts an element at the front of the deque
        # REQUIRED
        new_node = DLLNode(value)
        self.headNode.setPrev(new_node)
        new_node.setNext(self.headNode)
        new_node.setPrev(None)
        self.headNode = new_node
        self.size += 1

    def insertLast(self, value):
        # The insertLast() operation inserts an element at the end of the deque
        # REQUIRED
        new_node = DLLNode(value)
        self.tailNode.setNext(new_node)
        new_node.setPrev(self.tailNode)
        new_node.setNext(None)
        self.tailNode = new_node
        self.size += 1

    def removeFirst(self):
        # The removeFirst() operation removes the element at the front of the deque
        # This should also return the 'DLLNode' that was removed
        # REQUIRED
        if self.isEmpty():
            raise Exception
        removed = self.headNode
        self.headNode = removed.getNext()
        removed.setNext(None)
        self.size -= 1
        return removed

    def removeLast(self):
        # The removeLast() operation removes the element at the end of the deque
        # This should also return the 'DLLNode' that was removed
        # REQUIRED
        if self.isEmpty():
            raise Exception
        removed = self.tailNode
        self.tailNode = removed.getPrev()
        removed.setPrev(None)
        self.size -= 1
        return removed



