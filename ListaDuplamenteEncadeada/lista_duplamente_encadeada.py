class Node:

    def __init__(self, content):
        self.content = content
        self.next = None
        self.prev = None


class ListaDuplamenteEncadeada:

    def __init__(self):
        self._start = None
        self._end = None
        self._quantity = 0

    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end

    @property
    def quantity(self):
        return self._quantity

    def _insert_at_empty_list(self, content):
        node = Node(content)
        self._start = node
        self._end = node
        self._quantity += 1

    def insert_at_start(self, content):
        if self._quantity == 0:
            return self._insert_at_empty_list(content)
        else:
            node = Node(content)
            node.next = self._start
            self._start.prev = node
            self._start = node
            self._quantity += 1

    def insert_at_end(self, content):
        if self._quantity == 0:
            return self._insert_at_empty_list(content)
        else:
            node = Node(content)
            node.prev = self._end
            self._end.next = node
            self._end = node
            self._quantity += 1

    def insert_at_any_position(self, position, content):
        if position == 0:
            return self.insert_at_start(content)
        if position == self._quantity:
            return self.insert_at_end(content)
        left = self._node(position - 1)
        right = left.next
        node = Node(content)
        node.next = right
        node.prev = left
        left.next = node
        right.prev = node
        self._quantity += 1

    def _remove_last(self):
        if self._quantity == 1:
            removed = self._start
            self._start = None
            self._end = None
            self._quantity -= 1
            return removed.content

    def remove_at_start(self):
        if self._quantity == 1:
            return self._remove_last()
        else:
            removed = self._start
            self._start = removed.next
            self._start.prev = None
            removed.next = None
            self._quantity -= 1
            return removed.content

    def remove_at_end(self):
        if self._quantity == 1:
            return self._remove_last()
        else:
            removed = self._end
            self._end = removed.prev
            self._end.next = None
            removed.prev = None
            self._quantity -= 1
            return removed.content

    def remove_in_any_position(self, position):
        if position == 0:
            return self.remove_at_start()
        if position == self.quantity - 1:
            return self.remove_at_end()
        removed = self._node(position)
        left = removed.prev
        right = removed.next
        removed.next = None
        removed.prev = None
        left.next = right
        right.prev = left
        self._quantity -= 1
        return removed.content

    def item(self, position):
        node = self._node(position)
        return node.content

    def _validate_position(self, position):
        if 0 <= position < self._quantity:
            return True
        raise IndexError("Posição inválida: {}".format(position))

    def _node(self, position):
        self._validate_position(position)
        half = self._quantity // 2
        if position < half:
            current = self._start
            for i in range(0, position):
                current = current.next
            return current
        else:
            current = self._end
            for i in range(position + 1, self._quantity)[::-1]:
                current = current.prev
            return current

    def imprimir(self):
        current = self._start
        for i in range(0, self._quantity):
            print(current.content)
            current = current.next
