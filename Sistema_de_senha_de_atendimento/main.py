#Uma clínica possui três tipos de atendimento: 1 - Atendimento normal 2 - Atendimento prioritário 3 
#Encerrar Sempre que uma pessoa solicitar atendimento, o sistema deverá gerar uma senha. Exemplo:
#N001, N002, P001, N003. O sistema deverá controlar separadamente a quantidade de senhas normais
#e prioritárias. Responda: Quais contadores seriam necessários? Como diferenciar uma senha normal
#de uma prioritária? O que deve acontecer quando a opção 3 for escolhida? Qual estrutura seria
#utilizada para manter o sistema funcionando?
senha_n = 0
senha_p = 0
teste = True

while teste:

    print("="*30)
    print("Sistema de senha de atendimento")
    print("="*30)
    print("1 - Atendimento normal")
    print("2 - Atendimento prioritário")
    print("3 - Encerrar")

    opcao = (input("Informe a opção desejada: "))

    if opcao == "1":
        senha_n += 1
        senha_normal = f"N{senha_n:03d}"
        print("senha: ", senha_normal)
        
    elif opcao == "2":
        senha_p +=1
        senha_prioritaria = f"P{senha_p:03d}"
        print("senha: ", senha_prioritaria)
        
    elif opcao == "3":
        print("Obrigado por usar nosso sistema!")
        teste = False
    
    else:
        print("Opção invalidade, tente novamente!!!")


    


    
