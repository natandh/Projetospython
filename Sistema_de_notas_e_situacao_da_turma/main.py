"""Uma turma possui N alunos. O programa deverá primeiro perguntar quantos alunos serão cadastrados. Para cada
aluno, deverão ser informadas duas notas. Calcule a média individual e apresente:
• média do aluno;
• situação: Aprovado, Recuperação ou Reprovado. Regras:
• média >= 7 fi Aprovado;
• média entre 5 e 6,9 fi Recuperação;
• média < 5 fi Reprovado. Ao final, informe:
• média geral da turma;
• quantidade de aprovados;
• quantidade em recuperação;
• quantidade de reprovados;
• maior média obtida. Desafio adicional: informe também a posição do aluno que obteve a maior média.
Restrição: não utilize max().
Exemplo / referência:
Exemplo de saída: Maior média: 9.5 | Aluno: 4
Explique como o algoritmo consegue guardar a posição do aluno que possui a maior média."""

print(30*"=")
print("SISTEMA DE NOTAS E SITUAÇÃO DA TURMA")
print(30*"=")

quantidade = int(input("Informe a quantidade de alunos: "))
print(30*"=")

aprovados = 0
recuperacao = 0
reprovados = 0
maior_media = 0

for i in range(quantidade):
    print(f"{i+1}º Aluno")
    nota1 = float(input("Informe a primeira nota: "))
    nota2 = float(input("Informe a segunda nota: "))

    media = (nota1 + nota2) / 2

    print(f"Média do {i+1}º Aluno: {media}")

    if maior_media < media:
        maior_media = media
        posicao = i+1

    if media >= 7:
        print("Aprovado!")
        aprovados += 1

    elif media >= 5:
        print("Recuperação")
        recuperacao += 1

    elif media < 5:
        print("Reprovado")
        reprovados += 1
    
    print(30*"=")

print("Quantidade de aprovados: ", aprovados)
print("Quantidade em recuperação: ", recuperacao)
print("Quantidade de reprovados: ", reprovados)
print(f"Maior média: {maior_media} | Aluno: {posicao}")