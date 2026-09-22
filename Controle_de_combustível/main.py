'''Um posto deseja registrar os abastecimentos realizados durante o dia. Para cada veículo, o sistema
deve receber a quantidade de litros abastecidos e o preço do litro.
O sistema deve calcular o valor pago por cada cliente e, ao final, apresentar:
• quantidade de veículos atendidos;
• quantidade total de litros vendidos;
• valor total arrecadado;
• média de litros abastecidos por veículo.
O cadastro termina quando a quantidade de litros informada for 0.
Desafio: informar quantos veículos abasteceram mais de 40 litros.'''

def total(preco,litros):
    return preco * litros

def media(quantidade_litros,quantidade_veiculos):
    if quantidade_litros != 0:
        return quantidade_litros / quantidade_veiculos
    else:
        return "_"


def main():
    quantidade_veiculos = 0
    veiculos_mais_40l = 0
    quantidade_litros = 0
    valor_total = 0

    print(30*"=")
    print("Sistema de Controle de Combustível")
    print(30*"=")

    litros = float(input("Informe a quantidade de litros abastecidos ou 0 para terminar: "))
    quantidade_litros += litros
    if litros >= 40:
        veiculos_mais_40l += 1

    while litros != 0:
        
        preco = float(input("Informe o preço do litro: "))
        valor_total += total(preco,litros)

        litros = float(input("Informe a quantidade de litros abastecidos ou 0 para terminar: "))
        quantidade_litros += litros

        if litros >= 40:
            veiculos_mais_40l += 1

        quantidade_veiculos += 1

    media_litros = media(quantidade_litros,quantidade_veiculos)
    
    print(30*"=")
    print("Quantidade de veículos atendidos: ", quantidade_veiculos)
    print("Quantidade total de litros vendidos: ", quantidade_litros)
    print(f"Valor total arrecadado: R$ {valor_total:.2f}")
    print("Média de litros abastecidos por veículo: ", media_litros)
    print("Quantidade de veiculos que abasteceram mais de 40 litros: ", veiculos_mais_40l)
    print(30*"=")

main()