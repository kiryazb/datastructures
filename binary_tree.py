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
        if value < node.val:
            if node.left is None:
                node.left = Node(value)
            else:
                self._recursion_append(value, node.left)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._recursion_append(value, node.right)

    def print_tree(self):
        if self.head:
            print(self.head.val)
            if self.head.left:
                self._recursion_print(self.head.left)
            if self.head.right:
                self._recursion_print(self.head.right)
        else:
            print("tree is empty")


    def _recursion_print(self, node):
        print(node.val)
        if node.left:
            self._recursion_print(node.left)
        if node.right:
            self._recursion_print(node.right)



if __name__ == "__main__":
    tree = Tree()
    tree.append(5)
    tree.print_tree()
    tree.append(4)
    tree.print_tree()
    tree.append(6)
    tree.print_tree()




