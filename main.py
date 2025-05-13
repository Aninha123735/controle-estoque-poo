from produto import Produto
from produtoalimenticio import ProdutosAlimenticios

lista=[]
while True:
    print("MENU")
    print("-"*10)
    print("1.cadastrar produto comum")
    print("2.cadastrar produto alimenticio")
    print("3.listar todos os produtos")
    print("4.sair")
    escolha= input("informe a opcao desejada: ")

    if escolha =="1": 
     qntd= int(input("informe quantos produtos deseja cadastrar: "))
     for i in range(qntd):
      sla= input("informe o nome do produto que deseja inseiri: ")
      quantidade = int(input(f"informe a quantidade do produto {sla}"))
      preco = float(input("informe o preco do produto: "))
      produto = Produto(sla, preco, quantidade)
      lista.append(produto)

    elif escolha == "2":
      sla = input("informe o nome do produto que deseja inseiri: ")
      quantidade = int(input(f"informe a quantidade do produto {sla}"))
      preco = float(input("informe o preco do produto: "))
      validade= float(input("informe a validade do produto"))
      produtoalimenticioo = ProdutosAlimenticios(sla,preco,quantidade,validade)
      lista.append(produtoalimenticioo)

    elif escolha == "3":
     for c in lista:
       c.exibir_produtos()
    
    elif escolha == "4":
      print("Sair")
      break

    else:
      print("Opcao invalida!")