from ciu.cci.ControladorCadastroFrase import ControladorCadastroFrase
from ciu.cci.ControleMenu.EstadoMenu import EstadoMenu
from ciu.cci.ControladorCadastroRelacoes import ControladorCadastroRelacoes
from ciu.cci.ControladorCadastroImagens import ControladorCadastroImagens
from cln.cgt.AplCadastro import AplCadastro

__author__ = 'dell'


class EstadoMenuRanking(EstadoMenu):

    def __init__(self, menu):
        self.menu = menu

    def proximo_valor(self):
        self.menu.set_estado(self.menu.estadomenusair)

    def valor_anterior(self):
        self.menu.set_estado(self.menu.estadomenuiniciar)

    def selecionar_valor(self):
        controladorcadastrofrase = ControladorCadastroFrase()

        frase = controladorcadastrofrase.cadastro_frase()
        if frase != "":
            controladorcadastrorelacoes = ControladorCadastroRelacoes(frase)
            listarelacoes = controladorcadastrorelacoes.cadastro_relacoes()
            if len(listarelacoes) > 0:
                controladorcadastroimagens = ControladorCadastroImagens(frase, listarelacoes)
                listacenariosimagens = controladorcadastroimagens.cadastro_imagens()

                if len(listacenariosimagens) > 0:
                    aplcadastro = AplCadastro()
                    aplcadastro.cadastrar_dados(frase, listarelacoes, listacenariosimagens)



        #self.aplcadastro.cadastrar_dados()
        #self.menu.aguarda_confirmacao()

