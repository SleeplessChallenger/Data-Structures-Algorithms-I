"""
Look in IterativeBst for notes
"""


class Node(object):

    def __init__(self, data):
        self.root = data
        self.left = None
        self.right = None


class BinarySearchTree(object):

    def __init__(self):
        self.top = None

    def recursive(self, node, value):
        """
        node defines root(node) and self.top.root == .val
        """
        if node is None:
            """
            If self.top == None =>
            we define in BST as self.top, but the all inner stuff (.root, .left, .right) defines in Node.
            
            If root exists and if it is != None then
            newly created node will move either to left or right from it and so on
            """
            node = Node(value)
        elif self.top.root > value:
            node.left = self.recursive(node.left, value)
        elif self.top.root <= value:
            node.right = self.recursive(node.right, value)

        return node

    def insert(self, value):
        self.top = self.recursive(self.top, value)


if __name__ == "__main__":
    conv = BinarySearchTree()
    conv.insert(4)
    conv.insert(8)
    conv.insert(2)

    tree = BinarySearchTree()
    tree.root = Node(10)
