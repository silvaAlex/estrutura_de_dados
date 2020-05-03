from lista_duplamente_encadeada import ListaDuplamenteEncadeada, Node


class Loja:

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __repr__(self):
        return "* {} - {}".format(self.name, self.address)


def situacao(lista):
    print("Quantidade: {}".format(lista.quantity))
    lista.imprimir()


def main():

    loja1 = Loja("Mercadinho", "Rua das Laranjeiras, 12")
    loja2 = Loja("HortiFruti", "Rua do Pomar, 300")
    loja3 = Loja("Padaria", "Rua das Flores, 600")
    loja4 = Loja("Supermecado", "Alameda Santos, 400")
    loja5 = Loja("Mini Mercado", "Rua da Fazenda, 900")
    loja6 = Loja("Quitanda", "Avenida Rio Branco, 34")
    loja7 = Loja("Minimercado das Frutas", "Avenida do Bosque, 66")
    loja8 = Loja("SF", "Avenida Rio Branco, 600")
    loja9 = Loja("Supermercado das Frutas", "Rua do Pomar, 800")
    loja10 = Loja("Hortifruti da Terra", "Rua das Laranjeira, 800")

    lista = ListaDuplamenteEncadeada()

    lista.insert_at_start(loja1)
    lista.insert_at_start(loja2)
    lista.insert_at_start(loja3)
    lista.insert_at_end(loja4)
    lista.insert_at_end(loja5)
    lista.insert_at_end(loja6)
    lista.insert_at_any_position(2, loja7)
    lista.insert_at_any_position(7, loja8)
    lista.insert_at_any_position(0, loja9)
    lista.insert_at_any_position(6, loja10)

    situacao(lista)

    removido = lista.remove_at_start()
    print("Removido do inicio: {}".format(removido))

    situacao(lista)

    removido = lista.remove_at_end()
    print("Removido do fim: {}".format(removido))

    situacao(lista)

    removido = lista.remove_in_any_position(1)
    print("Removido da posição 1: {}".format(removido))

    situacao(lista)

    removido = lista.remove_in_any_position(5)
    print("Removido da posição 5: {}".format(removido))

    situacao(lista)

    removido = lista.remove_in_any_position(0)
    print("Removido da posição 0: {}".format(removido))

    situacao(lista)


main()
