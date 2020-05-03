from ListaDuplamenteEncadeada.lista_duplamente_encadeada import ListaDuplamenteEncadeada


class ListNodes(ListaDuplamenteEncadeada):
    def __init__(self):
        super().__init__()

    def imprimir(self, level):
        current = self._start
        for i in range(0, self._quantity):
            current.content.imprimir(level)
            current = current.next

    def find_node(self, content):
        current = self._start
        for i in range(0, self._quantity):
            found = current.content.find_node(content)
            if found:
                return found
            current = current.next

    def position(self, content):
        current = self._start
        for i in range(0, self._quantity):
            if current.content.content == content:
                return i
            current = current.next


class Node:
    def __init__(self, content):
        self.content = content
        self.parent = None
        self.children = None

    def __repr__(self):
        return self.content

    def imprimir(self, level=0):
        print("{} - {}".format(" "*level, self.content))
        if self.children:
            self.children.imprimir(level + 1)

    def insert_child(self, child):
        if self.children is None:
            self.children = ListNodes()
        node = Node(child)
        node.parent = self
        self.children.insert_at_end(node)

    def find_node(self, content):
        if self.content == content:
            return self
        if self.children:
            return self.children.find_node(content)

    def remove(self):
        if self.parent:
            position = self.parent.children.position(self.content)
            return self.parent.children.remove_in_any_position(position)
        return self


class Tree:

    def __init__(self, content):
        self.root = Node(content)

    def imprimir(self):
        self.root.imprimir()

    def find_node(self, content):
        return self.root.find_node(content)

    def insert_node(self, parent, child):
        node_parent = self.find_node(parent)
        if node_parent:
            node_parent.insert_child(child)

    def remove_node(self, content):
        found = self.root.find_node(content)
        if found:
            if found is self.root:
                self.root = None
            else:
                found.remove()
        return found
