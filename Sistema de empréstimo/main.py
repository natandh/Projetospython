'''Uma biblioteca possui 100 livros disponíveis.
Menu:
1 - Emprestar livro
2 - Devolver livro
3 - Consultar quantidade disponível
0 - Encerrar
Ao emprestar, a quantidade disponível diminui em 1. Ao devolver, aumenta em 1.
Não permitir empréstimo quando não houver livros nem devolução quando não houver livros
emprestados.
Ao finalizar, apresente quantidade de empréstimos, quantidade de devoluções e livros disponíveis.'''

livros_disponivel = 100
livros_emprestado = 0
opcao = "4"

while opcao != "0":

    print(30*"=")
    print("Menu:")
    print(30*"=")
    print("1 - Emprestar livro")
    print("2 - Devolver livro")
    print("3 - Consultar quantidade disponível")
    print("0 - Encerrar")

    opcao = input("Entre coma opção desejada: ")

    if opcao == "1":
        if livros_disponivel > 0:
            livros_disponivel -= 1
            livros_emprestado += 1
            print("Livro emprestado, quantidade disponível: ", livros_disponivel)

        else:
            print("Não ha livros disponiveis")

    elif opcao == "2":
        if livros_emprestado > 0:
            livros_disponivel += 1
            livros_emprestado -= 1
            print("Livro devolvido, quantidade disponível: ", livros_disponivel)

        else:
            print("Não a livros emprestados")

    elif opcao == "3":
        print("Quantidade disponível: ", livros_disponivel)

    elif opcao == "0":
        print("Sistema encerrado.")

    else:
        print("Opção invalida, tente novamente.")