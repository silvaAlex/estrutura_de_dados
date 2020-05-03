from fila import Fila


class Pedido:

    def __init__(self, pizza):
        self.pizza = pizza

    def __repr__(self):
        return self.pizza


def main():

    pizzaria = Fila()

    pedido1 = Pedido("A Moda")
    pedido2 = Pedido("Calabresa")
    pedido3 = Pedido("Marguerita")
    pedido4 = Pedido("Peperonni")

    pizzaria.enter(pedido1)
    print("Recebendo pedido: {}".format(pedido1))

    pizzaria.enter(pedido2)
    print("Recebendo pedido: {}".format(pedido2))

    pizzaria.enter(pedido3)
    print("Recebendo pedido: {}".format(pedido3))

    pizzaria.enter(pedido4)
    print("Recebendo pedido: {}".format(pedido4))

    pedido = pizzaria.exit()
    print("Fazendo a pizza de: {}".format(pedido))
    print("Está vazia? {}".format(pizzaria.empty))

    pedido = pizzaria.exit()
    print("Fazendo a pizza de: {}".format(pedido))
    print("Está vazia? {}".format(pizzaria.empty))

    pedido = pizzaria.exit()
    print("Fazendo a pizza de: {}".format(pedido))
    print("Está vazia? {}".format(pizzaria.empty))

    pedido = pizzaria.exit()
    print("Fazendo a pizza de: {}".format(pedido))
    print("Está vazia? {}".format(pizzaria.empty))


main()
