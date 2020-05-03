from pilha import Pilha


class Fase:

    def __init__(self, scenario, scores, punishment):
        self.scenario = scenario
        self.scores = scores
        self.punishment = punishment

    def __repr__(self):
        return self.scenario


def main():
    fases = Pilha()
    fase1 = Fase("Floresta", 300, -100)
    fase2 = Fase("Caverna", 400, -50)
    fase3 = Fase("Vulcão", 300, -4)
    fase4 = Fase("Montanha", 3000, -400)

    fases.empilha(fase1)
    fases.empilha(fase2)
    fases.empilha(fase3)
    fases.empilha(fase4)

    falhou = fases.desempilha()
    print("Falhou na fase: ")
    print(falhou)
    print("Voltou para a fase:")
    print(fases.ver_topo)

    falhou = fases.desempilha()
    print("Falhou na fase: ")
    print(falhou)
    print("Voltou para a fase:")
    print(fases.ver_topo)


main()
