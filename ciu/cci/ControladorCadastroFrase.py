import os
import pygame
from pygame.constants import QUIT
import sys
from pygame.constants import KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE, K_TAB, QUIT

from ciu.cci.ControladorDigitacao import ControladorDigitacao
from cln.cgt.AplCadastro import AplCadastro
from ciu.cih.TelaMenu import TelaMenu
from cln.cdp.EstiloElementos import EstiloElementos
from cln.cdp.Posicao import Posicao
from principal.CaminhoRecursos import CaminhoRecursos
from ciu.cih.EventosTeclado import ObservableEventosTeclado

_author__ = 'Hanna'


class ControladorCadastroFrase:
    POSICAO_INICIAL_DADOS = 190
    POSICAOX_LETRA_DADOS = 100
    INCREMENTA_ESPACAMENTO = 40
    COR_VERDE = (60, 179, 113)
    TEXTO_BOTAO_CADASTRO_FRASE = "CADASTRAR"
    POSICAOX_BOTAO_CADASTRAR_FRASE = 350
    POSICAOY_BOTAO_CADASTRAR_FRASE = 400
    TAM_FONTE_TEXTO = 35
    TAM_MARGEM_BOTAO = 40

    def __init__(self):
        self.aplcadastro = AplCadastro()
        self.telamenu = TelaMenu()
        self.lopcoes = ["LOGIN:", "SENHA:"]
        self.finalizarcadastro = False

    @staticmethod
    def get_imagem(nomeimagem):
        return pygame.image.load(os.path.join(CaminhoRecursos.caminho_imagens(), nomeimagem))

    def exibe_tela_cadastro_frase(self):
        imagem = self.get_imagem("cadastrafrase.png")
        self.telamenu.exibe_imagem(imagem, EstiloElementos.posicao_imagem_fundo())
        self.criar_botao_cadastrar()
        self.exibir_botao_voltar_menu()
        pygame.display.flip()

    def imprimir_botao(self, botao):
        self.telamenu.exibe_imagem(botao, Posicao(self.POSICAOX_BOTAO_CADASTRAR_FRASE, self.POSICAOY_BOTAO_CADASTRAR_FRASE))
        self.telamenu.exibe_texto(self.TEXTO_BOTAO_CADASTRO_FRASE, self.TAM_FONTE_TEXTO,
                                  Posicao(self.POSICAOX_BOTAO_CADASTRAR_FRASE + 10, self.POSICAOY_BOTAO_CADASTRAR_FRASE + 10))

    def criar_botao_cadastrar(self):
        botao = self.get_imagem("btfrase.png")
        self.telamenu.exibe_imagem(botao, Posicao(self.POSICAOX_BOTAO_CADASTRAR_FRASE, self.POSICAOY_BOTAO_CADASTRAR_FRASE))
        self.imagemrectbotaocadastrar = botao.get_rect().move(self.POSICAOX_BOTAO_CADASTRAR_FRASE, self.POSICAOY_BOTAO_CADASTRAR_FRASE)

    def exibir_botao_voltar_menu(self):
        botao = self.get_imagem("voltar.png")
        self.telamenu.exibe_imagem(botao, Posicao(15, 15))
        self.rectbotaovoltar = botao.get_rect().move(15, 15)

    def atualiza_tela_geral(self):
        self.exibe_tela_cadastro_frase()

    def get_key(self):
        while True:
            event = pygame.event.poll()
            if event.type == KEYDOWN:
                return event.key

            if pygame.mouse.get_pressed()[0]:
                if self.imagemrectbotaocadastrar.collidepoint(pygame.mouse.get_pos()):
                    self.finalizarcadastro = True
                    break
                elif self.rectbotaovoltar.collidepoint(pygame.mouse.get_pos()):
                    self.finalizarcadastro = True
                    self.controladorDigitacao.nome = ""
                    break

    def cadastro_frase(self):
        self.controladorDigitacao = ControladorDigitacao(self.POSICAO_INICIAL_DADOS)
        self.exibe_tela_cadastro_frase()

        while True:
            self.exibir_botao_voltar_menu()
            teclaclicada = self.get_key()

            if self.finalizarcadastro:
                return self.controladorDigitacao.nome

            self.controladorDigitacao.verifica_teclas_digitadas(self, teclaclicada)


