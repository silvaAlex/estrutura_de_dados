from arvore import Tree


def main():
    livraria = Tree('Livros')
    livraria.root.insert_child('Hqs')
    livraria.root.insert_child('Informática')

    livraria.imprimir()

    found = livraria.find_node('Livros')

    print("Encontrado: {}".format(found))
    found = livraria.find_node("Hqs")
    print("Encontrado: {}".format(found))
    found = livraria.find_node("Informática")
    print("Encontrado: {}".format(found))

    found = livraria.find_node("Turismo")
    print("Encontrado: {}".format(found))

    livraria.insert_node("Informática", "Linguagens")
    livraria.insert_node("Linguagens", "Python")
    livraria.insert_node("Hqs", "Guerras Secretas")
    livraria.insert_node("Hqs", "Inumanos")
    livraria.insert_node("Hqs", "Camelot 3000")
    livraria.insert_node("Hqs", "Electra")
    livraria.imprimir()

    removed = livraria.remove_node("Camelot 3000")
    print("Removido: {}".format(removed))
    livraria.imprimir()

    removed = livraria.remove_node("Informática")
    print("Removido:")
    removed.imprimir()
    print("Ainda na Livraria:")
    livraria.imprimir()


main()
