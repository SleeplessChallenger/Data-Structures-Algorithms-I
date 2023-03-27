"""
Insertion O(1)
Removal O(1)
Searching O(n)
Access O(n)
"""


class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:

    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def push(self, var):
        var = Node(var)
        if not self.first:
            self.first = var
            self.last = self.first
        else:
            temp = self.first
            self.first = var
            var.next = temp  # self.first.next = temp

            # another method
            var.next = self.first
            self.first = var

        self.length += 1
        return self.length

    def pop(self, var):
        if self.length == 0:
            return False

        temp = self.first
        self.first = temp.next
        self.length -= 1

        if self.length == 0:
            self.first = None
            self.last = None
        return temp.val

        # noinspection PyUnreachableCode
        """
                    # another variant
                    temp = self.first
                    if self.length == 1:  # if self.first == self.last
                        self.last = None
                    self.first = temp.next
                    self.length -= 1
                    return temp.val
            
                    # method which also can be used
                    temp = self.first
                    if self.first == self.last:
                        self.first == None
                        self.last == None
                    else:
                        self.first = temp.next
                    return temp.val
                """
