from ciu.cci.ControladorJogo import ControladorJogo
from ciu.cci.ControleMenu.EstadoMenu import EstadoMenu

__author__ = 'Hanna'


class EstadoMenuIniciar(EstadoMenu):

    def __init__(self, menu):
        self.menu = menu

    def proximo_valor(self):
        self.menu.set_estado(self.menu.estadomenuranking)

    def valor_anterior(self):
        pass

    def selecionar_valor(self):
        controladorjogo = ControladorJogo()

        controladorjogo.jogo()
