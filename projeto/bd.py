import mysql.connector
from datetime import datetime


class bd:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Elias_0301!",
            database="me_poupe",
            ssl_disabled=True
        )

        self.cursor = self.conexao.cursor()
        self.criar_tabelas()

    # -----------------
    # CRIAR TABELAS
    # -----------------
    def criar_tabelas(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS categorias (
            id INT PRIMARY KEY,
            tipo VARCHAR(50) UNIQUE NOT NULL,
            limite_mensal DECIMAL(10,2) NOT NULL
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS despesas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            descricao VARCHAR(100) NOT NULL,
            valor DECIMAL(10,2) NOT NULL,
            data DATE NOT NULL,
            categoria_id INT,
            FOREIGN KEY (categoria_id) REFERENCES categorias(id)
        )
        """)

        self.conexao.commit()

    # -----------------
    # CRUD CATEGORIA
    # -----------------

    def inserir_categoria(self, categoria):
        if categoria.tipo == 1:
            categoria.tipo = 'Fixa'
            categoria.id = 1
        elif categoria.tipo == 2:
            categoria.tipo = 'Variavel'
            categoria.id = 2
        elif categoria.tipo == 3:
            categoria.tipo = 'Essencial'
            categoria.id = 3
        elif categoria.tipo == 4:
            categoria.tipo = 'Diarias'
            categoria.id = 4
        try:
            sql = "INSERT INTO categorias (id, tipo, limite_mensal) VALUES (%s, %s, %s)"
            self.cursor.execute(sql, (categoria.id, categoria.tipo, categoria.limite_mensal))
            self.conexao.commit()
            print("Categoria inserida!")
        except mysql.connector.Error as err:
            print(f"Categoria já existente no banco de dados: ")

    def listar_categoria(self):
        sql = "SELECT * FROM categorias"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def atualizar_categoria(self, novo_limite, id_busca):
        sql = "UPDATE categorias SET limite_mensal = %s WHERE id = %s"
        
        self.cursor.execute(sql, (novo_limite, id_busca))
        self.conexao.commit()

        if self.cursor.rowcount > 0:
            print("Categoria atualizada com sucesso!")
        else:
            print("Categoria não encontrada.")

    '''def excluir_categoria(self, id):
        sql = "DELETE FROM categorias WHERE id = %s"
        self.cursor.execute(sql, (id,))
        self.conexao.commit()
        print("Categoria excluída!")'''

    def fechar(self):
        self.cursor.close()
        self.conexao.close()

    # -----------------
    # CRUD DESPESAS
    # -----------------

    def inserir_despesa(self, despesa):

        data_convertida = datetime.strptime(despesa.data, "%d/%m/%Y").date()

        sql = """
        INSERT INTO despesas (id, descricao, valor, data, categoria_id)
        VALUES (%s, %s, %s, %s, %s)
        """
        self.cursor.execute(sql, (despesa.id, despesa.descricao, despesa.valor, data_convertida, despesa.categoria))
        self.conexao.commit()
        print("Despesa inserida!")

    def listar_despesas(self):
        sql = """
        SELECT d.id, d.descricao, d.valor, d.data, c.tipo
        FROM despesas d
        LEFT JOIN categorias c ON d.categoria_id = c.id
        """
        self.cursor.execute(sql)
        despesas = self.cursor.fetchall()

        return despesas

    def atualizar_despesa(self, despesa, busca_id):

        data_convertida = datetime.strptime(despesa.data, "%d/%m/%Y").date()

        sql = """
        UPDATE despesas
        SET descricao=%s, valor=%s, data=%s, categoria_id=%s
        WHERE id=%s
        """
        self.cursor.execute(sql, (despesa.descricao, despesa.valor, data_convertida, despesa.categoria, busca_id))
        self.conexao.commit()

        if self.cursor.rowcount > 0:
            print("Despesa atualizada!")
        else:
            print("Despesa não encontrada.")

    def excluir_despesa(self, id):
        sql = "DELETE FROM despesas WHERE id = %s"
        self.cursor.execute(sql, (id,))
        self.conexao.commit()

        if self.cursor.rowcount > 0:
            print("Despesa excluída!")
        else:
            print("Despesa não encontrada.")

    def valor_total_despesas(self):
        self.cursor.execute("SELECT SUM(valor) FROM despesas")
        total = self.cursor.fetchone()[0]

        if total is None:
            total = 0

        print(f"Total de despesas: R$ {total}")
        return total
    
    def total_despesas_por_categoria(self):
        sql = """
        SELECT c.tipo, SUM(d.valor) AS total
        FROM despesas d
        JOIN categorias c ON d.categoria_id = c.id
        GROUP BY c.tipo
        """

        self.cursor.execute(sql)
        resultados = self.cursor.fetchall()

        if not resultados:
            print("Nenhuma despesa cadastrada.")
            return []

        for tipo, total in resultados:
            print(f"Categoria: {tipo} | Total gasto: R$ {total:.2f}")

        return resultados