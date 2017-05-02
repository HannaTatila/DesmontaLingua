import pygame

from ciu.cih.TelaMenu import TelaMenu
from cln.cdp.Posicao import Posicao


class ControladorDigitacao:
    TAMANHO_LETRA_DADOS = 24
    TAMANHO_PALAVRA = 50

    def __init__(self, posicaoinicialdados):
        self.telamenu = TelaMenu()
        self.nomecorrente = []
        self.nome = ""
        self.posicaoinicialdados = posicaoinicialdados
        self.posicaoimprimenome = posicaoinicialdados

    def imprime_nome(self, dado, posicaoy):
        self.nome = ""
        for i in range(len(dado)):
            self.nome = self.nome + dado[i]
        self.telamenu.exibe_texto_dados(self.nome, self.TAMANHO_LETRA_DADOS, Posicao(self.objetoX.POSICAOX_LETRA_DADOS, posicaoy))
        pygame.display.flip()

    def atualiza_entrada(self):
        self.objetoX.atualiza_tela_geral()
        posicaoy = self.posicaoinicialdados
        self.imprime_nome(self.nomecorrente, posicaoy)


    def verifica_teclas_digitadas(self, objetoX, teclaclicada):
        self.objetoX = objetoX
        self.tecla = teclaclicada

        if self.tecla == pygame.K_BACKSPACE:
            if len(self.nomecorrente) > 0:
                self.nomecorrente.pop(-1)
                self.atualiza_entrada()
        elif self.tecla <= 127 and len(self.nomecorrente) < self.TAMANHO_PALAVRA:
            self.nomecorrente.append(chr(self.tecla))
            self.imprime_nome(self.nomecorrente, self.posicaoimprimenome)