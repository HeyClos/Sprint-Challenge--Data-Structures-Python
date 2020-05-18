class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []

    # We're just adding stuff onto here so we wont need to return anything
    def append(self, item):
        # save remaining capacity into a variable
            # original_capacity = self.capacity
        self.capacity = self.capacity - 1
        # If we're at capacity enter the scope of this if statement
        if self.capacity == -1: # try <= later
            # I need item to overwrite oldest item in RingBuffer
            # How will i know which is oldest? it wont always be [-1]
            # oldest_item = item
            # for i in self.storage:
            self.storage.pop(0)
            self.storage.insert(0, item)
            
            # self.storage[0] = self.storage[original_capacity]
            # i dont think we need to use len(self.storage)
        else:
            print (self.capacity)
            # append item into RingBuffer
            self.storage.append(item)
        
        

    def get(self):
        # return all items in RingBuffer
        return self.storage
