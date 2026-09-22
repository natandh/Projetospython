#Clínica Vida+

pacientes = []
id = []
pct_prioritario= []
medicos = {

}
agendamento_concluido = {

}

def cadastro():
    paciente = '-1'
    while paciente != '0':
        paciente = input('Digite seu CPF(11 dígitos e só números): ') 

        if len(paciente) < 11 or len(paciente) > 11:
            print ('CPF inválido.')
            continue

        if paciente in pacientes:
            print('Paciente já cadastrado. Tente outra opção: ')
            continue

        else:
            nome_paciente = input('Informe seu nome: ')
            telefone = int(input('Informe seu número de telefone: '))
            prioridade = input('Você precisa de atendimento prioritário? (Sim/Não): ').lower()

            if prioridade == 'sim':
                pct_prioritario.append(nome_paciente)
                print('Você foi adicionado à lista de prioridade')
                print('Cadastro Finalizado. ')
                pacientes.append(paciente)
                break

            if prioridade == 'nao' or prioridade == 'não':
                pacientes.append(paciente)
                print('Cadastro Finalizado. ')
                break

            else:
                print('Escolha inválida. Somente (Sim/Não): ')
                continue

def cadastro_medico():
    for i in range(1):
        id_medico = input('ID do(a) médico(a): ')

        if id_medico in id:
            print('Médico já cadastrado. Tente outra opção')
            continue

        else:
            nome_medico = input('Nos informe seu nome: ')
            especialidade = int(input('Qual especialidade do(a) Médico(a):\n1-Cardiologista\n2-Neurologista\n3-Clínico Geral\n4-Pediatra\n>  '))
            medicos[id_medico] = {
                'nome' : nome_medico,
                'especialidade' : especialidade,
                'dias disponíveis' : []
            }

        try:
            dias = int(input('Quantos dias no mês você está disponível: '))
        
        except ValueError:
            print('Informe somente números. ')
            continue

        else:
            try:
                for i in range(dias):
                    dia_atendimento = int(input('Informe quais dias do mês você está disponível: '))
                    medicos[id_medico]['dias disponíveis'].append(dia_atendimento)

            except ValueError:
                print('Informe somente números. ')
                continue

            else:
                print('Cadastro completo')

def agendamento_consulta():
    cpf = input('Porfavor informe seu CPF: ')
    if cpf in pacientes:
        tipo_atendimento = int(input('Qual tipo de atendimento necessita:\n1-Cardiologista\n2-Neurologista\n3-Clínico Geral\n4-Pediatra\n> '))

        encontrou = False
        medicos_encontrados = []

        for chave_id, dict_medico in medicos.items():

            if dict_medico['especialidade'] == tipo_atendimento:
                medicos_encontrados.append(chave_id)
                print(f'ID do médico: {chave_id}')
                print(f'O médico disponível é: {dict_medico['nome']}')
                print(f'Os dias dipoíveis são: {dict_medico['dias disponíveis']}')
                encontrou = True

            id_escolhido = input('Informe o ID do médico que deseja ser atendido: ')

            if id_escolhido in medicos_encontrados:
                medicos_encontrados = medicos[id_escolhido]

                for i in range(1):
                    escolha_dia = int(input('Escolha o dia que deseja ser atendido: '))

                    if escolha_dia in medicos_encontrados['dias disponíveis']:
                        agendamento_concluido[cpf] = {
                            'médico' : id_escolhido,
                            'dia marcado' : escolha_dia,
                            'horário' : []
                            }
                        
                        horario_agendado = float(input('Informe o horário que deseja ser atendido(Lembrando do horário de funcionamento)\n> '))

                        if horario_agendado in agendamento_concluido[cpf]:
                            print('Horário já escolhido, volte ao dia e tente remarcar: ')
                            continue

                        else: 
                            print('Finalizamos! Consulta agendada.')
                            indice = dict_medico['dias disponíveis'].index(escolha_dia)
                            dia_removido = dict_medico['dias disponíveis'].pop(indice)
                            agendamento_concluido[cpf] = {
                                'médico' : id_escolhido,
                                'dia marcado' : escolha_dia,
                                'horário' : [horario_agendado]
                            }
                    else:
                        print('Esse dia não está disponível para esse médico.')
                        continue

        if encontrou == False:
            print('Infelizmente estamos sem esse médico no momento.')

    else:
        print('Paciente ainda não cadastrado. Por favor faça seu cadastro para ser atendido... ')
        cadastro()

