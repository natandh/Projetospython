#Uma empresa deseja acompanhar o consumo mensal de energia. O sistema deverá receber o
#consumo de 12 meses. Ao final, deverá informar: consumo total; consumo médio; maior consumo;
#menor consumo; mês de maior consumo. Responda: Quantas vezes o sistema deverá receber dados?
#Qual estrutura de repetição seria adequada? Como descobrir o maior valor? Como descobrir o menor
#valor? Desafio: tente resolver sem armazenar os 12 valores.

consumo_mensal = 0
consumo_total = 0
maior_consumo = 0
menor_consumo = 0

for i in range(1,13):

    consumo_mensal = float(input(f"Informe o consumo do {i}º mes: "))
    consumo_total += consumo_mensal
    
    if i == 1:
        menor_consumo = consumo_mensal
        mes_menor = i
        maior_consumo = consumo_mensal
        mes_maior = i

    elif consumo_mensal > maior_consumo:
        maior_consumo = consumo_mensal
        mes_maior = i

    elif consumo_mensal < menor_consumo:
        menor_consumo = consumo_mensal
        mes_menor = i

consumo_medio = consumo_total / 12

print("Consumo total: ", consumo_total)
print("Consumo medio: ", consumo_medio)
print("Maior consumo : ", maior_consumo)
print("Menor consumo: ", menor_consumo)
print("Mês de maior consumo: mês", mes_maior)
print("Mês de menor consumo: mês", mes_menor)