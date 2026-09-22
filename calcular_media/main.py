aprovados = 0
recuperacao = 0
reprovados = 0

print("Bem vindo ao sistema de Notas")

aluno = None
while aluno != "0":
    notas = 0
    aluno = str(input("Informe o nome do aluno ou 0 para terminar: "))
    if aluno != "0":
        for i in range(3):
            nota = float(input("digite a nota: "))
            notas = notas + nota
        media = notas/3
        print("Aluno: ", aluno)
        print("Média final: ",media)
        if media >= 7:
            print("Aprovado")
            aprovados +=1
        elif media >= 5 and media < 7:
            print("Recuperação")
            recuperacao +=1
        elif media < 5:
            print("Reprovado")
            reprovados +=1

print("Alunos aprovados: ", aprovados)
print("Alunos em recuperação: ", recuperacao)
print("Alunos reprovados: ", reprovados)