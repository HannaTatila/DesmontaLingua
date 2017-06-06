import os

import pygame
import sys

from ciu.cci.ControladorJogo import ControladorJogo
from ciu.cih.Tela import Tela
from cln.cdp.Posicao import Posicao
from cln.cgt.AplJogo import AplJogo
from principal.CaminhoRecursos import CaminhoRecursos


class ControladorDefineSintagma (ControladorJogo):
    POSICAOX_BOTAO_CADASTRAR_SINTAGMAS = 350
    POSICAOY_BOTAO_CADASTRAR_SINTAGMAS = 400
    POSICAOX_BOTAO_MARCAR_SINTAGMA = 50
    POSICAOY_BOTAO_MARCAR_SINTAGMA = 250
    POSICAOX_BOTAO_CADASTRAR_SINTAGMAS = 350
    POSICAOY_BOTAO_CADASTRAR_SINTAGMAS = 450
    POSICAOX_CLASSE_GRAMATICAL = 250
    POSICAOY_CLASSE_GRAMATICAL = 250
    INCREMENTO_POSICAOY_CLASSE_GRAMATICAL = 80


    def __init__(self, frase):
        ControladorJogo.__init__(self)
        self.apljogo = AplJogo()
        self.telajogo = Tela()
        self.frase = frase
        self.posicaoy = (self.telajogo.tamanhotelay / 4)
        self.listarelacoes = []


    def inicializa_tela(self):
        self.renderizar_fundo()
        self.exibir_botoes_palavras()

    def renderizar_fundo(self):
        self.telajogo.telajogo.fill((255, 255, 255))

    def gerar_botao(self, nomeimagem, posicaoxbotao, posicaoybotao):
        botao = self.get_imagem(nomeimagem)
        botaorect = botao.get_rect().move(posicaoxbotao, posicaoybotao)
        return botao, botaorect

    def imprimir_imagem_botao(self, botao, posicaox, posicaoy):
        self.telajogo.exibe_imagem(botao, Posicao(posicaox, posicaoy))

    def imprimir_botao_classes(self, classe, botao, posicaox, posicaoy):
        self.telajogo.exibe_imagem(botao, Posicao(posicaox, posicaoy))
        self.telajogo.exibe_texto(classe, self.TAM_FONTE_TEXTO,
                                  Posicao(posicaox + 10, posicaoy + 10))

    def imprimir_classes_gramaticais(self):
        self.listaclasses = ["Substantivo", "Verbo", "Adverbio", "Adjetivo", "Pronome Adjetivo", "Numeral", "Artigo"]
        self.listarectclasses = []

        posicaoy = self.POSICAOY_CLASSE_GRAMATICAL
        posicaox = self.POSICAOX_CLASSE_GRAMATICAL
        cont = 0
        for classe in self.listaclasses:
            largura = self.calcula_largura_botao(classe)
            botao = self.cria_botao(classe, (220,220,220)) #definir a melhor cor
            imagemrectbotao = botao.get_rect().move(posicaox, posicaoy)
            self.listarectclasses.append(imagemrectbotao)
            self.imprimir_botao_classes(classe, botao, posicaox, posicaoy)
            posicaox += largura + 10

            cont += 1
            if cont == 4:
                posicaoy = posicaoy + self.INCREMENTO_POSICAOY_CLASSE_GRAMATICAL
                posicaox = self.POSICAOX_CLASSE_GRAMATICAL
                cont = 0

        pygame.display.flip()

    def verificar_escolha_classe_gramatical(self):
        while True:
            for idrectclasse in range(len(self.listarectclasses)):
                if pygame.mouse.get_pressed()[0] and self.listarectclasses[idrectclasse].collidepoint(pygame.mouse.get_pos()):
                    return idrectclasse

            self.verifica_evento_finalizar()


    def verifica_evento_mouse(self):
        for palavraobj in self.objpalavras:
            self.controla_cor_botao_visitado(palavraobj)

            if palavraobj.foi_clicada():
                if palavraobj.id not in self.listapalavrasclicadas:
                    palavraobj.ativo = True
                    self.listapalavrasclicadas.append(palavraobj.id)
                    self.destacar_botao_clicado(palavraobj.id)
                else:
                    palavraobj.ativo = False
                    self.listapalavrasclicadas.remove(palavraobj.id)
                    self.restaurar_botao(palavraobj.id)

    def verifica_evento_finalizar(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def verifica_sintagma_existente(self):
        for tuplasintagmaclasse in self.listaretornosintagmasclasses:
            if tuplasintagmaclasse[0] == self.listapalavrasclicadas:
                return True
        return False

    def define_sintagmas(self):
        self.apljogo.configuracao()
        self.objpalavras = self.apljogo.gera_estrutura_frase(self.frase)
        self.inicializa_tela()

        self.botaodefinirsintagma, self.imagemrectbotaodefinirsintagma = self.gerar_botao("btmarcarcenario.png", self.POSICAOX_BOTAO_MARCAR_SINTAGMA, self.POSICAOY_BOTAO_MARCAR_SINTAGMA)
        self.botaocadastrar, self.imagemrectbotaocadastrar = self.gerar_botao("btimagens.png", self.POSICAOX_BOTAO_CADASTRAR_SINTAGMAS, self.POSICAOY_BOTAO_CADASTRAR_SINTAGMAS)

        self.listaretornosintagmasclasses = []
        self.listapalavrasclicadas = []
        continua = True
        while continua:
            self.imprimir_imagem_botao(self.botaodefinirsintagma, self.POSICAOX_BOTAO_MARCAR_SINTAGMA, self.POSICAOY_BOTAO_MARCAR_SINTAGMA)
            self.imprimir_imagem_botao(self.botaocadastrar, self.POSICAOX_BOTAO_CADASTRAR_SINTAGMAS, self.POSICAOY_BOTAO_CADASTRAR_SINTAGMAS)
            self.verifica_evento_mouse()
            self.verifica_evento_finalizar()

            if pygame.mouse.get_pressed()[0] and self.imagemrectbotaodefinirsintagma.collidepoint(pygame.mouse.get_pos()):
                self.listapalavrasclicadas.sort()

                if not self.verifica_sintagma_existente():
                    self.imprimir_classes_gramaticais()
                    idclasse = self.verificar_escolha_classe_gramatical()

                    tuplasintagmaclasse = (self.listapalavrasclicadas, self.listaclasses[idclasse])
                    self.listaretornosintagmasclasses.append(tuplasintagmaclasse)
                    self.telajogo.exibe_som(self.get_som("acerto.wav"))
                else:
                    self.telajogo.exibe_som(self.get_som("erro.wav"))

                self.listapalavrasclicadas = []
                self.inicializa_tela()

            if pygame.mouse.get_pressed()[0] and self.imagemrectbotaocadastrar.collidepoint(pygame.mouse.get_pos()):
                return self.listaretornosintagmasclasses

            pygame.display.flip()
            self.apljogo.clock.tick(10)