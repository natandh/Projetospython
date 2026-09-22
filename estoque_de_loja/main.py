estoque = 100

def entrada_produto(estoque,produto):
    return estoque + produto
   
def saida_produto(estoque,produto):
    return estoque - produto

def saldo(estoque):
    print("O saldo do estoque é: ", estoque)

def menu_principal(estoque):
    while True:
        print("1 - Entrada de produto")
        print("2 - Saida de produto")
        print("3 - Saldo consultar Estoque")
        print("0 - Encerrar")

        opcao = int(input("Informe a opção desejada: "))

        if opcao == 1:
            produto = int(input("Informe a quantidade produtos para adicionar ao estoque: "))
            estoque = entrada_produto(estoque,produto)
            print("Operação efetuada!")

        elif opcao == 2:
            if estoque > 0:
                produto = int(input("Informe a quantidade produtos para Excluir do estoque: "))
                if estoque >= produto:
                    estoque = saida_produto(estoque,produto)
                    print("Operação efetuada!")
                else:
                    print("Operação recusada, estoque insuficiente!")
            else:
                print("Operação recusada, estoque insuficiente!")

        elif opcao == 3:
            saldo(estoque)
            
        elif opcao == 0:
            print("Obrigado por usar nosso sistema!")
            return False
            
        else:
            print("Opção invalida, tente novamente.")

menu_principal(estoque)