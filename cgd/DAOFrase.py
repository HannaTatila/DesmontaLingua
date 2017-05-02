import sqlite3

_author__ = 'Hanna'


class DAOFrase:
    def __init__(self):
        try:
            self.conn = sqlite3.connect("Desmontalingua2.db")  # conexao banco
            self.cursor = self.conn.cursor()
            self.criar_tabelas()
        except sqlite3.Error:
            print("Erro ao abrir o banco.")


    def criar_tabelas(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS frase (id INTEGER PRIMARY KEY AUTOINCREMENT, frase varchar(100))")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS relacao (id INTEGER PRIMARY KEY AUTOINCREMENT, origem INTEGER, destino INTEGER, frase_id INTEGER, FOREIGN KEY (frase_id) REFERENCES frase(id) )")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS cenario (id INTEGER PRIMARY KEY AUTOINCREMENT, estado VARCHAR(50), imagem VARCHAR(10), frase_id INTEGER, FOREIGN KEY (frase_id) REFERENCES frase(id))")
        #self.cursor.execute("ALTER TABLE cenario ADD COLUMN imagem VARCHAR(10)")


    def inserir_frase(self, frase):
        try:
            self.cursor.execute("INSERT INTO frase (frase) VALUES(?)", (frase,)) #VALUES (?,?)", (self.jogador[0], self.jogador[1],0,))
            self.conn.commit()  # salva dados no banco

            self.cursor.execute("SELECT * FROM frase")
            print "Tabela frase"
            print self.cursor.fetchall()
            print len(self.cursor.fetchall())
            return len(self.cursor.fetchall())


        except sqlite3.Error as oq:
            print(oq)
            print("Erro ao inserir frase.")


    def inserir_relacoes(self, listarelacoes):
        try:
            self.cursor.executemany("INSERT INTO relacao (origem, destino, frase_id) VALUES (?,?,?)", listarelacoes)
            self.conn.commit()

            self.cursor.execute("SELECT * FROM relacao")
            print "Tabela relacao"
            print self.cursor.fetchall()


        except sqlite3.Error as oq:
            print(oq)
            print("Erro ao inserir relacoes.")

    def inserir_cenarios(self, listacenarios):
        try:
            self.cursor.executemany("INSERT INTO cenario (estado, imagem, frase_id) VALUES (?,?,?)", listacenarios)
            self.conn.commit()

            self.cursor.execute("SELECT * FROM cenario")
            print "Tabela cenario"
            print self.cursor.fetchall()


        except sqlite3.Error as oq:
            print(oq)
            print("Erro ao inserir cenarios.")

    """
    def inserir_dados(self):
        try:
            self.cursor.execute("INSERT INTO frase VALUES(1,'O sol eh amarelo')") #VALUES (?,?)", (self.jogador[0], self.jogador[1],0,))
            self.cursor.execute("INSERT INTO relacao VALUES(1, 0, 1, 1)")
            self.cursor.execute("INSERT INTO relacao VALUES(2, 1, 2, 1)")
            self.cursor.execute("INSERT INTO relacao VALUES(3, 3, 2, 1)")
            self.cursor.execute("INSERT INTO cenario VALUES(1,'100','img1.png', 1)")
            self.cursor.execute("INSERT INTO cenario VALUES(2,'111','img2.png', 1)")
            self.conn.commit()  # salva dados no banco

            self.cursor.execute("SELECT * FROM frase")
            print(self.cursor.fetchone())

            self.cursor.execute("SELECT * FROM relacao")
            print(self.cursor.fetchone())

            self.cursor.execute("SELECT * FROM cenario")
            print(self.cursor.fetchone())

        except sqlite3.Error as oq:
            print(oq)
            print("Erro ao inserir dados.")

    """

    def consultar_frase(self, idfrase):
        try:
            self.cursor.execute("SELECT frase FROM frase WHERE id = (?)", (idfrase,))
            return self.cursor.fetchone()

        except sqlite3.Error:
            print("Erro ao consultar o banco!")

    def consultar_relacoes(self, idfrase):
        try:
            self.cursor.execute("SELECT origem, destino FROM relacao WHERE frase_id = (?)", (idfrase,))
            return self.cursor.fetchall()

        except sqlite3.Error:
            print("Erro ao consultar o banco!")

    def consultar_cenarios(self, idfrase):
        try:
            self.cursor.execute("SELECT estado, imagem FROM cenario WHERE frase_id = (?)", (idfrase,))
            return self.cursor.fetchall()

        except sqlite3.Error:
            print("Erro ao consultar o banco!")

    """
    def validar_login(self):
        try:
            self.cursor.execute("SELECT login, senha FROM jogador WHERE login = (?) AND senha = ?", (str(self.jogador[0]), str(self.jogador[1]),))
            if len(self.cursor.fetchall()) == 0:
                return False
            else:
                return True
        except sqlite3.Error:
            print("Erro ao consultar o banco para validar login!")

    def atualizar_pontuacao(self, pontos):
        self.cursor.execute("SELECT recorde FROM jogador WHERE login = (?)", (str(self.jogador[0]),))
        tuplarecorde = self.cursor.fetchone()
        if pontos > tuplarecorde[0]:
            self.cursor.execute("UPDATE jogador SET recorde = ? WHERE login = ?", (pontos, self.jogador[0],))
        self.conn.commit()
    """

    def fechar_banco(self):
        self.conn.close()
