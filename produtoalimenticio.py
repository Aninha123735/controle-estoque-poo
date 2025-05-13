from produto import Produto

class ProdutosAlimenticios(Produto):
    def __init__ (self,nome,preco,quantidade,data_validade):
        super().__init__(nome,preco,quantidade)
        self.data_validade = data_validade
        
    def exbir_produtos(self):
        super().exibir_produtos()
        print(f"A data de validade: {self.data_validade}")


