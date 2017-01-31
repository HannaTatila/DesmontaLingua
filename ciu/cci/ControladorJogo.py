import os
import pygame
from ciu.cih.EventosTeclado import ObservableEventosTeclado
from ciu.cih.Tela import Tela
from cln.cgt.AplJogo import AplJogo
from principal.CaminhoRecursos import CaminhoRecursos
from cln.cdp.Posicao import Posicao

__author__ = 'Hanna'


class ControladorJogo:

    TAM_FONTE_TEXTO = 35
    TAM_MARGEM_BOTAO = 40

    def __init__(self):
        self.apljogo = AplJogo()
        self.telajogo = Tela()
        self.music = True
        self.posicaobotaorelacoes = 0

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

    def exibir_botoes_palavras(self):
        posicaox = 50
        for palavra in self.objpalavras:
            tamanhopalavra = len(palavra.texto)
            largura = (tamanhopalavra * 10) + self.TAM_MARGEM_BOTAO
            botao = pygame.Surface((largura, 50))
            botao.fill((218, 165, 32))  # cor goldenrod

            self.telajogo.exibe_imagem(botao, Posicao(posicaox, (self.telajogo.tamanhotelay / 5 * 4)))
            imagemrect = botao.get_rect().move(posicaox, (self.telajogo.tamanhotelay / 5 * 4))
            palavra.set_imagemrect(imagemrect)
            self.telajogo.exibe_texto(palavra.texto, self.TAM_FONTE_TEXTO, Posicao(posicaox + 10, (self.telajogo.tamanhotelay / 5 * 4) + 10))

            posicaox += largura + 10

        self.posicaobotaorelacoes = posicaox

        self.exibir_botao_qtd_relacoes(posicaox)

    def exibir_botao_qtd_relacoes(self, posicaox):
        setarelacoes = self.get_imagem("setarelacoes.gif")
        self.telajogo.exibe_imagem(setarelacoes, Posicao(posicaox + 10, (self.telajogo.tamanhotelay / 5 * 4) - 50))
        self.telajogo.exibe_texto(str(self.apljogo.qtdrelacaoes), self.TAM_FONTE_TEXTO,Posicao(posicaox + 27, (self.telajogo.tamanhotelay / 5 * 4) - 35))

    def verifica_relacao(self, idpalavradestino):
        relacaoentrada = (self.idpalavraorigem, idpalavradestino)

        for k in range(len(self.relacoes)):
            if self.relacoes[k] == relacaoentrada:
                self.apljogo.qtdrelacaoes -= 1
                self.relacoes.pop(k)
                return True
            else:
                pass
                # TODO: destacar de vermelho botoes da relacao incorreta

        return False

    def verifica_clique_mouse(self):

        for palavraobj in self.objpalavras:
            if palavraobj.is_clicked():
                if not(self.existepalavraclicada):
                    self.idpalavraorigem = palavraobj.id
                    self.existepalavraclicada = True
                    #TODO: destacar palavra clicada
                else:
                    print("Relacao entre palavra" + str(self.idpalavraorigem) + " e " + str(palavraobj.id) + " !")
                    self.existepalavraclicada = False

                    self.verifica_relacao(palavraobj.id)


    def jogo(self):
        observable = self.inicializa_observable()
        #self.exibir_musica("music1.mp3")
        self.apljogo.configuracao()

        self.objpalavras = self.apljogo.gera_estrutura_frase()
        self.relacoes = self.apljogo.captura_relacoes()
        self.apljogo.qtdrelacaoes = len(self.relacoes)

        self.exibir_botoes_palavras()

        self.existepalavraclicada = False
        continua = True
        while continua:
            observable.verifica_evento()
            #TODO: geracombinacoesrelacoes()

            self.verifica_clique_mouse()
            self.exibir_botao_qtd_relacoes(self.posicaobotaorelacoes)

            pygame.display.flip()
            self.apljogo.clock.tick(10)


    # a classe ControlodorJogo (q eh um observador)recebe atualizacao pq a classe Observada ObservableEventosTeclado
    # capturou um evento
    def update(self, observable):
        if observable.cima:
            pass
        elif observable.soltoubaixo:
            pass

    def inicializa_observable(self):
        observable = ObservableEventosTeclado()
        observable.add_observer(self)
        return observable