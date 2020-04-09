class Node(object):
    def __init__(self, value, prev, nxt):
        self.value = value
        self.next = nxt
        self.prev = prev

class Queue(object):
    def __init__(self):
        self.tail = None
        self.head = None

    def enqueue(self, obj):
        node = self.tail
        if node is None:
            self.tail = self.head = Node(obj, None, None)
        else:
            while node.next is not None:
                node = node.next
            node.next = Node(obj, node, None)
            self.head = node.next

    def dequeue(self):
        if self.head is not None:
            self.head = self.head.prev
            if self.head is not None:
                self.head.next = None
            else:
                self.tail = None

    def dump(self, mark):
        """Debugging function that dumps the contents of the list."""
        output = []
        node = self.tail
        while node is not None:
            output.append(node.value)
            node = node.next
        print(mark + ": " + str(output))
