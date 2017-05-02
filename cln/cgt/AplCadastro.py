
from cgd.DAOFrase import DAOFrase

class AplCadastro:


    def completa_lista_com_id_frase(self, lista, idfrase):
        for id in range(len(lista)):
            lista[id] = lista[id] + (idfrase,)

        return lista


    def cadastrar_dados(self, frase, listarelacoes, listacenariosimagens):
        daofrase = DAOFrase()
        idfrase = daofrase.inserir_frase(frase)

        listarelacoes = self.completa_lista_com_id_frase(listarelacoes, idfrase)
        daofrase.inserir_relacoes(listarelacoes)

        listacenariosimagens = self.completa_lista_com_id_frase(listacenariosimagens, idfrase)
        daofrase.inserir_cenarios(listacenariosimagens)

        daofrase.fechar_banco()

