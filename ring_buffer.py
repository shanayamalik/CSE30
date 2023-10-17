class RingBuffer:
    def __init__(self, size: int):
        self.size = size
        self.queue = [None] * size
        self.head = self.tail = 0
        self.num_elements = 0
        
    def is_empty(self) -> bool:
        #Return True only if the buffer is empty
        return self.num_elements == 0
    
    def is_full(self) -> bool:
        #Return True only if the buffer is full
        return self.num_elements == self.size
    
    def en_queue(self, value: int):
        """
        Add an element to the back of the queue. If the buffer is full,
        remove the oldest element to make room for the new element.
        """
        if self.is_full():
            self.de_queue()
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.size
        self.num_elements += 1
    
    def de_queue(self) -> bool:
        """
        Remove the oldest element from the front of the queue. 
        Return True if an element was removed, False otherwise.
        """
        if self.is_empty():
            return False
        self.head = (self.head + 1) % self.size
        self.num_elements -= 1
        return True
    
    def get_rear(self) -> int:
        """
        Return the value of the element at the back of the queue.
        Return -1 if the queue is empty.
        """
        return self.queue[self.tail - 1] if self.num_elements != 0 else -1
    
    def get_front(self) -> int:
        """
        Return the value of the element at the front of the queue.
        Return -1 if the queue is empty.
        """
        return self.queue[self.head] if self.num_elements != 0 else -1
    
    def get_average(self) -> float:
        """
        Return the average of all elements in the queue. 
        Return -1.0 if the queue is empty.
        """
        if self.is_empty():
            return -1.0
        return sum(self.queue) / self.num_elements

#ringBuffer = RingBuffer(3)
#print(ringBuffer.is_empty()) # return True
#ringBuffer.en_queue(1) # return None (No return is necessary for this function)
#ringBuffer.en_queue(2) # return None
#ringBuffer.en_queue(3) # return None
#ringBuffer.en_queue(4) # return None (the queue is full).  → it should overwrite the old values 
#print(ringBuffer.get_rear())      # return 4
#print(ringBuffer.get_front())     # return 2
#print(ringBuffer.is_full())       # return True
#print(ringBuffer.get_average()) # return 3.0
#print(ringBuffer.de_queue())   # return True
#print(ringBuffer.is_full())       # return False
#print(ringBuffer.de_queue())   # return True
#print(ringBuffer.de_queue())   # return True
#print(ringBuffer.de_queue())   # return False (queue is empty)
#print(ringBuffer.is_empty())     # return True
#print(ringBuffer.get_rear())      # return -1
#print(ringBuffer.get_front())     # return -1
