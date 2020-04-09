class Node(object):
    def __init__(self, value, prev, nxt):
        self.value = value
        self.prev = prev
        self.next = nxt
        def __repr__(self):
            pval = self.prev and self.prev.value or None
            nval = self.next and self.next.value or None
            return f"[{self.value}, {repr(nval)}, {repr(pval)}]"

class DoubleLinkedList(object):
    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, obj):
        """Appends a new value on the end of the list."""
        node = self.begin
        if node is None:
            node = Node(obj, None, None)
            self.begin = node
            self.end = node
        else:
            while node.next is not None:
                node = node.next
            node.next = self.end = Node(obj, node, None)

    def pop(self):
        """Removes the last item and returns it."""
        deleted_node = self.end
        if self.end is not None and self.end.prev is not None:
            self.end = self.end.prev
            self.end.next = None
        elif self.end == self.begin:
            self.begin = self.end = None
        if deleted_node is None:
            return None
        return deleted_node.value
    
    def shift(self, obj):
        """Inserts item into beginning of the list."""
        self.begin = Node(obj,None,self.begin)
        if self.end is None:
            self.end = self.begin

    def unshift(self):
        """Removes the first item (from begin) and returns it."""
        deleted_node = self.begin
        if self.begin is None:
            return None
        else:
            self.begin = self.begin.next
            if self.begin is not None:
                self.begin.prev = None
            return deleted_node.value

    def detach_node(self,node):
        """You'll need to use this operation sometimes inside remove(),
        but mostly it should take a node and detach it from the list, 
        whether the node is at the front, end, or in the middle."""
        iter_node = self.begin
        while iter_node is not None:
            if iter_node.value == node.value:
                if iter_node.prev is None:
                    self.begin = node.next
                    if self.begin is not None:
                        self.begin.prev = None
                    break
                else: 
                    iter_node.prev.next = node.next
                    break
                
            iter_node = iter_node.next

    def remove(self, obj):
        """Finds a matching item and removes it from the list."""
        node = self.begin
        index = 0
        while node is not None:
            if node.value == obj:
                self.detach_node(node)
                break
            index += 1
            node = node.next
        return index
    
    def first(self):
        """Returns a *reference* to the first item, does not remove."""
        if self.begin is None:
            return None
        else:
            return self.begin.value
    
    def last(self):
        """Returns a reference to the last item, does not remove."""
        if self.end is None:
            return None
        else:
            return self.end.value
    
    def count(self):
        """Counts the number of elements in the list.""" 
        count = 0
        node = self.begin
        while node is not None:
            node = node.next
            count += 1 
        return count
    
    def get(self, index):
        """Get the value at index."""
        node = self.begin
        iter = 0
        
        while node is not None:
            if iter == index:
                return node.value
            iter+=1
            node = node.next
        
        return None

    def dump(self, mark):
        """Debugging function that dumps the contents of the list."""
        output = []
        node = self.begin
        while node is not None:
            output.append(node.value)
            node = node.next
        print(mark + ": " + str(output))
