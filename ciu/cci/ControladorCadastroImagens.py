import pygame
import sys

from pygame.rect import Rect

from ciu.cci.ControladorDigitacao import ControladorDigitacao
from ciu.cci.ControladorJogo import ControladorJogo
from pygame.constants import QUIT
from cln.cdp.Posicao import Posicao
from pygame.constants import KEYDOWN


class ControladorCadastroImagens(ControladorJogo):
    POSICAOX_BOTAO_CADASTRAR_FRASE = 350
    POSICAOY_BOTAO_CADASTRAR_FRASE = 400
    POSICAOX_BOTAO_MARCAR_CENARIO = 50
    POSICAOY_BOTAO_MARCAR_CENARIO = 280
    POSICAOX_BOTAO_NOME_IMAGEM = 550
    POSICAOY_BOTAO_NOME_IMAGEM = 280
    POSICAO_INICIAL_DADOS = 285
    POSICAOX_LETRA_DADOS = 250
    COR_CINZA = (255, 255, 255)
    COR_PRETO = (0, 0, 0)

    def __init__(self, frase, listarelacoes):
        ControladorJogo.__init__(self)
        self.frase = frase
        self.listarelacoes = listarelacoes
        self.listarelacoescenario = []
        self.listafinalcenario = []
        self.listacenariosjamarcados = []
        self.posicaoy = (self.telajogo.tamanhotelay / 3)

    def inicializar_tela(self):
        self.telajogo.telajogo.fill(self.COR_CINZA)
        self.exibir_botoes_palavras()


    def gera_estado_atual(self):
        estado = ""
        for relacao in self.listarelacoes:
            bit = "0"
            if relacao in self.listarelacoescenario:
                bit = "1"

            estado += bit

        return estado

    def gerar_botao(self, nomeimagem, posicaoxbotao, posicaoybotao):
        botao = self.get_imagem(nomeimagem)
        botaorect = botao.get_rect().move(posicaoxbotao, posicaoybotao)
        return botao, botaorect

    def imprimir_imagem_botao(self, botao, posicaox, posicaoy):
        self.telajogo.exibe_imagem(botao, Posicao(posicaox, posicaoy))

    def verifica_seta_repetida(self, relacao):
        for seta in self.listasetas:
            if seta.tuplarelacao == relacao:
                self.listasetas.remove(seta)
                self.listarelacoescenario.remove(relacao)
                self.inicializar_tela()
                return True

        return False

    def manipula_seta_relacao(self, idorigem, iddestino):
        relacao = (idorigem, iddestino)
        largura = abs(self.objpalavras[iddestino].posicaoxbotao - self.objpalavras[idorigem].posicaoxbotao)
        posicaosaidaseta = idorigem
        issequencial = iddestino > idorigem
        if not issequencial:
            posicaosaidaseta = iddestino

        setajaexiste = self.verifica_seta_repetida(relacao)

        if not setajaexiste:
            self.listarelacoescenario.append(relacao)
            self.incrementa_lista_setas(largura, self.objpalavras[posicaosaidaseta].posicaoxbotao, issequencial, relacao)


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
                    relacaoatual = (self.idpalavraorigem, palavraobj.id)
                    if (self.idpalavraorigem != palavraobj.id) and (relacaoatual in self.listarelacoes):
                        self.manipula_seta_relacao(self.idpalavraorigem, palavraobj.id)
                    self.idpalavraorigem = -1

    def exibe_lista_setas(self):
        for seta in self.listasetas:
            self.exibir_seta_relacao(seta.largura, seta.posicaox, seta.direcaonormal)

    def verifica_evento_fechar_tela(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    def atualiza_tela_geral(self):
        self.inicializar_tela()
        self.exibe_lista_setas()
        self.imprimir_imagem_botao(self.botaocadastrar, self.POSICAOX_BOTAO_CADASTRAR_FRASE, self.POSICAOY_BOTAO_CADASTRAR_FRASE)
        self.imprimir_imagem_botao(self.botaomarcarcenario, self.POSICAOX_BOTAO_MARCAR_CENARIO, self.POSICAOY_BOTAO_MARCAR_CENARIO)
        self.imprimir_imagem_botao(self.botaoimagem, self.POSICAOX_BOTAO_NOME_IMAGEM, self.POSICAOY_BOTAO_NOME_IMAGEM)
        self.telajogo.desenha_retangulo(self.COR_PRETO, (240, 280, 280, 40))
        pygame.display.flip()

    def get_key(self):
        while True:
            event = pygame.event.poll()
            if event.type == KEYDOWN:
                return event.key

            if pygame.mouse.get_pressed()[0]:
                if self.imagemrectbotaocadastrarnomeimagem.collidepoint(pygame.mouse.get_pos()):
                    self.finalizarcadastro = True
                    break

    def cadastrar_nome_imagem(self):
        controladorDigitacao = ControladorDigitacao(self.POSICAO_INICIAL_DADOS)

        self.atualiza_tela_geral()
        self.finalizarcadastro = False
        while True:
            teclaclicada = self.get_key()

            if self.finalizarcadastro:
                return controladorDigitacao.nome

            controladorDigitacao.verifica_teclas_digitadas(self, teclaclicada)

    def verifica_cenario_existente(self, estado):
        for estadoexistente in self.listafinalcenario:
            if estado == estadoexistente[0]:
                return True
        return False

    def criar_botoes(self):
        self.botaocadastrar, self.imagemrectbotaocadastrar = self.gerar_botao("btimagens.png", self.POSICAOX_BOTAO_CADASTRAR_FRASE, self.POSICAOY_BOTAO_CADASTRAR_FRASE)
        self.botaomarcarcenario, self.imagemrectbotaomarcarcenario = self.gerar_botao("btmarcarcenario.png", self.POSICAOX_BOTAO_MARCAR_CENARIO, self.POSICAOY_BOTAO_MARCAR_CENARIO)
        self.botaoimagem, self.imagemrectbotaocadastrarnomeimagem = self.gerar_botao("btfrase.png", self.POSICAOX_BOTAO_NOME_IMAGEM, self.POSICAOY_BOTAO_NOME_IMAGEM)

    def cadastro_imagens(self):
        self.apljogo.configuracao()
        self.objpalavras = self.apljogo.gera_estrutura_frase(self.frase)
        self.inicializar_tela()
        self.criar_botoes()

        self.existepalavraclicada = False
        while True:

            self.imprimir_imagem_botao(self.botaocadastrar, self.POSICAOX_BOTAO_CADASTRAR_FRASE, self.POSICAOY_BOTAO_CADASTRAR_FRASE)
            self.imprimir_imagem_botao(self.botaomarcarcenario, self.POSICAOX_BOTAO_MARCAR_CENARIO, self.POSICAOY_BOTAO_MARCAR_CENARIO)
            self.verifica_evento_mouse()
            self.exibe_lista_setas()
            self.verifica_evento_fechar_tela()

            if pygame.mouse.get_pressed()[0]:
                if self.imagemrectbotaomarcarcenario.collidepoint(pygame.mouse.get_pos()):
                    estado = self.gera_estado_atual()

                    if not self.verifica_cenario_existente(estado):
                        nomeimagemdigitado = self.cadastrar_nome_imagem()
                        self.listafinalcenario.append((estado, nomeimagemdigitado))
                        self.listarelacoescenario = []
                        self.listasetas = []
                        self.inicializar_tela()
                    else:
                        self.telajogo.exibe_som(self.get_som("erro.wav"))
                elif self.imagemrectbotaocadastrar.collidepoint(pygame.mouse.get_pos()):
                    return self.listafinalcenario

            pygame.display.flip()
            self.apljogo.clock.tick(10)