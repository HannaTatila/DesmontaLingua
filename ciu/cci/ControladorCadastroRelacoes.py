import pygame
import sys

from ciu.cci.ControladorJogo import ControladorJogo
from pygame.constants import QUIT
from cln.cdp.Posicao import Posicao
#from cln.cgt.AplSuporteSintaxe import AplSuporteSintaxe


class ControladorCadastroRelacoes(ControladorJogo):
    POSICAOX_BOTAO_CADASTRAR_FRASE = 350
    POSICAOY_BOTAO_CADASTRAR_FRASE = 400

    def __init__(self, frase):
        ControladorJogo.__init__(self)
        self.frase = frase
        self.renderizar_fundo()
        self.posicaoy = (self.telajogo.tamanhotelay / 3)
        self.listarelacoes = []

    def renderizar_fundo(self):
        self.telajogo.telajogo.fill((255, 255, 255))

    def criar_botao_cadastrar(self):
        botao = self.get_imagem("btrelacoes.png")
        self.telajogo.exibe_imagem(botao, Posicao(self.POSICAOX_BOTAO_CADASTRAR_FRASE, self.POSICAOY_BOTAO_CADASTRAR_FRASE))
        self.imagemrectbotaocadastrar = botao.get_rect().move(self.POSICAOX_BOTAO_CADASTRAR_FRASE, self.POSICAOY_BOTAO_CADASTRAR_FRASE)

    def verifica_seta_repetida(self, relacao):
        setajaexiste = False
        for seta in self.listasetas:
            if seta.tuplarelacao == relacao:
                self.listasetas.remove(seta)
                self.listarelacoes.remove(relacao)
                self.renderizar_fundo()
                self.exibir_botoes_palavras()
                setajaexiste = True
                return setajaexiste

        return setajaexiste

    def manipula_seta_relacao(self, idorigem, iddestino):
        relacao = (idorigem, iddestino)
        wsize = abs(self.objpalavras[iddestino].posicaoxbotao - self.objpalavras[idorigem].posicaoxbotao)
        posicaosaidaseta = idorigem
        issequencial = iddestino > idorigem
        if not issequencial:
            posicaosaidaseta = iddestino

        setajaexiste = self.verifica_seta_repetida(relacao)

        if not setajaexiste:
            self.listarelacoes.append(relacao)
            self.incrementa_lista_setas(wsize, self.objpalavras[posicaosaidaseta].posicaoxbotao, issequencial, relacao)


    def verifica_evento_mouse(self):
        for palavraobj in self.objpalavras:
            self.controla_cor_botao_visitado(palavraobj)

            if palavraobj.foi_clicada():
                if not (self.existepalavraclicada):
                    self.idpalavraorigem = palavraobj.id
                    self.existepalavraclicada = True
                    self.destacar_botao_clicado(self.idpalavraorigem)
                else:
                    self.existepalavraclicada = False
                    self.restaurar_botao(self.idpalavraorigem)
                    if self.idpalavraorigem != palavraobj.id:
                        self.manipula_seta_relacao(self.idpalavraorigem, palavraobj.id)
                    self.idpalavraorigem = -1

    def exibe_lista_setas(self):
        for seta in self.listasetas:
            self.exibir_seta_relacao(seta.largura, seta.posicaox, seta.direcaonormal)

    def cadastro_relacoes(self):
        self.apljogo.configuracao()
        self.objpalavras = self.apljogo.gera_estrutura_frase(self.frase)
        self.exibir_botoes_palavras()

        #ctrlsuportesintaxe = AplSuporteSintaxe()

        self.existepalavraclicada = False
        continua = True
        while continua:
            self.criar_botao_cadastrar()
            self.verifica_evento_mouse()
            self.exibe_lista_setas()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if pygame.mouse.get_pressed()[0] and self.imagemrectbotaocadastrar.collidepoint(pygame.mouse.get_pos()):
                return self.listarelacoes

            pygame.display.flip()
            self.apljogo.clock.tick(10)