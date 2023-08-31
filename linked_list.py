class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append_to_begin(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def insert(self, pos, value):
        current_node = self.head
        new_node = Node(value)
        for i in range(pos - 1):
            if current_node.next:
                current_node = current_node.next
            else:
                print("Incorrect pos")
                return -1
        new_node.next = current_node.next
        current_node.next = new_node

    def print_list(self):
        current = self.head
        while current:
            if current.next:
                print(current.val, end=' ')
            else:
                print(current.val)
            current = current.next


if __name__ == "__main__":
    linked = LinkedList()
    linked.append_to_begin(5)
    linked.append_to_begin(6)
    linked.append(12)
    linked.append_to_begin(7)
    linked.append_to_begin(8)
    linked.append(13)
    linked.print_list()
    linked.insert(8, 222)
    linked.print_list()
