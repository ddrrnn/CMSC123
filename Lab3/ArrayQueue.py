class Element:
    # Insert the 'Element' class you created in Lab2, since they should be the same
    def __init__(self, value, index):
        self.value = value
        self.index = index

    def setValue(self,value):
        self.value = value

    def getValue(self):
        return self.value

    def getIndex(self):
        return self.index

class Array:
    def __init__(self, capacity=10):
        self.contents = []
        self.size = 0          
        self.capacity = capacity
        self.DEFAULT_EXPANSION = 5

    def getCapacity(self):
        return self.capacity

    def isEmpty(self):
        return (self.size == 0)
   
    def getSize(self):
        return self.size

    def expand(self):
        self.capacity += self.DEFAULT_EXPANSION


class ArrayQueue(Array):
    # Note that class "ArrayQueue" inherits the class "Array" attributes and methods
    def front(self):
        if self.isEmpty():
            return Element(None, None)
        else:
            return self.contents[0]

    def enqueue(self, value):
        if self.size < self.capacity:
            element = Element(value, self.size)
            self.contents = self.contents + [element]
            self.size += 1
            return
        else:
            raise Exception

    def dequeue(self):
        if self.isEmpty():
            raise Exception
        else:
            removed = self.front()
            for i in range(0, self.size-1):
                self.contents[i] = self.contents[i+1]
            self.size -= 1
            return removed