def remarcar_consulta():
    verificar_agendamento = input('Digite seu CPF para verificarmos seu agendamento: ')

    if verificar_agendamento in agendamento_concluido:
        escolha_remarcar = int(input('Verificamos e você tem uma consulta agendada. Você prefere:\n1-Cancelar consulta\n2-Remarcar para outro dia\n>'))

        if escolha_remarcar == 1:
            agendamento_concluido.pop(verificar_agendamento)
            print('Consulta cancelada. Obrigado por entrar em contato')

        if escolha_remarcar == 2:
            id_medico_antigo = agendamento_concluido[verificar_agendamento]['medico']
            dia_antigo = agendamento_concluido[verificar_agendamento]['dia']
            horario_antigo = agendamento_concluido[verificar_agendamento]['horário']
            
            medicos[id_medico_antigo]['dias disponíveis'].append(dia_antigo)
            medicos[agendamento_concluido]['horário'].pop()
            agendamento_concluido.pop(verificar_agendamento)

            tipo_atendimento = int(input('Qual tipo de atendimento necessita:\n1-Cardiologista\n2-Neurologista\n3-Clínico Geral\n4-Pediatra\n> '))

            encontrou = False
            medicos_encontrados = []

            for chave_id, dict_medico in medicos.items():

                if dict_medico['especialidade'] == tipo_atendimento:
                    medicos_encontrados.append(chave_id)
                    print(f'ID do médico: {chave_id}')
                    print(f'O médico disponível é: {dict_medico['nome']}')
                    print(f'Os dias dipoíveis são: {dict_medico['dias disponíveis']}')
                    encontrou = True
            
                id_escolhido = input('Informe o ID do médico que deseja ser atendido: ')
            
                if id_escolhido in medicos_encontrados:
                    medicos_encontrados = medicos[id_escolhido]

                    for i in range(1):
                        escolha_dia = int(input('Escolha o dia que deseja ser atendido: '))

                        if escolha_dia in medicos_encontrados['dias disponíveis']:
                            agendamento_concluido[verificar_agendamento] = {
                                'medico' : id_escolhido,
                                'dia marcado' : escolha_dia,
                                'horário' : []
                            }
                            
                            horario_agendado = float(input('Informe o horário que deseja ser atendido(Lembrando do horário de funcionamento)\n> '))

                            if horario_agendado in agendamento_concluido[verificar_agendamento]:
                                print('Horário já escolhido, volte ao dia e tente remarcar: ')
                                continue

                            else:             
                                print('Finalizamos! Consulta agendada.')
                                indice = dict_medico['dias disponíveis'].index(escolha_dia)
                                dia_removido = dict_medico['dias disponíveis'].pop(indice)
                                agendamento_concluido[verificar_agendamento] = {
                                    'medico' : id_escolhido,
                                    'dia marcado' : escolha_dia,
                                    'horário' : [horario_agendado]
                                }

                        else:
                            print('Esse dia não está disponível para esse médico.')
                            continue

            if encontrou == False:
                print('Infelizmente estamos sem esse médico no momento.')

    else:
        print('Não temos nenhum agendamento registrado com esse CPF. Por favor tente outra opção...')

def atendimento_emergencia():
    cpf_cadastrado = input('Por favor digite o CPF cadastrado: ')
    if cpf_cadastrado in pacientes:
        tipo_atendimento = int(input('Qual tipo de atendimento necessita:\n1-Cardiologista\n2-Neurologista\n3-Clínico Geral\n4-Pediatra\n> '))

        encontrou = False
        medicos_encontrados = []

        for chave_id, dict_medico in medicos.items():

            if dict_medico['especialidade'] == tipo_atendimento:
                medicos_encontrados.append(chave_id)
                print(f'ID do médico: {chave_id}')
                print(f'O médico disponível é: {dict_medico['nome']}')
                print(f'Os dias dipoíveis são: {dict_medico['dias disponíveis']}')
                encontrou = True
            
        id_escolhido = input('Informe o ID do médico que deseja ser atendido: ')
            
        if id_escolhido in medicos_encontrados:
            medicos_encontrados.append(medicos[id_escolhido])

            menor_dia = min(medicos_encontrados['dias disponíveis'])
            print('Seu atendimento foi agendado para o dia mais próximo que temos com o médico disponível. ')
            print(f'Dia: {menor_dia}')
            agendamento_concluido[cpf_cadastrado] = {
                        'médico' : id_escolhido,
                        'dia marcado' : menor_dia,
                        'horário' : []
                        }
                        
            horario_agendado = float(input('Informe o horário que deseja ser atendido(Lembrando do horário de funcionamento)\n> '))

            if horario_agendado in agendamento_concluido[cpf_cadastrado]:
                print('Horário já escolhido, volte ao dia e tente remarcar: ')
                

            else: 
                print('Finalizamos! Consulta agendada.')
                indice = dict_medico['dias disponíveis'].index(menor_dia)
                dia_removido = dict_medico['dias disponíveis'].pop(indice)
                agendamento_concluido[cpf_cadastrado] = {
                            'médico' : id_escolhido,
                            'dia marcado' : menor_dia,
                            'horário' : [horario_agendado]
                        }
    

    if encontrou == False:
        print('Infelizmente estamos sem esse médico no momento.')

    else:
        print('Paciente ainda não cadastrado. Por favor faça seu cadastro para ser atendido... ')
        cadastro()

def clinica():
    option = -1
    while option != 0:
        try:
            print('='*35)
            print('-----------CLÍNICA VIDA+-----------')
            print('='*35)
            print('Horário de funcionamento:\n08:00 as 17:00')
            print('='*35)
            option = int(input('Escolha umas das opções:\n1-Cadastrar Paciente\n2-Cadastrar Médico\n3-Agendamento de Consulta\n4-Remarcar Consulta\n5-Atendimento de emergência\n0-Sair\n> ' ))
            
        except ValueError:
            print('Opção inválida, somente números de 1 a ?. Tente novamente: ')
            continue

        else:
            match option:
                case 1: 
                    cadastro()

                case 2:
                    cadastro_medico()

                case 3:
                    agendamento_consulta()

                case 4:
                    remarcar_consulta()

                case 5:
                    atendimento_emergencia()

                case 0:
                    print('Sessão encerrada')
                    print('Obrigado por escolher nosso atendimento.')

                case _:
                    print('Escolha inválida. Tente novamente: ')
                    continue

clinica()