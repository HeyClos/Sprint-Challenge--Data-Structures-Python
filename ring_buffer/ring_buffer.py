class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []

    # We're just adding stuff onto here so we wont need to return anything
    def append(self, item):
        # save remaining capacity into a variable
        remaining_capacity = self.capacity -1
        oldest_item = self.storage
        # If we're at capacity enter the scope of this if statement
        if remaining_capacity == 0:
            # I need item to overwrite oldest item in RingBuffer
            # How will i know which is oldest? it wont always be [-1]
            # oldest_item = item
            oldest_item = item
        else:
            # append item into RingBuffer
            self.storage.append(item)

    def get(self):
        # return all items in RingBuffer
        return self.storage