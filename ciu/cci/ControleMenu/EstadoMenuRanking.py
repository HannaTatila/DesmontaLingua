from ciu.cci.ControladorCadastroFrase import ControladorCadastroFrase
from ciu.cci.ControleMenu.EstadoMenu import EstadoMenu
from ciu.cci.ControladorCadastroRelacoes import ControladorCadastroRelacoes

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

        controladorcadastrofrase.exibe_tela_cadastro_frase()
        frase = controladorcadastrofrase.cadastro_frase()
        if frase != "":
            controladorcadastrorelacoes = ControladorCadastroRelacoes(frase)
            listarelacoes = controladorcadastrorelacoes.cadastro_relacoes()
            print "RETORNO: "
            print frase
            print listarelacoes
            #if len(listarelacoes) > 0:
            #    controladorcadastroimagens = ControladorCadastroImagens()

        else:
            pass
            #volta ao menu


        #self.aplcadastro.cadastrar_dados()
        #self.menu.aguarda_confirmacao()

