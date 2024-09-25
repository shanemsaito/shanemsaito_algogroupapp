# OPTION 2 - IMPLEMENT STACK
# DO NOT SHARE

# 2. Implement a growable integer stack (without using container libraries like vector, list, etc.)
#    that satisfies the following requirements:

# `push` adds a given value to the top
# `pop`  returns and removes the value at the top
# `peek` returns the value at the top
# `size` returns the count of values

class Node:
    def __init__(self, val, next_node=None) -> None:
        self.val = val
        self.next = next_node

class IntStack:
    def __init__(self) -> None:
        self.top = None
        self._size = 0

    def push(self, val: int) -> None:
        new_node = Node(val, self.top)
        self.top = new_node
        self._size += 1

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("Cannot pop from empty stack")
        popped_val = self.top.val
        self.top = self.top.next
        self._size -= 1
        return popped_val

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("Cannot peek from empty stack")
        return self.top.val

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        if self.top:
            return False
        return True