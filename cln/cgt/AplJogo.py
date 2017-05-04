import pygame
from cln.cdp.Palavra import Palavra
from cgd.DAOFrase import DAOFrase


class AplJogo:

    def __init__(self):
        self.clock = ""
        self.qtdrelacaoes = 0
        self.daofrase = DAOFrase()
        self.idfraseselecionada = 1

    def configuracao(self):
        self.clock = pygame.time.Clock()

    def captura_frase(self):
        #TODO: pensar na forma como as frases serao consultadas
        frase = self.daofrase.consultar_frase(self.idfraseselecionada)
        print "Frase consultada no banco:"
        print frase[0]
        #frase = "O sol eh amarelo"
        estrutura = self.gera_estrutura_frase(frase[0])

        return estrutura

    def gera_estrutura_frase(self, frase):
        listapalavras = frase.split()
        estrutura = []
        valorid = 0

        for palavra in listapalavras:
            obj = Palavra()
            obj.set_texto(palavra)
            obj.set_id(valorid)
            estrutura.append(obj)
            valorid += 1

        return estrutura

    def captura_relacoes(self):
        relacoes = self.daofrase.consultar_relacoes(self.idfraseselecionada)

        for id in range(len(relacoes)):
            novatupla = relacoes[id] + (0,)
            relacoes[id] = novatupla

        print "Relacoes consultadas no banco: "
        print relacoes
        return relacoes
        #return [(0, 1, 0), (1, 2, 0), (3, 2, 0)]

    def captura_relacao_cenario(self):
        cenarios = self.daofrase.consultar_cenarios(self.idfraseselecionada)
        print "Cenarios consultados no banco: "
        print cenarios

        return cenarios
        #return [("100", "img1.png"), ("111", "img2.png")]



    def jogar(self):
        pass


