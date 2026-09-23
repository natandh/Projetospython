'''Uma loja deseja registrar suas vendas. Para cada venda, informe código do vendedor e valor da venda.
O cadastro termina quando o código for 0.
Apresente quantidade total de vendas, valor total vendido, média das vendas e vendedor responsável
pela maior venda.
Desafio: informar quanto cada vendedor vendeu.'''

print("Controle de vendas de uma loja")

quantidade_total = 0
valor_total = 0
vendedores = []
maior_venda = 0

cod_vendedor = int(input("Informe o código do vendedor ou 0 para encerrar: "))
vendedores.append(cod_vendedor)

while cod_vendedor != 0:
    valor = float(input("Informe o valor da venda: "))

    quantidade_total += 1
    valor_total += valor

    if maior_venda < valor:
        maior_venda = valor
        vendedor_maior = cod_vendedor

    cod_vendedor = int(input("Informe o código do vendedor ou 0 para encerrar: "))
    vendedores.append(cod_vendedor)

if quantidade_total != 0:
    media = valor_total / quantidade_total

else:
    media = 0
    vendedor_maior = ""

print("Quantidade total de vendas: ", quantidade_total)
print(f"Valor total vendido: R$ {valor_total:.2f}")
print(f"Média das vendas: R$ {media:.2f}")
print("Vendedor responsável pela maior venda: ", vendedor_maior)