from ciu.cci.ControleMenu.EstadoMenu import EstadoMenu

__author__ = 'dell'


class EstadoMenuSair(EstadoMenu):

    def __init__(self, menu):
        self.menu = menu

    def proximo_valor(self):
        pass

    def valor_anterior(self):
        self.menu.set_estado(self.menu.estadomenuranking)

    @staticmethod
    def selecionar_valor():
        exit()
