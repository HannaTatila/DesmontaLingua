import pygame
from pygame.constants import QUIT
import sys

__author__ = 'Hanna'

class ObservableEventosTeclado:
    def __init__(self):
        self.observers = []
        self.enter = False
        self.baixo = False
        self.cima = False
        self.soltoubaixo = False
        self.direita = False
        self.esquerda = False
        self.clicou = False

    def add_observer(self, observer):
        self.observers.append(observer)

    def notifica_observador(self):
        for observer in self.observers:
            observer.update(self)

    def verifica_evento(self):
        self.inicializa_variaveis()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    exit()
                elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    self.enter = True
                elif event.key == pygame.K_UP:
                    self.cima = True
                elif event.key == pygame.K_DOWN:
                    self.baixo = True
                elif event.key == pygame.K_RIGHT:
                    self.direita = True
                elif event.key == pygame.K_LEFT:
                    self.esquerda = True
            elif (event.type == pygame.KEYUP) and (event.key == pygame.K_UP):
                    self.soltoubaixo = True
        if pygame.mouse.get_pressed()[0]:
            self.clicou = True
        self.notifica_observador()

    def inicializa_variaveis(self):
        self.enter = False
        self.baixo = False
        self.cima = False
        self.soltoubaixo = False
        self.direita = False
        self.esquerda = False
        self.clicou = False