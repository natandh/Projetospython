saldo = 1500

def saida(saldo,saque):
    return saldo - saque

def entrada(saldo,deposito):
    return saldo + deposito

def conta(saldo):
    print("Seu saldo é: R$ ",saldo)

def menu_principal(saldo):
    while True:
        print("="*30)
        print("Caixa Eletronico")
        print("="*30)
        print("1 - Consultar saldo")
        print("2 - Sacar")
        print("3 - Depositar")
        print("0 - Sair")

        opcao = (input("Informe a opção desejada: "))
        print("="*30)
        if opcao == "1":
            conta(saldo)

        elif opcao == "2":
            if saldo > 0:
                saque = float(input("Informe o valor do saque: "))
                if saque > 0:
                    if saldo >= saque:
                        saldo = saida(saldo,saque)
                        print("Operação efetuada!")                    
                        conta(saldo)
                    else:
                        print("Operação recusada, Saldo insuficiente!")
                        conta(saldo)
                        
                else:
                        print("Operação recusada, valor invalido!")
                        
            else:
                print("Operação recusada, Saldo insuficiente!")
                conta(saldo)

        elif opcao == "3":
            deposito = float(input("Informe o valor a ser depositado: "))
            if deposito > 0:
                saldo = entrada(saldo,deposito)
                print("Operação efetuada!")
                conta(saldo)
            else:
                print("Valor de depósito incorreto")

        elif opcao == "0":
            print("Obrigado por usar nosso sistema!")
            return False
        else:
            print("Opção invalida, tente novamente.")
        
menu_principal(saldo)