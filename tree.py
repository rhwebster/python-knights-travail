class Node:
    def __init__(self, value):
        self._value = value
        self._parent = None
        self._children = []

    @property
    def value(self):
        return self._value

    @property
    def children(self):
        return self._children

    def add_child(self, node):
        if node:
            if node not in self._children:
                self._children.append(node)
                node._parent = self

    def remove_child(self, node):
        if node not in self._children:
            return
        self._children.remove(node)
        node._parent = None


    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        if node:
            self._parent = node
            node.add_child(self)

    
    
