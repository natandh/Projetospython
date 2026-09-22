valores = [5, 8, 13, 21, 34]

procurado = 13

for valor in valores:
    if valor == procurado:
        print("Encontrado")
        break

else:
    print("Não encontrado")