class Element:
    # Insert the 'Element' class you created in Lab1, since they should be the same
    def __init__(self, value, index=0):
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
        self.size = 0               # The 'size' attribute must not exceed the 'capacity'      
        self.capacity = capacity
        self.contents = [None]*self.capacity
        self.DEFAULT_EXPANSION = 5
        self.frontIndex = 0
        self.rearIndex =0
       
    def getSize(self):
        # returns the size of the queue
        # Note that the size is based on frontIndex and rearIndex
        # REQUIRED
        return self.size




    def getCapacity(self):
        # returns the capacity of the queue
        # REQUIRED
        return self.capacity


    def isEmpty(self):
        # The isEmpty() operation returns true if the queue is empty and false if the queue is not empty
        # REQUIRED
        return self.size == 0


    def expand(self):
        # The expand() operation increases the capacity when necessary
        self.capacity += self.DEFAULT_EXPANSION
        self.contents += ([None]*self.DEFAULT_EXPANSION)


    def wrapAround(self):
        # The wrapAround() operation resets the Array back where head is at index 0
        # Note: You will only use this function when capacity is full and you wish to enqueue()
        # REQUIRED
        new_contents = [None] * self.capacity
        for i in range(self.capacity):
            new_contents[i] = self.contents[(self.frontIndex + i) % self.capacity]
        self.contents = new_contents
        self.frontIndex = 0
        self.rearIndex = self.size




class CircularQueue(Array):
    # Note that class "CircularQueue" inherits the class "Array" attributes and methods


    def front(self):
        # The front() operation returns a reference value to the front element of the queue, but doesn’t remove it
        # REQUIRED
        if self.isEmpty():
            return Element(None)
        else:
            return self.contents[self.frontIndex]




    def enqueue(self, value):
        # The enqueue() operation inserts an element at the end of the queue
        # If the capacity is full, you are not allowed to enqueue() an element to the queue
        # REQUIRED
        new_elem = Element(value, self.size)
        if self.size == self.capacity:
            self.expand()
            self.wrapAround()
            self.enqueue(value)
        else:
            self.contents[self.rearIndex] = new_elem
            self.rearIndex = (self.rearIndex + 1) % self.capacity
            self.size += 1




    def dequeue(self):
        # The dequeue() operation removes the element at the front of the queue
        # This should also return the 'Element' that was removed
        # REQUIRED
        if self.isEmpty():
            raise Exception
        else:
            removed = self.contents[self.frontIndex]
            self.contents[self.frontIndex] = Element(None)
            self.frontIndex = (self.frontIndex + 1) % self.capacity
            self.size -= 1
            return removed
