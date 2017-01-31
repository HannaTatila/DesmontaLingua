import sys

import pygame
#from pygame.constants import KEYDOWN, K_RETURN, QUIT

from ciu.cci.ControleMenu.EstadoMenuIniciar import EstadoMenuIniciar
from ciu.cci.ControleMenu.EstadoMenuRanking import EstadoMenuRanking
from ciu.cci.ControleMenu.EstadoMenuSair import EstadoMenuSair

__author__ = 'Hanna'

class Menu():

    def __init__(self):
        self.estadomenuiniciar = EstadoMenuIniciar(self)
        self.estadomenuranking = EstadoMenuRanking(self)
        self.estadomenusair = EstadoMenuSair(self)
        self.set_estado(self.estadomenuiniciar)

    def set_estado(self, estado):
        self.estadocorrente = estado

    def alterar_opcao_menu_baixo(self):
        self.estadocorrente.proximo_valor()

    def alterar_opcao_menu_cima(self):
        self.estadocorrente.valor_anterior()

    def selecionar_opcao_menu(self):
        self.estadocorrente.selecionar_valor()

    @staticmethod
    def aguarda_confirmacao():
        espera = True
        while espera:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if (e.type == pygame.KEYDOWN) and (e.key == pygame.K_RETURN):
                    espera = False
