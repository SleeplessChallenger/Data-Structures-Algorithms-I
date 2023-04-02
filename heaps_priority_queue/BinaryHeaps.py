"""
In a MaxBinaryHeap, parent nodes are always larger than child nodes.
In a MinBinaryHeap, parent nodes are always smaller than child nodes
But there are no guarantees between sibling nodes

Binary heaps are used to implement Priority Queues, which
are very commonly used data structures

To find child from parent: Left Child is (2n + 1) and Right Child is (2n + 2)
And to find parent: (n - 1)/2 floored - to find Parent from Child
Aforementioned stuff is done to indices of nodes not the values of nodes

BinaryHeaps Big (O):
* Insertion O(log n)
	Even with worst case it will be O(log n) while Binary Tree can be O(n)
* Removal O(log n)
* Search O(n)
	For searching BinaryTree is much better for 16 elements 4 comparisons
"""


class MaxHeap:
    def __init__(self, array):
        self.heap = self._build_heap(array)

    def peek(self):
        if not len(self.heap):
            raise ValueError("Empty Heap")

        return self.heap[0]

    def check_length(self):
        return len(self.heap)

    def _build_heap(self, array):
        parent_idx = (len(array) - 2) // 2
        for idx in reversed(range(parent_idx + 1)):
            self.sift_down(idx, len(array) - 1, array)

        return array

    def insert(self, value):
        self.heap.append(value)
        self.sift_up()

    def delete(self):
        to_delete_node = self.heap[0]
        last_node = self.heap.pop()
        curr_length = self.check_length()

        if curr_length > 0:
            self.heap[0] = last_node
            self.sift_down(0, curr_length - 1, self.heap)

        return to_delete_node

    def sift_up(self):
        idx = len(self.heap) - 1
        while idx > 0:
            parent_idx = (idx - 1) // 2
            if self.heap[idx] > self.heap[parent_idx]:
                self.swap_action(idx, parent_idx, self.heap)
                idx = parent_idx
            else:
                return

    def sift_down(self, idx, length, heap):
        child_idx_one = idx * 2 + 1
        while child_idx_one <= length:
            child_idx_two = idx * 2 + 2 if idx * 2 + 2 <= length else -1
            if child_idx_two != -1 and heap[child_idx_two] > heap[child_idx_one]:
                swap = child_idx_two
            else:
                swap = child_idx_one

            if heap[swap] > heap[idx]:
                self.swap_action(swap, idx, heap)
                idx = swap
                child_idx_one = idx * 2 + 1
            else:
                return

    @staticmethod
    def swap_action(i, j, arr):
        arr[i], arr[j] = arr[j], arr[i]


if __name__ == "__main__":
    binary_heap = MaxHeap([4, 1, 7, 8, 3])
    print(binary_heap.heap)
