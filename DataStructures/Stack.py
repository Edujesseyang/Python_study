from typing import Any


class Stack:
    def __init__(self):
        self.main_list = list()
        self.size = 0
        self.top = None

    def is_empty(self) -> bool:
        return self.size == 0

    def push(self, item) -> None:
        self.main_list.append(item)
        self.size += 1
        self.top = item

    def pop(self) -> type[list[Any]]:
        if len(self.main_list) == 0:
            raise IndexError("Stack is empty")
        else:
            top = self.main_list[-1]

    def peek(self) -> type[Any]:
        if len(self.main_list) == 0:
            raise IndexError("Stack is empty")
        else:
            return self.main_list[self.top]

    def print(self) -> None:
        for item in self.main_list:
            print(item, ", ")



test = Stack()
test.push(1)
test.push(2)
test.push(3)
test.print()
print("=======")
print(test.pop())
print(test.pop(), " then: ")
test.print()