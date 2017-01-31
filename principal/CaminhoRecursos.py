import os

_author__ = 'Hanna'


class CaminhoRecursos:
    @staticmethod
    def caminho_imagens():
        return (os.path.dirname(os.path.realpath(__file__))).replace(CaminhoRecursos.diretorio(),
                                                                     os.path.join("recursos", "imagem"))

    @staticmethod
    def caminho_imagens_obstaculos():
        return (os.path.dirname(os.path.realpath(__file__))).replace(CaminhoRecursos.diretorio(),
                                                                     os.path.join("recursos", "imagem", "obstaculos"))

    @staticmethod
    def caminho_musicas():
        return (os.path.dirname(os.path.realpath(__file__))).replace(CaminhoRecursos.diretorio(),
                                                                     os.path.join("recursos", "audio", "musica"))

    @staticmethod
    def caminho_sons():
        return (os.path.dirname(os.path.realpath(__file__))).replace(CaminhoRecursos.diretorio(),
                                                                     os.path.join("recursos", "audio", "sons"))

    @staticmethod
    def diretorio():
        if os.path.basename(os.getcwd()) == "principal":
            return "principal"
        else:
            return os.path.join("library.zip", "principal")
