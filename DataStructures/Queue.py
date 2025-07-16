

class Queue:
    def __init__(self):
        self.main_list = []
        self.size = 0
        self.front = None
        self.back = None


    def offer(self,item):
        self.main_list.append(item)
        self.size += 1
        if self.front is None:
            self.front = item
            self.back = self.front
        else:
            self.back = item


    def poll(self):
        if self.size == 0:
            raise IndexError("Queue is empty")
        else:
            self.size -= 1
            temp = self.back
            self.main_list.delete(self.back)
            self.back = self.main_list[self.size]
            return temp


    def is_empty(self):
        return self.size == 0


    def size(self):
        return self.size


    def peek(self):
        return self.back


    def peek_front(self):
        return self.front