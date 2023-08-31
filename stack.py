class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:

    def __init__(self):
        self.head = None

    def PushStack(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def PrintStack(self):
        current = self.head
        while current:
            if current.next:
                print(current.val, end=' ')
            else:
                print(current.val)
            current = current.next


if __name__ == "__main__":
    stack = Stack()
    stack.PushStack(5)
    stack.PrintStack()
    stack.PushStack(15)
    stack.PrintStack()