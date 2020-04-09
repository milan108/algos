class Node:
    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt
    def __repr__(self):
        nval = self.next and self.next.value or None
        return r"[{self.value}:{repr(nval)}]"

class SingleLinkedList(object):
    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, obj):
        node = self.begin
        if node is None:
            # list is empty
            node = Node(obj,None)
            self.begin = node
            self.end = node
        else:
            # make previous node next value point to this node and reassign self.end
            # walk the list and until we find a node with a null next ref and add new Node
            while node.next is not None:
                node = node.next
            node.next = self.end = Node(obj,None)     

    def pop(self):
        """Removes the last item and returns it."""
        node = self.begin
        if node is None:
            return None
        elif node.next is None:
            self.begin = None
            self.end = None
            return node.value 
        while node.next.value is not self.end.value:
            if node.next is None:
                break
            node = node.next 
        ret = self.end.value 
        self.end = node
        self.end.next = None
        return ret

    def shift(self, obj):
        """Inserts item into beginning of the list."""
        self.begin = Node(obj,self.begin)
        if self.end is None:
            self.end = self.begin
    
    def unshift(self):
        """Removes the first item and returns it."""
        if self.begin is None:
            return None
        ret = self.begin.value 
        self.begin = self.begin.next
        return ret

    def remove(self, obj):
        """Finds a matching item and removes it from the list."""
        node = self.begin
        index = 0
        
        # account for removing first element case
        if node is not None:
            if node.value is obj:
                # remove first element
                self.begin = node.next
                return index

        while node.next is not None:
            index += 1
            if node.next.value is obj:
                # dissect the list
                self.end = node
                if node.next is not None:
                    self.end.next = node.next.next
                break
            node = node.next

        while self.end is not None:
            self.end = self.end.next
        return index
    
    def first(self):
        """Returns a *reference* to the first item, does not remove."""
        if self.begin is None:
            return None
        return self.begin.value
    
    def last(self):
        """Returns a reference to the last item, does not remove."""
        if self.end is None:
            return None
        return self.end.value

    def count(self):
        count = 0
        if self.begin is not None:
            count = 1
        node = self.begin
        while node.next is not None:
            node = node.next
            count += 1
        return count

    def get(self, index):
        """Get the value at index."""
        node = self.begin
        count = 0
        while count is not index:
            node = node.next
            count += 1
        if node is None: 
            return None
        return node.value

    def dump(self, mark):
        """Debugging function that dumps the contents of the list."""
        output = []
        node = self.begin
        while node is not None:
            output.append(node.value)
            node = node.next
        print(mark + ": " + str(output))
            
