'''Uma empresa realizou uma pesquisa com seus clientes. Cada cliente deverá informar uma nota de 1 a
5. O sistema continua recebendo notas até que seja informado 0.
Ao final, apresente quantidade de participantes, quantidade de cada nota e média das avaliações.
Desafio: informar qual foi a nota mais escolhida.'''

notas = []
nota_um = 0
nota_dois = 0
nota_tres = 0
nota_quatro = 0
nota_cinco = 0

print(30*"=")
print("Pesquisa de qualidade")
print(30*"=")

nota = 6

while nota != 0:
    
    nota = (input("Infome uma nota de 1 a 5 ou 0 para encerrar: "))
    if nota == "1" or nota == "2" or nota == "3" or nota == "4" or nota == "5" or nota == "0":
        nota = int(nota)
        notas.append(nota)
    else:
        print("Nota invalida")
    
notas.pop()   
quantidade = len(notas)

mais_escolhida = 0

for i in range(quantidade):
    if notas[i] == 1:
        nota_um += 1
        if nota_um > mais_escolhida:
            mais_escolhida = 1

    elif notas[i] == 2:
        nota_dois += 1
        if nota_dois > mais_escolhida:
            mais_escolhida = 2
    
    elif notas[i] == 3:
        nota_tres += 1
        if nota_tres > mais_escolhida:
            mais_escolhida = 3

    elif notas[i] == 4:
        nota_quatro += 1
        if nota_quatro > mais_escolhida:
            mais_escolhida = 4

    elif notas[i] == 5:
        nota_cinco += 1
        if nota_cinco > mais_escolhida:
            mais_escolhida = 5

if quantidade > 0:
    media = sum(notas) / quantidade

else:
    media = "nenhuma nota informada"

print("Quantidade de participantes: ",quantidade)
print("Quantidade de cada nota: ")
print(f"Nota 1: {nota_um}, nota 2: {nota_dois}, nota 3: {nota_tres}, nota 4: {nota_quatro}, nota 5: {nota_cinco}")
print("Média das avaliações: ",media)
print(f"A nota mais escolhida foi: nota {mais_escolhida}", )
