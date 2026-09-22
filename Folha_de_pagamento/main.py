'''Folha de pagamento
Uma empresa deseja calcular o salário dos funcionários. Para cada funcionário, informe nome, salário
bruto e quantidade de horas extras. Cada hora extra vale R$ 25,00.
Calcule: salário final = salário bruto + (horas extras × 25).
Ao final, apresente quantidade de funcionários cadastrados, maior salário final, menor salário final e
média dos salários finais.
O cadastro termina quando o salário bruto informado for 0'''

nomes = []
salario_bruto = []
horas_extras = []
salarios_finais = []
quantidade_funcionarios = 0
maior_salario_final = 0
menor_salario_final = 0

def cadastro(quantidade_funcionarios,maior_salario_final,menor_salario_final):


    print(30*"=")
    print("Sistema de folha de pagamento")
    print(30*"=")

    nome = input("Informe o nome do funcionário: ")
    nomes.append(nome)

    while nome != "0":
        salario = float(input("Informe o salario bruto: "))
        salario_bruto.append(salario)

        extras = float(input("Informe a quantidade de horas extras: "))
        horas_extras.append(extras)

        salario_final = salario + (extras * 25)
        salarios_finais.append(salario_final)

        nome = input("Informe o nome do funcionário: ")
        nomes.append(nome)

        quantidade_funcionarios += 1

        if maior_salario_final == 0 and menor_salario_final == 0:
            maior_salario_final = salario_final
            menor_salario_final = salario_final

        elif salario_final > maior_salario_final:
            maior_salario_final = salario_final
        
        elif salario_final < menor_salario_final:
            menor_salario_final = salario_final

    media_salarios_finais = sum(salarios_finais) / quantidade_funcionarios

    print(30*"=")
    print("Quantidade de funcionários cadastrados: ", quantidade_funcionarios)
    print("maior salário final: ", maior_salario_final)
    print("menor salário final: ", menor_salario_final)
    print("média dos salários finais: ", media_salarios_finais)

def relatorio(nomes,salario_bruto,horas_extras,salarios_finais):
    print(30*"=")
    print("Relatorio")
    print(30*"=")
    for i in range(len(nomes)-1):
        print(f"Funcionario: {nomes[i]}, Salario bruto: R$ {salario_bruto[i]:.2f}, horas extras: {horas_extras[i]}, salario final: R$ {salarios_finais[i]:.2f}")


def menu():
    opcao = 10
    while opcao != "0":
        print(30*"=")
        print("Sistema de folha de pagamento")
        print(30*"=")
        print("1 - Castro de folha de pagamento")
        print("2 - Relatorio")
        print("0 - Sair")

        opcao = input("Entre com a opção desejada: ")
        print(30*"=")

        if opcao == "1":
            cadastro(quantidade_funcionarios,maior_salario_final,menor_salario_final)
        
        if opcao == "2":
            relatorio(nomes,salario_bruto,horas_extras,salarios_finais)
        
        if opcao == "0":
            print("Obrigado por usar nosso sistema!")
        
        else:
            print("Opção invalida, tente novamente.")

menu()