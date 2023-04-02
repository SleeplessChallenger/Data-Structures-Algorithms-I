"""
will implement MinBinaryHeap
the lower the .priority the bigger importance
"""

from math import floor


class Node:

    def __init__(self, val, priority):
        self.val = val
        self.priority = priority


class PriorityQueue:

    def __init__(self):
        self.values = []

    def enqueue(self, value, priority):
        node = Node(value, priority)
        self.values.append(node)
        self.sift_up()

    def sift_up(self):
        idx = len(self.values) - 1
        element = self.values[idx]
        while idx > 0:
            parent_idx = floor((idx - 1) / 2)
            parent = self.values[parent_idx]
            if element.priority <= parent.priority:
                break
            self.values[idx] = parent
            self.values[parent_idx] = element
            idx = parent_idx

    def dequeue(self):
        node = self.values[0]
        end = self.values.pop()
        if len(self.values) > 1:
            self.values[0] = end
            self.sift_down()
        return node

    def sift_down(self):
        idx = 0
        element = self.values[0]
        length = len(self.values)
        while True:
            left_idx = 2 * idx + 1
            right_idx = 2 * idx + 2
            swap = None
            if left_idx < length:
                left_child = self.values[left_idx]
                if left_child.priority < element.priority:
                    swap = left_idx

            if right_idx < length:
                right_child = self.values[right_idx]
                if (swap is None and right_child.priority < element.priority) or (
                        swap is not None and right_child.priority < left_child.priority):
                    swap = right_idx

            if swap is None:
                break

            self.values[idx] = self.values[swap]
            self.values[swap] = element

            idx = swap


if __name__ == "__main__":
    queue = PriorityQueue()
    queue.enqueue(5, 2)
