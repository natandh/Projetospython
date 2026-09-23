'''Um estacionamento deseja calcular o faturamento diário. Para cada veículo, informe placa e
quantidade de horas estacionado.
Valores: até 1 hora: R$ 10,00; de 1 até 3 horas: R$ 18,00; acima de 3 horas: R$ 30,00.
O cadastro termina quando a placa informada for "FIM".
Ao final, apresente quantidade de veículos, faturamento total, quantidade de veículos acima de 3 horas
e maior valor pago.'''

print("Sistema de estacionamento mensal")

quantidade = 0
faturamento_total = 0
veiculos_3h_mais = 0
maior_valor = 0

placa = input("Informe a placa do veiculo ou FIM para encerrar: ").lower()

while placa != "fim":

    horas = float(input("Informe a quantidade de horas estacionado: "))

    if horas <= 1:
        valor = 10

    elif horas <= 3:
        valor = 18

    else:
        valor = 30
        veiculos_3h_mais += 1

    if maior_valor < valor:
        maior_valor = valor

    quantidade += 1
    faturamento_total += valor
    
    placa = input("Informe a placa do veiculo ou FIM para encerrar: ").lower()
    
print("Quantidade de veículos: ", quantidade)
print(f"Faturamento total: R$ {faturamento_total},00")
print("Quantidade de veículos acima de 3 horas: ", veiculos_3h_mais)
print(f"Maior valor pago: R$ {maior_valor},00")