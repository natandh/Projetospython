'''Uma biblioteca deseja controlar empréstimos de livros. O sistema apresenta: 1 - Emprestar livro 2 
Devolver livro 3 - Consultar quantidade disponível 0 - Sair A biblioteca possui inicialmente 50 livros
disponíveis. Quando um livro é emprestado, a quantidade disponível diminui em 1. Quando um livro é
devolvido, a quantidade disponível aumenta em 1. O sistema não pode permitir empréstimo quando
não houver livros disponíveis. Também não deve permitir devolução quando não houver livros
emprestados. Responda: Quais variáveis são necessárias? Quais condições devem ser verificadas?
Qual estrutura mantém o menu funcionando? Como controlar a quantidade de livros emprestados'''
def emprestar_livros(quantidade):
    if quantidade > 0:
        quantidade -=1
        print("Livro emprestado")
    else:
        print("Não ha livros disponível!")
    
    return quantidade

def devolver_livros(quantidade):
    if quantidade < 50:
        quantidade +=1
        print("Livro devolvido")
    else:
        print("Não ha livros emprestados!")
    
    return quantidade

def consultar_livros(quantidade):
    print("quantidade de livros disponível: ", quantidade)
    emprestados = 50 - quantidade
    print("quantidade de livros emprestados: ", emprestados)

def sair():
    print("Obrigado por usar nosso sistema!")
    
quantidade = 50

def menu_principal(quantidade):
    quantidade = 50
    while True:
        print("="*30)
        print("Sistema da biblioteca")
        print("="*30)
        print("1 - Emprestar livro")
        print("2 - Devolver livro")
        print("3 - Consultar quantidade disponível")
        print("0 - Sair")

        opcao = (input("Informe a opção desejada: "))
        print("="*30)

        if opcao == "1":
            emprestar_livros(quantidade)
        
        elif opcao == "2":
            devolver_livros(quantidade)
        
        elif opcao == "3":
            consultar_livros(quantidade)
        
        elif opcao == "0":
            sair()
            return False
        else:
            print("Opção invalida, tente novamente.")

menu_principal(quantidade)