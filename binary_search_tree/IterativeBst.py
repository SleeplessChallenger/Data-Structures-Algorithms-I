"""
root - the top node in a tree
child - a node directly connected to another node when moving away from the Root
Parent - the converse notion of a child
Siblings - a group of nodes with the same parent
Leaf - a node with no children
Edge - the connection between one node and another

Trees -> Binary Trees -> Binary Search Trees
Tree can have multiple nodes with undefined amount of children
Binary Tree: each node at most can have 2 children
Binary Search Tree can have from 0 to 2 children per node
and sorted in a binary search manner
i.e. every node to the left of a parent node is
always less than the parent and every node to the
right of a parent node is always greater than the parent

Big(O):
* Insertion O(log n)
* Searching O(log n)

But not guaranteed!!!!
y = log[2] (x)
in other words: only one step up when we DOUBLE the number of nodes

2x number of nodes: 1 extra step
4x number of nodes: 2 extra steps
8x number of nodes: 3 extra steps
"""


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


"""
Every 'tree' variable defines a separate tree (it has same properties of Node above).
So, we put all values inside one tree => every Node variable has it's own .left and .right

When there is no root out 'insert' value become root.
After it next 'insert' at first ALSO defines as Node and we compare it with 
self.root.right and self.root.left

And thus we change values via .right/.left.
The next variable is attached to self.root [.left and .right precisely] and so on
"""


class BinarySearchTree:

    def __init__(self):
        self.root = None

    # iterative
    def insert(self, new_value):
        new_node = Node(new_value)
        if not self.root:
            self.root = new_node
            return self
        curr = self.root
        while True:
            if new_node.value == curr.value:
                return False
            elif new_node.value < curr.value:
                if curr.left is None:
                    curr.left = new_node
                    return self
                curr = curr.left
            else:
                # Case for new_node.value > curr.value
                if curr.right is None:
                    curr.right = new_node
                    return self
                curr = curr.right

    def find_node_by_value_return_node(self, new_value):
        if self.root is None:
            return False

        current = self.root
        start = False
        while current and not start:
            """
            When current hit the end of the tree the loop will stop.
            Or when start == True i.e. we found our value
            """
            if new_value < current.val:
                current = current.left
            elif new_value > current.val:
                current = current.right
            else:
                start = True

        if not start:  # if start == False then we didn't find value and ended at some leaf
            return False
        return current

    def find_node_by_value(self, value):
        """
        resembles the one above, but return only True/False
        """
        if not self.root:
            return False
        cur = self.root
        found = False
        while cur and not found:
            if cur.val > value:
                cur = cur.left
            elif cur.val < value:
                cur = cur.right
            else:
                return True

        return False
