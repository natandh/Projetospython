'''Uma turma possui quantidade indeterminada de alunos. Para cada aluno, informe três notas.
Classificação: média ‡ 7: Aprovado; média ‡ 5 e < 7: Recuperação; média < 5: Reprovado.
O cadastro termina quando a primeira nota for -1.
Ao final, apresente quantidade de aprovados, recuperações e reprovações, média geral, maior média e
menor média.'''

aluno = 1
quantidade_aprovados = 0
quantidade_recuperacao = 0
quantidade_reprovados = 0
media_total = 0
media_geral = 0
maior_media = 0
menor_media = 0

print("Para cada aluno, informe três notas. O cadastro termina quando a primeira nota for -1.")

nota1 = float(input(f"Informe a primeira nota do {aluno}º aluno: "))

while nota1 != -1:
    nota2 = float(input(f"Informe a segunda nota do {aluno}º aluno: "))
    nota3 = float(input(f"Informe a terceira nota do {aluno}º aluno: "))

    media = (nota1 + nota2 + nota3) / 3

    media_total += media
    media_geral = media_total / aluno

    if maior_media < media:
        maior_media = media

    if menor_media > media or menor_media == 0:
        menor_media = media

    print(f"A média do {aluno}º aluno é: {media}")

    if media >= 7:
        print("Aprovado")
        quantidade_aprovados += 1

    elif media >= 5:
        print("Recuperação")
        quantidade_recuperacao += 1

    else:
        print("Reprovado")
        quantidade_reprovados += 1

    aluno += 1

    nota1 = float(input(f"Informe a primeira nota do {aluno}º aluno: "))

print("Quantidade de aprovados: ", quantidade_aprovados)
print("Quantidade de recuperação: ", quantidade_recuperacao)
print("Quantidade de reprovados: ", quantidade_reprovados)
print("Média Geral: ",media_geral)
print("Maior média: ", maior_media)
print("Menor média: ", menor_media)