from ciu.cci.ControladorCadastroFrase import ControladorCadastroFrase
from ciu.cci.ControleMenu.EstadoMenu import EstadoMenu

__author__ = 'dell'


class EstadoMenuRanking(EstadoMenu):

    def __init__(self, menu):
        self.menu = menu

    def proximo_valor(self):
        self.menu.set_estado(self.menu.estadomenusair)

    def valor_anterior(self):
        self.menu.set_estado(self.menu.estadomenuiniciar)

    def selecionar_valor(self):
        controladorcadastro = ControladorCadastroFrase()
        controladorcadastro.cadastra_frase()
        #self.menu.aguarda_confirmacao()

