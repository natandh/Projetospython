'''Crie um jogo em que o computador possui um número secreto e o usuário deve tentar descobri-lo. A cada tentativa, o
programa deverá informar:
• “Tente um número maior.” quando o palpite for menor que o segredo;
• “Tente um número menor.” quando o palpite for maior;
• “Parabéns! Você acertou.” quando o usuário acertar. O programa também deverá informar a quantidade de tentativas
utilizadas. O usuário poderá tentar quantas vezes quiser. Desafio adicional:
• até 5 tentativas fi Excelente;
• de 6 a 10 fi Bom;
• acima de 10 fi Precisa melhorar.'''

import random

print(30*"=")
print("JOGO DE ADIVINHAÇÃO")
print(30*"=")

numero_secreto = random.randint(1, 100) # Gera um número entre 1 e 100 (inclusive)
palpite = 0
tentativas = 0

while palpite != numero_secreto:

    palpite = int(input("Adivinhe o numero secreto: "))
    print(30*"=")

    tentativas += 1

    if palpite < numero_secreto:
        print("Tente um número maior.")
        

    elif palpite > numero_secreto:
        print("Tente um número menor.")

    else:
        print("Parabéns! Você acertou.")
        print("Quantidade de tentativas: ", tentativas)

if tentativas <= 5:
    print("Excelente")

elif 5 < tentativas <= 10: 
    print("Bom")  

elif tentativas > 10: 
    print("Precisa melhorar")  

