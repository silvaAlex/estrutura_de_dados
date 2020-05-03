from ListaDuplamenteEncadeada.lista_duplamente_encadeada import ListaDuplamenteEncadeada


class Fila:

    def __init__(self):
        self.fila = ListaDuplamenteEncadeada()

    def enter(self, conteudo):
        self.fila.insert_at_end(conteudo)

    def exit(self):
        return self.fila.remove_at_start()

    @property
    def empty(self):
        return self.fila.quantity == 0
