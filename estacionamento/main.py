horas = []
valores = []
veiculos = -1
veiculos_3h = 0

while 0 not in horas:

    hora = float(input("Informe a quantida de horas do veiculo ou 0 para terminar: "))
    horas.append(hora)
    
    if 0< hora <= 1:
        valor = 8.00
    
    elif 1< hora <=3:
        valor = 15.00
    
    elif hora > 3:
        valor = 20.00
        veiculos_3h +=1
    
    else:
        valor = 0
    
    valores.append(valor)
    veiculos += 1
    print("R$ ", valor)

print("quantidade de veiculos: ",veiculos)
print("Valor total arrecadado: ",sum(valores))
print("Quantidade de veiculos que permaneceram mais de 3 horas: ", veiculos_3h)