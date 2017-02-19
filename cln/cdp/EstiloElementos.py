from random import randint

from cln.cdp.Posicao import Posicao

_author__ = 'Hanna e Neimar'


class EstiloElementos:
    @staticmethod
    def posicao_personagem():
        return Posicao(150, 250)

    @staticmethod
    def posicao_inimigo():
        return Posicao(700, randint(0, 445))

    @staticmethod
    def posicao_imagem_fundo():
        return Posicao(0, 0)

    @staticmethod
    def posicao_texto_pontuacao():
        return Posicao(290, 50)

    @staticmethod
    def posicao_numero_pontuacao():
        return Posicao(345, 20)

    @staticmethod
    def posicao_texto_vida():
        return Posicao(10, 50)

    @staticmethod
    def posicao_desenho_moeda():
        return Posicao(560, 11)

    @staticmethod
    def posicao_texto_bonus():
        return Posicao(595,50)

    @staticmethod
    def posicao_numero_bonus():
        return Posicao(600, 15)

    @staticmethod
    def posicao_tela_gameover():
        return Posicao(80, 100)

    @staticmethod
    def posicao_mensagem_gameover():
        return Posicao(150, 245)

    @staticmethod
    def posicao_mensagem():
        return Posicao(250, 50)

    @staticmethod
    def get_posicao_vida(numvida):
        return Posicao(numvida * 36, 3)

    @staticmethod
    def posicao_titulo_jogo():
        return Posicao(250, 30)

    @staticmethod
    def posicao_mensagem_cadastro():
        return Posicao(200, 22)
