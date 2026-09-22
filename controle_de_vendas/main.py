'''Uma loja deseja analisar 8 vendas realizadas durante o dia. O programa deve: • ler o valor de cada venda; • calcular o total
vendido; • contar quantas vendas foram maiores ou iguais a R$ 100,00; • identificar a maior venda; • apresentar a média das
vendas. Não utilize sum() nem max()'''

total_vendido = 0
maiores_100 = 0
maior_venda = 0

for i in range(8):
    venda = float(input(f"Entre com o valor da {i+1}º venda: "))
    total_vendido += venda

    if venda >= 100:
        maiores_100 += 1
    
    if venda > maior_venda:
        maior_venda = venda

media = total_vendido / 8

print("Total vendido: ", total_vendido)
print("Quantidade de vendas maiores ou iguais a R$ 100,00: ", maiores_100)
print("Maior venda: ", maior_venda)
print("Valor médio das vendas: ", media)