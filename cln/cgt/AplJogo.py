import pygame
from cln.cdp.Palavra import Palavra


class AplJogo:

    def __init__(self):
        self.clock = ""
        self.qtdrelacaoes = 0

    def configuracao(self):
        self.clock = pygame.time.Clock()

    def captura_frase(self):
        return ["O", "sol", "eh", "amarelo"]

    def captura_relacoes(self):
        return [(0, 1, 0), (1, 2, 0), (3, 2, 0)]

    def captura_relacao_cenario(self):
        return [("100", "img1.png"), ("111", "img2.png")]

    def gera_estrutura_frase(self):
        estrutura = []
        frase = self.captura_frase()
        cont = 0

        for palavra in frase:
            obj = Palavra()
            obj.set_texto(palavra)
            obj.set_id(cont)
            estrutura.append(obj)
            cont += 1

        return estrutura



    def jogar(self):
        pass


