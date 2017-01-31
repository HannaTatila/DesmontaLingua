import os
import pygame
from ciu.cih.Tela import Tela

_author__ = 'Hanna'


class TelaMenu(Tela):
    COR_CINZA = (80, 80, 80)
    TAMANHO_FONTE_MENSAGEM = 30

    def __init__(self):
        super(TelaMenu, self).__init__()

    def exibe_texto_menu(self, texto, tam, cor, posicao):
        fonte = pygame.font.SysFont("Agency FB", tam, False, False)
        t = fonte.render(texto, True, cor)
        self.telajogo.blit(t, (posicao.eixox, posicao.eixoy))

    def exibe_texto_dados(self, texto, tam, posicao):
        fonte = pygame.font.SysFont("Arial", tam, False, False)
        t = fonte.render(texto, True, self.preto)
        self.telajogo.blit(t, (posicao.eixox, posicao.eixoy))

    def exibe_mensagem_cadastro(self, texto, posicao):
        fonte = pygame.font.SysFont("Agency FB", self.TAMANHO_FONTE_MENSAGEM, False, False)
        t = fonte.render(texto, True, self.COR_CINZA)
        self.telajogo.blit(t, (posicao.eixox, (self.tamanhotelay / 2) + posicao.eixoy))
