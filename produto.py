class Produto:
    def __init__ (self,nome,preco,quantidade):
        self.nome=nome
        self.preco=preco
        self.quantidade=quantidade

    def exibir_produtos(self):
        print("-"*30)
        print(f"Produto: {self.nome}")
        print(f"Quantidade: {self.quantidade} ")
        print(f"Preco:  {self.preco}")