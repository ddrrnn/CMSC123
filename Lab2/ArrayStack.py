from uu import Error

class Element:
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

    def expand(self):
        self.capacity += self.DEFAULT_EXPANSION


class ArrayStack(Array):
    def top(self):
        if self.size == 0:
            return None
        else:
            return self.contents[self.size-1]

    def push(self, value):
        if self.size < self.capacity:
            element = Element(value, self.size)
            self.contents = self.contents + [element]
            self.size += 1
        elif self.size == self.capacity:
            self.expand()
            self.push(element)

    def pop(self):
        if self.size > 0:
            removed = self.contents[self.size - 1]
            self.contents = self.contents[:self.size - 1]
            self.size -= 1
            return removed
        else:
            raise Exception('Empty Stack')
