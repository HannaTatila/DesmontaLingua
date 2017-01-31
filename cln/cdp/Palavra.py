import pygame

class Palavra:

    def __init__(self):
        self.id = 0
        self.texto = ""
        self.ativo = False
        self.imagemrect = ""

    def set_texto(self, palavra):
        self.texto = palavra

    def set_ativo(self, ativo):
        self.ativo = ativo

    def set_imagemrect(self, img):
        self.imagemrect = img

    def set_id(self, id):
        self.id = id

    def is_clicked(self):
        return pygame.mouse.get_pressed()[0] and self.imagemrect.collidepoint(pygame.mouse.get_pos())
