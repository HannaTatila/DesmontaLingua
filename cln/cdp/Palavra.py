import pygame

class Palavra:

    def __init__(self):
        self.id = 0
        self.texto = ""
        self.imagemrect = ""
        self.posicaoxbotao = 0
        self.ativo = False

    def set_texto(self, palavra):
        self.texto = palavra

    def set_imagemrect(self, img):
        self.imagemrect = img

    def set_id(self, id):
        self.id = id

    def foi_clicada(self):
        return pygame.mouse.get_pressed()[0] and self.imagemrect.collidepoint(pygame.mouse.get_pos())

    def foi_detectada(self):
        return pygame.MOUSEBUTTONUP and self.imagemrect.collidepoint(pygame.mouse.get_pos())
