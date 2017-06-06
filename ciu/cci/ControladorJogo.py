import os
import pygame
import sys
import unicodedata
from ciu.cih.EventosTeclado import ObservableEventosTeclado
from ciu.cih.Tela import Tela
from cln.cgt.AplJogo import AplJogo
from principal.CaminhoRecursos import CaminhoRecursos
from cln.cdp.Posicao import Posicao
from cln.cdp.Seta import Seta
from cln.cdp.Palavra import Palavra


__author__ = 'Hanna'

reload(sys)
sys.setdefaultencoding("utf-8")


class ControladorJogo:

    TAM_FONTE_TEXTO = 35
    TAM_MARGEM_BOTAO = 40

    def __init__(self):
        self.apljogo = AplJogo()
        self.telajogo = Tela()
        self.music = True
        self.posicaobotaorelacoes = 0
        self.idpalavraorigem = -1
        self.posicaoy = (self.telajogo.tamanhotelay / 5 * 4)
        self.listasetas = []

    @staticmethod
    def get_imagem(nomeimagem):
        return pygame.image.load(os.path.join(CaminhoRecursos.caminho_imagens(), nomeimagem))

    @staticmethod
    def get_musica(nomemusica):
        return os.path.join(CaminhoRecursos.caminho_musicas(), nomemusica)

    @staticmethod
    def get_som(nomesom):
        return os.path.join(CaminhoRecursos.caminho_sons(), nomesom)

    def exibir_musica(self, musica):
        self.telajogo.exibe_musica(CaminhoRecursos.caminho_musicas(), musica)

    def redimensionar_imagem(self, wsize):
        hsize = 75
        img = self.get_imagem("relacao.png")
        img = pygame.transform.scale(img, (wsize + 30, hsize))
        return img

    def exibir_seta_relacao(self, wsize, posicaox, direcaonormal):
        pygameImage = self.redimensionar_imagem(wsize)

        if not direcaonormal:
            pygameImage = pygame.transform.flip(pygameImage, True, False)

        self.telajogo.exibe_imagem(pygameImage, Posicao(posicaox, self.posicaoy - 60))

    def exibir_botao_voltar_menu(self):
        botao = self.get_imagem("voltar.png")
        self.telajogo.exibe_imagem(botao, Posicao(15, 15))
        self.rectbotaovoltar = botao.get_rect().move(15, 15)

    def calcula_largura_botao(self, palavra):
        tamanhopalavra = len(palavra)
        largura = (tamanhopalavra * 10) + self.TAM_MARGEM_BOTAO
        return largura

    def cria_botao(self, palavra, cor):
        largura = self.calcula_largura_botao(palavra)
        botao = pygame.Surface((largura, 50))
        botao.fill(cor)
        return botao

    def exibir_botoes_palavras(self):
        posicaox = 50
        for palavra in self.objpalavras:
            largura = self.calcula_largura_botao(palavra.texto) #TODO: pensar melhor nesse metodo repetido aqui
            botao = self.cria_botao(palavra.texto, (218, 165, 32)) #cor goldenrod

            palavra.posicaoxbotao = posicaox
            imagemrect = botao.get_rect().move(posicaox, self.posicaoy)
            palavra.set_imagemrect(imagemrect)

            self.imprimir_botao(palavra.id, botao)

            posicaox += largura + 10

        self.posicaobotaorelacoes = posicaox

    def exibir_botao_qtd_relacoes(self, posicaox):
        setarelacoes = self.get_imagem("setarelacoes.gif")
        self.telajogo.exibe_imagem(setarelacoes, Posicao(posicaox + 10, self.posicaoy - 50))
        self.telajogo.exibe_texto(str(self.apljogo.qtdrelacaoes), self.TAM_FONTE_TEXTO,Posicao(posicaox + 27, self.posicaoy - 35))

    def imprimir_botao(self, idpalavraclicada, botao):
        self.telajogo.exibe_imagem(botao, Posicao(self.objpalavras[idpalavraclicada].posicaoxbotao, self.posicaoy))
        self.telajogo.exibe_texto(self.objpalavras[idpalavraclicada].texto, self.TAM_FONTE_TEXTO,
                                  Posicao(self.objpalavras[idpalavraclicada].posicaoxbotao + 10, self.posicaoy + 10))

    #TODO: os tres proximos metodos virarao um so, recebendo como prametro id e cor
    def destacar_botao(self, idpalavraclicada):
        botao = self.cria_botao(self.objpalavras[idpalavraclicada].texto, (255,105,180)) #cor HotPink
        self.imprimir_botao(idpalavraclicada, botao)

    def destacar_botao_clicado(self, idpalavraclicada):
        botao = self.cria_botao(self.objpalavras[idpalavraclicada].texto, (220,20,60)) #cor Crimson
        self.imprimir_botao(idpalavraclicada, botao)

    def restaurar_botao(self, idpalavraclicada):
        botao = self.cria_botao(self.objpalavras[idpalavraclicada].texto, (218, 165, 32)) #cor goldenrod
        self.imprimir_botao(idpalavraclicada, botao)

    def verifica_relacao(self, idpalavradestino):
        relacaoentrada = (self.idpalavraorigem, idpalavradestino, 0)

        for idrelacao in range(len(self.relacoes)):
            if self.relacoes[idrelacao] == relacaoentrada:
                self.apljogo.qtdrelacaoes -= 1
                #self.relacoes.pop(idrelacao)
                self.relacoes[idrelacao] = (self.relacoes[idrelacao][0], self.relacoes[idrelacao][1], 1)
                self.telajogo.exibe_som(self.get_som("acerto.wav"))
                return True

        self.telajogo.exibe_som(self.get_som("erro.wav"))
        # TODO: destacar de vermelho botoes da relacao incorreta
        return False

    def busca_estado_relacoes(self):
        estado = ""
        for relacao in self.relacoes:
            estado += str(relacao[2])
        return estado

    # TODO: conferir todas as possibilidades que essa logica alcanca
    def altera_cenario(self):
        estado = self.busca_estado_relacoes()
        for cenario in self.cenario:
            valido = True
            for id in range(len(estado)):
                if cenario[0][id] == "1" and estado[id] == "0":
                    valido = False
                    break

            if valido:
                imagem = self.get_imagem(cenario[1])
                self.telajogo.exibe_imagem(imagem, Posicao(0, 0))

    def controla_cor_botao_visitado(self, palavraobj):
        if palavraobj.foi_detectada() and palavraobj.id != self.idpalavraorigem and not palavraobj.ativo:
            self.destacar_botao(palavraobj.id)
        elif pygame.MOUSEBUTTONDOWN and palavraobj.id != self.idpalavraorigem and not palavraobj.ativo:
            self.restaurar_botao(palavraobj.id)

    def incrementa_lista_setas(self, wsize, posicaox, direcaonormal, relacao):
        seta = Seta(posicaox, wsize, direcaonormal, relacao)
        self.listasetas.append(seta)

    def manipula_seta_relacao(self, idorigem, iddestino):
        wsize = abs(self.objpalavras[iddestino].posicaoxbotao - self.objpalavras[idorigem].posicaoxbotao)
        posicaosaidaseta = idorigem
        issequencial = iddestino > idorigem
        if (not issequencial):
            posicaosaidaseta = iddestino

        relacao = (idorigem, iddestino)
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
                    if self.verifica_relacao(palavraobj.id):
                        self.altera_cenario()
                        self.manipula_seta_relacao(self.idpalavraorigem, palavraobj.id)

                    self.idpalavraorigem = -1


    def carrega_dados(self):
        self.objpalavras = self.apljogo.captura_frase()
        self.relacoes = self.apljogo.captura_relacoes()
        self.cenario = self.apljogo.captura_relacao_cenario()
        self.apljogo.qtdrelacaoes = len(self.relacoes)

    def jogo(self):
        observable = self.inicializa_observable()
        #self.exibir_musica("music1.mp3")
        self.apljogo.configuracao()

        self.carrega_dados()
        self.exibir_botoes_palavras()
        self.exibir_botao_qtd_relacoes(self.posicaobotaorelacoes)

        self.existepalavraclicada = False
        self.continua = True
        while self.continua:
            observable.verifica_evento()
            self.verifica_evento_mouse()
            self.exibir_botao_qtd_relacoes(self.posicaobotaorelacoes)
            self.exibir_botao_voltar_menu()

            for seta in self.listasetas:
                self.exibir_seta_relacao(seta.largura, seta.posicaox, seta.direcaonormal)

            pygame.display.flip()
            self.apljogo.clock.tick(10)




    # a classe ControlodorJogo (q eh um observador)recebe atualizacao pq a classe Observada ObservableEventosTeclado
    # capturou um evento
    def update(self, observable):
        if observable.clicou and self.rectbotaovoltar.collidepoint(pygame.mouse.get_pos()):
            self.continua = False

    def inicializa_observable(self):
        observable = ObservableEventosTeclado()
        observable.add_observer(self)
        return observable