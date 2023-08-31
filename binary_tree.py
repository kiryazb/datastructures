class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:


    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = self.head
        if self.head is None:
            self.head = Node(value)
        else:
            self._recursion_append(value, new_node)
            pass

    def _recursion_append(self, value, node):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._recursion_append(value, node.left)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._recursion_append(value, node.right)


if __name__ == "__main__":
    pass



