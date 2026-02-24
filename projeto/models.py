
#------------------------
#Classe categoria
#------------------------

class Categoria:

    def __init__(self, id, tipo, limite_mensal):
        self.id = id
        self.tipo = tipo
        self.limite_mensal = limite_mensal

    def update_limite_mensal(self, limite_mensal):
        self.limite_mensal = limite_mensal

#------------------------
#Classe categoria
#------------------------

class Despesa:

    def __init__(self, id, descricao, valor, data, categoria):
        self.id = id
        self.descricao = descricao
        self.valor = valor
        self.data = data
        self.categoria = categoria

    def update_descricao(self, descricao):
        self.descricao = descricao

    def update_valor(self, valor):
        self.valor = valor

    def update_data(self, data):
        self.data = data

    def update_categoria(self, categoria):
        self.categoria = categoria

#------------------------
#Classe usuario
#------------------------

#------------------------
#Classe fonte de renda
#------------------------