
#------------------------
#Classe categoria
#------------------------

class Categoria:

    def __init__(self, id, tipo, limite_mensal):
        self.id = id
        self.tipo = tipo
        self.limite_mensal = limite_mensal

    def list_categoria(self):
        return f'ID: {self.id} - Tipo: {self.tipo} - Limite Mensal R$: {self.limite_mensal}'

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

    def list_despesa(self):
        return f'ID: {self.id} - Descrição: {self.descricao} - Valor R$: {self.valor} - Data: {self.data} - Categoria: {self.categoria}'

#------------------------
#Classe usuario
#------------------------

#------------------------
#Classe fonte de renda
#------------------------