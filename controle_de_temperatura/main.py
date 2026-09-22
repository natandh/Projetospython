'''Uma estação meteorológica registra a temperatura durante 7 dias. Para cada dia, informe a
temperatura registrada.
Ao final, apresente temperatura média, maior temperatura, menor temperatura, dia da maior
temperatura e quantidade de dias com temperatura acima de 30 °C.
Desafio: resolver sem armazenar todas as temperaturas.'''

print(30*"=")
print("Controle de temperatura")
print(30*"=")

temperaturas = 0
maior = 0
dias_maior_30 = 0

for dia in range(1,8):
    temperatura = float(input(f"informe a temperatura registrada no {dia}º: "))
    temperaturas += temperatura

    if maior < temperatura:
        maior = temperatura
        dia_maior = dia

    if temperatura >= 30:
        dias_maior_30 += 1

    if dia == 1:
        menor = temperatura

    if menor > temperatura:
        menor = temperatura

media = temperaturas / 7

print(f"Temperatura média: {media} °C")
print(f"Maior temperatura: {maior} °C")
print(f"Menor temperatura: {menor} °C")
print("Dia da maior temperatura: ", dia_maior)
print("Quantidade de dias com temperatura acima de 30 °C: ", dias_maior_30)