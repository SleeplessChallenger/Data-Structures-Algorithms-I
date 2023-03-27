"""
Big O

Insertion O(1)
Removal O(1)
Searching O(n)
Access O(n)

Example of Queue using LinkedList
"""


class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:

    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enqueue(self, var) -> int:
        var = Node(var)
        if not self.first:
            self.first = var
            self.last = self.first
        else:
            self.last.next = var
            self.last = var

        self.size += 1
        return self.size

    def dequeue(self):
        if self.size == 0:
            return False
        temp = self.first
        if self.size == 1:
            self.last = None
        self.first = temp.next
        self.size -= 1
        return temp
