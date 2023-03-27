"""
Big O

Insertion O(1)
Removal O(1)
Searching O(n) technically it's O(n/2) as we use divide and conquer
Access O(n)

"""


class Node:

    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, new_value):
        """
        to add node to the end
        """
        new_node = Node(new_value)
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail.next.prev = self.tail  # or new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return self

    def pop(self):
        """
        for removing head
        """
        if not self.head:
            return False
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = temp.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def shift(self):
        """
        to remove old head
        """
        if not self.head:
            return False
        old_head = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = old_head.next
            self.head.prev = None
            old_head.next = None
        self.length -= 1
        return old_head

    def unshift(self, new_value):
        """
        to add new head
        """
        new_node = Node(new_value)
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return self

    def get_by_index(self, index):
        """
        get node by index
        """
        if index < 0 or index >= self.length:
            return False
        elif index <= (self.length / 2):
            count = 0
            temp = self.head
            while count != index:
                count += 1
                temp = temp.next
        else:
            count = self.length - 1
            temp = self.tail
            while count != index:
                count -= 1
                temp = temp.prev
        return temp

    def set_value_by_index(self, index, new_value):
        """
        set new value for existing node
        """
        new = self.get_by_index(index)
        if not new:
            return False
        new.val = new_value
        return True

    # actually self.length in two elif statements gets increased as we call those methods
    def insert(self, index, new_value):
        """
        to insert node at particular index
        """
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            return not self.unshift(new_value)
        elif index == self.length:
            return not self.push(new_value)
        else:
            new_node = Node(new_value)
            node_before_index = self.get_by_index(index - 1)
            node_at_index = node_before_index.next

            node_before_index.next = new_node
            new_node.prev = node_before_index

            new_node.next = node_at_index
            node_at_index.prev = new_node

            self.length += 1
            return True

    def remove(self, index):
        """
        to remove at certain index
        """
        if index < 0 or index >= self.length:
            return False
        elif index == 0:
            return self.shift()
        elif index == self.length - 1:
            return self.pop()
        else:
            node_at_current_index = self.get_by_index(index)

            node_at_current_index.prev.next = node_at_current_index.next
            node_at_current_index.next.prev = node_at_current_index.prev

            node_at_current_index.prev = None
            node_at_current_index.next = None

            self.length -= 1
            return node_at_current_index


if __name__ == "__main__":
    doubly_linked_list = DoublyLinkedList()

    doubly_linked_list.push(5)
    doubly_linked_list.push(7)
    doubly_linked_list.push(9)
    doubly_linked_list.push(19)
    doubly_linked_list.push(1)
