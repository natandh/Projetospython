def soma(a,b):
    return a+b

def subtracao(a,b):
    return a-b

def multiplicacao(a,b):
    return a*b

def divisao(a,b):
    if b != 0:
        return a/b
    else:
        print("Não é possivel dividir por 0")

print("Calculadora")
a = float(input("Informe o primeiro valor: "))
b = float(input("Informe o segundo valor: "))
print("1 SOMA , 2 SUBTRAÇÃO, 3 MULTIPLICAÇÃO, 4 DIVISÃO")
operacao = int(input("Informe a opção da operação desejada: "))

if operacao == 1:
    resultado = soma(a,b)
elif operacao == 2:
    resultado = subtracao(a,b)
elif operacao == 3:
    resultado = multiplicacao(a,b)
elif operacao == 4:
    resultado = divisao(a,b)

print("Resultado: ", resultado)