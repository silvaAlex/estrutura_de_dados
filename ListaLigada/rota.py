from lista_ligada import ListaLigada, Cell


class Loja:

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __repr__(self):
        return "{}\n {}".format(self.name, self.address)


def main():

    loja1 = Loja("Mercadinho", "Rua das Laranjeiras, 12")
    loja2 = Loja("HortiFruti", "Rua do Pomar, 300")
    loja3 = Loja("Padaria", "Rua das Floes, 600")
    loja4 = Loja("Supermecado", "Alameda Santos, 400")
    loja5 = Loja("Mini Mercado", "Rua da Fazenda, 900")
    loja6 = Loja("Quitanda", "Avenida Rio Branco, 34")

    lista = ListaLigada()

    lista.insert_at_start(loja1)
    lista.insert_at_start(loja2)
    lista.insert_at_start(loja3)
    lista.insert_at_start(loja4)
    lista.insert_at_start(loja5)
    lista.insert_at_start(loja6)
    lista.insert_at_any_position(1, loja2)

    print("======== Inserções ========\n")
    lista.imprimir()
    print("\nQuantidade de itens: ", end="")
    print(lista.quantity)

    print("\n\n======== Remoções no início ========\n")
    removido = lista.remove_at_start()
    print("Removido: {}".format(removido))
    removido = lista.remove_at_start()
    print("Removido: {}".format(removido))
    print("\nQuantidade de itens: ", end="")
    print(lista.quantity)

    print("\n\n======== Remoções em qualquer posição ========\n")

    removido = lista.remove_at_any_position(2)
    print("Removido da posicao 2: {}".format(removido))
    removido = lista.remove_at_any_position(0)
    print("Removido da posicao 0: {}".format(removido))

    print("\n\n======== Lista Resultante ========\n")
    lista.imprimir()
    print("\nQuantidade de itens: ", end="")
    print(lista.quantity)

    print("\n\n========Printando na posição específica ========\n")
    print(lista.item(0))


main()
