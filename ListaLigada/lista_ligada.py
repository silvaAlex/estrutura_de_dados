class Cell:
    def __init__(self, content):
        self.content = content
        self.next = None


class ListaLigada:
    def __init__(self):
        self._start = None
        self._quantity = 0

    @property
    def start(self):
        return self._start

    @property
    def quantity(self):
        return self._quantity

    def insert_at_start(self, content):
        cell = Cell(content)
        cell.next = self._start
        self._start = cell
        self._quantity += 1

    def insert_at_any_position(self, position, content):
        if position == 0:  # Se for a primeira posição, ou seja, a lista está vazia
            self.insert_at_start(content)
            return
        else:
            cell = Cell(content)
            left = self._cell(position - 1)
            cell.next = left.next
            left.next = cell
            self._quantity += 1

    def _cell(self, position):
        self._validate_position(position)
        current = self._start
        for i in range(0, position):
            current = current.next
        return current

    def _validate_position(self, position):
        if 0 <= position < self._quantity:
            return True
        else:
            raise IndexError("Posição inválida {}". format(position))

    def remove_at_start(self):
        removed = self._start
        self._start = removed.next
        removed.next = None
        self._quantity -= 1
        return removed.content

    def remove_at_any_position(self, position):
        if position == 0:
            return self.remove_at_start()
        else:
            left = self._cell(position - 1)
            removed = left.next
            left.next = removed.next
            removed.next = None
            self._quantity -= 1
            return removed.content

    def item(self, position):
        self._validate_position(position)
        cell = self._cell(position)
        return cell.content

    def imprimir(self):
        current = self.start
        for i in range(self._quantity):
            print(current.content)
            current = current.next
