alunos = []
opcao = 5

while opcao != 0:
    print("="*30)
    print("Cadastro de alunos")
    print("="*30)
    print("1 - Cadastrar alunos")
    print("2 - Listar todos os Alunos cadastrados")
    print("3 - Consultar se o Aluno está cadastrado")
    print("4 - Escluir um Aluno")
    print("0 - Sair")

    opcao = (input("Informe a opção desejada: "))
    
    print("="*30)
    
    if opcao == "1":
        aluno = input("Informe o nome do aluno a ser cadastrado: ")
        
        if aluno in alunos:
            print(f"Operação não realiza, o aluno {aluno}, já está cadastrado no sistema!")
            retornar = input("Pressione enter para retornar o menu principal: ")

        else:
            alunos.append(aluno)
            print(f"Aluno {aluno}, cadastrado com sucesso!")
            retornar = input("Pressione enter para retornar o menu principal: ")

    elif opcao == "2":
        for aluno in alunos:
            print(aluno)
        retornar = input("Pressione enter para retornar o menu principal: ")

    elif opcao == "3":
        aluno = input("Informe o nome do aluno a ser consultado: ")

        if aluno in alunos:
            print(f"O aluno, {aluno}, já está cadastrado no sistema!")
            retornar = input("Pressione enter para retornar o menu principal: ")

        else:
            print(f"O aluno, {aluno}, não esta cadastrado no sistema!")
            retornar = input("Pressione enter para retornar o menu principal: ")

    elif opcao == "4":
        aluno = input("Informe o nome do aluno a ser excluido do sistema: ")

    elif opcao == "0":
        print("Obrigado por usar nosso sistema!")




            
