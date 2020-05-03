from estrutura_de_dados.ListaLigada.lista_ligada import ListaLigada


class Pilha:

    def __init__(self):
        self.pilha = ListaLigada()

    def empilha(self, content):
        self.pilha.insert_at_start(content)

    def desempilha(self):
        return self.pilha.remove_at_start()

    @property
    def ver_topo(self):
        return self.pilha.item(0)

    @property
    def pilha_vazia(self):
        return self.pilha.quantity == 0
