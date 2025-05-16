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

    def alterar_quantidade(self,lista):
      produto = input("informe o produto que deseja modificar a quantidade: ")
      if produto in lista:
           nova_quantidade = int(input("informe a quantidade que deseja adicionar: "))
           self.quantidade[produto] = nova_quantidade
           print(f"a nova quantidade de {self.nome} é {self.quantidade}")
      else:
          print("produto n registrado ainda! ")

    
    def vender_produto(self,lista):
       produto = input("qual produto deseja informar a venda: ")
       if produto in lista:
          vendas = int(input(f"informe a quantidade de vendas que foi feita de {produto}"))
          if vendas > self.quantidade[produto] in lista:
             print("A quantidade vendida não corresponde com o estoque")
          elif self.quantidade[produto] - vendas:
             print("venda realizada como sucesso!")
       else:
          ("A venda não foi concluida")   
          
        