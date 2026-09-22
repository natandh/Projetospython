def calcular_valor_vendas(quantidade_vendida, preco_unitario):
    return quantidade_vendida * preco_unitario

def calcular_meta(valor_total):
    if valor_total >= 5000:
        return "Meta diária de R$ 5.000,00 atingida"

    else:
        falta = 5000.00 - valor_total
        return f"Meta diária de R$ 5.000,00 não atingida. Faltam: R$ {falta:.2f}"

def main():
    codigo_produto = 1
    quantidade_vendas = 0
    preco_unitario = 0
    valor_total = 0
    maior_venda = 0

    while codigo_produto != 0:
        codigo_produto = int(input("Informe o codigo do produto ou 0 para terminar: "))
        if codigo_produto !=0:
            quantidade_vendida = int(input("Informe a quantidade vendida: "))
            preco_unitario = float(input("Informe o preço unitario do produto: "))

            valor_venda = calcular_valor_vendas(quantidade_vendida, preco_unitario)
            valor_total = valor_total + valor_venda
            quantidade_vendas +=1

            if valor_venda > maior_venda:
                maior_venda = valor_venda
        

    print("Quantidade de vendas: ", quantidade_vendas)
    print("Valor todal vendido: ", valor_total)
    print("Maior venda realizada: ", maior_venda)

    meta = calcular_meta(valor_total)

    print(meta)

main()