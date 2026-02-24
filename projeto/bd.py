from models import Categoria

class bd:
    def __init__(self):
        self.despesas = []
        self.categorias = []
        self.tipos = ['Fixa', 'Variavel', 'Essencial', 'Diarias']
        self.id_categoria = 0
        self.id_despesa = 0


#-----------------
# CRUD categoria
#-----------------

    def inserir_categoria(self, categoria):
        
        if categoria.tipo in self.tipos:
            self.id_categoria += 1
            categoria.id = self.id_categoria
            self.categorias.append(categoria)
            print('Categoria inserida com sucesso!')
        else:
            print("Tipo de categoria inválido.")
        
        
    
    def listar_categoria(self):
        if not self.categorias:
            print('Nenhuma categoria cadastrada.')
            return
        else:
            for categoria in self.categorias:
                print(f'ID: {categoria.id} - Tipo: {categoria.tipo} - Limite Mensal R$: {categoria.limite_mensal}')
    
    def update_categoria(self, categoria, busca_id):
        for c in self.categorias:
            if c.id == busca_id:
                c.tipo = categoria.tipo
                c.limite_mensal = categoria.limite_mensal
                print('Categoria atualizada com sucesso!')
                return
        print('Categoria não encontrada.')
    
    def excluir_categoria(self, busca_id):
        for categoria in self.categorias:
            if categoria.id == busca_id:
                self.categorias.remove(categoria)
                print('Categoria excluída com sucesso!')
                return
        print('Categoria não encontrada.')

#-----------------
# CRUD Despesa
#-----------------
                
    def inserir_despesa(self, despesa):
        self.despesas.append(despesa)
        self.id_despesa += 1
        despesa.id = self.id_despesa
        return print('Despesa inserida com sucesso!')

    def listar_despesa(self):
        if not self.despesas:
            print('Nenhuma despesa cadastrada.')
            return
        else:
            for despesa in self.despesas:
                print(f'ID: {despesa.id} - Descrição: {despesa.descricao} - Valor R$: {despesa.valor} - Data: {despesa.data} - Categoria: {despesa.categoria}')
        
    def update_despesa(self, despesa, busca_id):
        for d in self.despesas:
            if d.id == busca_id:
                d.descricao = despesa.descricao
                d.valor = despesa.valor
                d.data = despesa.data
                d.categoria = despesa.categoria
                print('Despesa atualizada com sucesso!')
                return
        print('Despesa não encontrada.')

    def excluir_despesa(self, busca_id):
        for despesa in self.despesas:
            if despesa.id == busca_id:
                self.despesas.remove(despesa)
                print('Despesa excluída com sucesso!')
                return
        print('Despesa não encontrada.')

    def valor_total_despesas(self):
        total = sum(despesa.valor for despesa in self.despesas)
        return total