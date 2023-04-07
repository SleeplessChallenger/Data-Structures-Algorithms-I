"""
Big O
Insertion O(1)
Removal - It depends: O(1) if the beginning(best case) or O(N) from the end (worst case)
Searching O(n)
Access O(n)
"""


class Node:
    def __init__(self, val):
        """
        piece of data - val reference
        to next node - next
        """
        self.val = val
        self.next = None


"""
Example of how nodes look like:

first = Node('Hi')
first.next = Node('there')
first.next.next = Node('how')
first.next.next.next = Node('are')
first.next.next.next.next = node('you')

every Node is a new connection => maybe that's why every new value will have it's 
own .next value. I.e. we have 4, and it's .next is 7. Then we have 7 which .next is 10
"""


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, new_value):
        """
        to add new node to the end
        """
        new_node = Node(new_value)
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return self

    def pop(self):
        """
        to remove last node
        """
        if not self.head:
            return None
        nxt = self.head
        curr = nxt
        # stop one node before last
        while nxt.next:
            curr = nxt
            nxt = nxt.next
        self.tail = curr
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return curr

    def shift(self):
        """
        to remove head
        """
        if not self.head:
            return None
        curr = self.head
        self.head = curr.next
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return curr

    def unshift(self, new_value):
        """
        for adding new head and shifting existing
        """
        new_node = Node(new_value)
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return self

    # var.next = self.head
    # self.head = var

    def get_node_by_index(self, index):
        if index < 0 or index >= self.length:
            return None

        count = 0
        node = self.head
        while count != index:
            node = node.next
            count += 1
        return node

    def set_value_by_index(self, index, new_value):
        """
        set new value for existing node
        """
        node = self.get_node_by_index(index)
        if not node:
            return False
        node.val = new_value
        return True

    def insert(self, index, new_value):
        """
        to insert node at particular index
        """
        if index < 0 or index > self.length:
            return False
        elif index == self.length:
            return not self.push(new_value)
        elif index == 0:
            return not self.unshift(new_value)
        else:
            new_node = Node(new_value)
            node_before_index = self.get_node_by_index(index - 1)
            temp = node_before_index.next
            node_before_index.next = new_node
            # assign node that was next
            new_node.next = temp
            self.length += 1
            return True

    def remove(self, index):
        """
        to remove at certain index
        """
        if index < 0 or index >= self.length:
            return False
        elif index == self.length - 1:
            return self.pop()
        elif index == 0:
            return self.shift()
        else:
            # 5
            node_before_index = self.get_node_by_index(index - 1) # 4
            # unlink node_before_index that is at index
            temp = node_before_index.next # 5
            node_before_index.next = temp.next # 6
            self.length -= 1
            return temp

    def reverse(self):
        node = self.head
        self.head = self.tail
        self.tail = node
        prev = None
        nxt = None
        i = 0
        while i < self.length:
            nxt = node.next  # save next
            node.next = prev
            """
            reverse. Here we switch the pointer to self.tail -> None
            we just reassign the variable: node.next from now means previous
            + for the first iteration we have node = 100 => the next of it will
            be None
            in other words:
            we save the next value of the old list
            and then the next will be the previous
            """
            prev = node
            node = nxt
            i += 1
        return self


if __name__ == "__main__":
    linked_list = SinglyLinkedList()

    linked_list.push(4)
    linked_list.push(6)
    linked_list.push(8)
    print(linked_list.shift())
