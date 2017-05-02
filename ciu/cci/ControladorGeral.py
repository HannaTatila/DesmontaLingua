import pygame
from cln.cdp.Posicao import Posicao
from ciu.cih.Tela import Tela
from cln.cgt.AplJogo import AplJogo
from cln.cdp.Seta import Seta

class ControladorGeral:
    TAM_MARGEM_BOTAO = 40
    TAM_FONTE_TEXTO = 35

    def __init__(self):
        self.apljogo = AplJogo()
        self.telajogo = Tela()
        self.posicaobotaorelacoes = 0


    def imprimir_botao(self, idpalavraclicada, botao):
        self.telajogo.exibe_imagem(botao, Posicao(self.objpalavras[idpalavraclicada].posicaoxbotao, self.posicaoy))
        self.telajogo.exibe_texto(self.objpalavras[idpalavraclicada].texto, self.TAM_FONTE_TEXTO,
                                  Posicao(self.objpalavras[idpalavraclicada].posicaoxbotao + 10, self.posicaoy + 10))

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

            palavra.set_botao(botao)
            palavra.posicaoxbotao = posicaox
            imagemrect = botao.get_rect().move(posicaox, self.posicaoy)
            palavra.set_imagemrect(imagemrect)

            self.imprimir_botao(palavra.id, botao)

            posicaox += largura + 10
        self.posicaobotaorelacoes = posicaox

    def controla_cor_botao_visitado(self, palavraobj):
        if palavraobj.foi_detectada() and palavraobj.id != self.idpalavraorigem:
            self.destacar_botao(palavraobj.id)
        elif pygame.MOUSEBUTTONDOWN and palavraobj.id != self.idpalavraorigem:
            self.restaurar_botao(palavraobj.id)

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

    def incrementa_lista_setas(self, wsize, posicaox, direcaonormal):
        seta = Seta()
        seta.set_largura(wsize)
        seta.set_posicaox(posicaox)
        seta.set_direcao_normal(direcaonormal)
        self.listasetas.append(seta)

    def manipula_seta_relacao(self, idorigem, iddestino):
        wsize = abs(self.objpalavras[iddestino].posicaoxbotao - self.objpalavras[idorigem].posicaoxbotao)
        posicaosaidaseta = idorigem
        issequencial = iddestino > idorigem
        if (not issequencial):
            posicaosaidaseta = iddestino

        self.exibir_seta_relacao(wsize, self.objpalavras[posicaosaidaseta].posicaoxbotao, issequencial)
        self.incrementa_lista_setas(wsize, self.objpalavras[posicaosaidaseta].posicaoxbotao, issequencial)

    def redimensionar_imagem(self, wsize):
        hsize = 75
        img = self.get_imagem("relacao.png")  # os.path.join(CaminhoRecursos.caminho_imagens(), "relacao.png")
        img = pygame.transform.scale(img, (wsize + 30, hsize))
        # img = PIL.Image.open(caminhoimagem)
        # img = pygame.image.fromstring(img.tobytes(), img.size, img.mode)
        # img.thumbnail((wsize + 20, hsize), Image.ANTIALIAS)
        return img

    def exibir_seta_relacao(self, wsize, posicaox, direcaonormal):
        pygameImage = self.redimensionar_imagem(wsize)

        if not direcaonormal:
            pygameImage = pygame.transform.flip(pygameImage, True, False)

        self.telajogo.exibe_imagem(pygameImage, Posicao(posicaox, self.posicaoy - 60))
