'''Crie um programa que leia a quantidade de alunos de uma turma. Para cada aluno, leia duas notas e calcule a média. O
programa deverá: • informar Aprovado para média ‡ 6 ou Reprovado para média < 6; • contar quantos alunos foram
aprovados; • calcular a média geral da turma; • apresentar a maior média obtida. Não utilize max().'''

print(30*"=")
print("Controle de notas")
print(30*"=")

quantidade_alunos = int(input("Informe a quantidade de alunos da turma: "))

medias = []
maior_media = 0
aprovados = []


for aluno in range(quantidade_alunos):
    print(30*"=")
    nota1 = float(input(f"Informe a primera nota do {aluno+1}º aluno: "))
    nota2 = float(input(f"Informe a segunda nota do {aluno+1}º aluno: "))
    print(30*"=")

    media = (nota1 + nota2) / 2
    medias.append(media)

    print("Média do aluno: ", media)

    if media >= 6:
        print("Aprovado")
        aprovados.append(aluno+1)

    else:
        print("Reprovado")

    if maior_media < media:
        maior_media = media

alunos_aprovados = len(aprovados)
media_geral = sum(medias) / quantidade_alunos

print(30*"=")
print("Quantidade de alunos aprovados: ", alunos_aprovados)
print("Média geral da turma: ", media_geral)
print("Maior média obtida: ", maior_media)
