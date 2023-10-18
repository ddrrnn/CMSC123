class Element:
    def __init__(self, value, index):
        self.value = value
        self.index = index

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

class Array:
    def __init__(self):
        self.size = 0
        self.contents = []

    def isEmpty(self):
        return (self.size == 0)

    def addElement(self, value):
        element = Element(value, self.size)
        self.contents = self.contents + [element]
        self.size += 1

    def removeElement(self, index):
        if 0 <= index < self.size:
            self.contents = self.contents[:index] + self.contents[index+1:]
            self.size -= 1
