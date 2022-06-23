#Esudante: Thiago Lima de Vasconcelos


def solicitarCartao():
    for i in range (50):
        print()
    print('Escolha a opção desejada:\n Documentos necessários para solicitar um cartão (1)\n Tipos de cartões que disponibilizamos (2)\n Anuidade (3)\n Sair(0)')
    optionS = int(input('Digite aqui... '))
    
    while optionS!=0 and optionS != 1 and optionS !=2 and optionS != 3:
        for i in range (50):
            print()
        print('Opção inválida...')
        print('Escolha a opção desejada:\n Documentos necessários para solicitar um cartão (1)\n Tipos de cartões que disponibilizamos (2)\n Anuidade (3)\n Sair(0)')
        optionS = int(input('Digite aqui... '))

    if optionS == 1:
        for i in range (50):
            print()
        print('Documentos necessários para solicitar um cartão:\nOs documentos necessários para pedir um Cartão de Crédito são:\ncarteira de identidade,\nCPF,\ncomprovante de residência,\ncomprovante de renda.')
 
    elif optionS == 2:
        for i in range (50):
            print()
        print('Tipos de cartões que disponibilizamos:\nI. Cartão de crédito nacional\nII. Cartão de crédito internacional\nIII. Cartão Pré-pago\nIV. Cartão de Débito')


    elif optionS == 3:
        for i in range (50):
            print()
        print('Anuidade:\nO nosso banco não cobra anuidade ou nenhuma outra tarifa dos seus clientes.')


def bloqCancel():
    for i in range (50):
        print()
    print('Escolha a opção desejada:\n Desbloqueio (1)\n Bloqueio por perda ou roubo (2)\n Cancelamento (3)\n Sair(0)')
    optionB = int(input('Digite aqui... '))
    
    while optionB != 0 and optionB != 1 and optionB !=2 and optionB != 3:
        for i in range (50):
            print()
        print('Opção inválida...')
        print('Escolha a opção desejada:\n Desbloqueio (1)\n Bloqueio por perda ou roubo (2)\n Cancelamento (3)\n Sair(0)')
        optionB = int(input('Digite aqui... '))

    if optionB == 1:
        for i in range (50):
            print()
        print('Desbloqueio:\nAcesse o nosso aplicativo e no campo de buscas digite "Desbloquear cartão de crédito";\nEscolha dentre as opções qual deseja desbloquear;\nInsira o CVV (código de segurança do cartão) que fica no verso do cartão;\nInsira sua senha eletrônica e valide com o iToken.')
 
    elif optionB == 2:
        for i in range (50):
            print()
        print('Bloqueio por perda ou roubo:\nPara bloquear seu cartão de crédito, você pode ligar para o SAC: 0800 234 5678 ou pelo nosso aplicativo, no campo buscas digite "Bloqueio" e siga as orientações passadas')


    elif optionB == 3:
        for i in range (50):
            print()
        print('Cancelamento:\nI-Abra o aplicativo do banco;\nII-Toque no ícone de “Ajuda" (um ponto de interrogação), no canto superior direito;\nIII-Toque no botão “Converse com a gente” e depois “Conversar pelo chat”;\nIV-Solicite o cancelamento do cartão;\nV-Aguarde a confirmação dos seus dados.')


def limites():
    for i in range (50):
        print()
    print('Escolha a opção desejada:\n Ajuste de limite (1)\n Solicitar aumento de limite (2)\n Por que meu pedido de aumento de limite foi negado? (3)\n Sair(0)')
    optionL = int(input('Digite aqui... '))
    
    while optionL != 0 and optionL != 1 and optionL !=2 and optionL != 3:
        for i in range (50):
            print()
        print('Opção inválida...')
        print('Escolha a opção desejada:\n Ajuste de limite (1)\n Solicitar aumento de limite (2)\n Por que meu pedido de aumento de limite foi negado? (3)\n Sair(0)')
        optionL = int(input('Digite aqui... '))

    if optionL == 1:
        for i in range (50):
            print()
        print('Ajuste de limite:\nI-Abra o aplicativo do banco;\nII-Na parte de cartão de crédito, clique em “Ajustar limite”;\nIII-Arraste a “gotinha” para a esquerda e diminua o valor, arraste para direita e aumente.')
 
    elif optionL == 2:
        for i in range (50):
            print()
        print('Solicitar aumento de limite:\nI-No aplicativo do nosso banco, clique na parte de cartão de crédito e depois em "Ajustar limite";\nII-Na tela de ajuste, selecione o botão "Pedir aumento" e você poderá digitar o valor que gostaria (ou escolher uma das sugestões de valor);\nIII-Depois, é só clicar na setinha para para passar para outra tela;\nIV-Escolha o motivo;\nV-E pronto, faremos a sua análise e, em poucos segundos, você receberá uma resposta.')

    elif optionL == 3:
        for i in range (50):
            print()
        print('Por que meu pedido de aumento de limite foi negado?\nPrecisamos avaliar várias informações. Na hora de definir o limite, analisamos também os dados a respeito do cliente em agências de crédito, o comportamento de compras e pagamentos, se há parcelamentos de fatura e se, em algum momento, o mesmo já teve dívidas com o nosso banco.')


def cartoes():
    select = None
    for i in range (50):
        print()
    print('Escolha a informação que deseja saber sobre cartões de crédito\n Solicitação de cartão de crédito(1)\n Desbloqueio, bloqueio ou cancelamento(2)\n Limites de crédito(3)\n Voltar ao menu principal(4)\n Encerrar atendimento(0)\n')
    option = int(input('Digite aqui... '))

    while option != 0 and option != 4:
        if option == 1:
            solicitarCartao()
            print('\nO que deseja fazer agora?\n Voltar ao menu anterior (1)\n Voltar ao menu [Cartões] (2)\n Voltar ao menu principal (3)\n Encerrar contato (0)')
            select = int(input('Digite aqui... '))
            while select != 0 and select != 1 and select != 2 and select != 3:
                for i in range (50):
                    print()
                print('Opção inválida...')
                print('\nO que deseja fazer agora?\n Voltar ao menu anterior (1)\n Voltar ao menu [Cartões] (2)\n Voltar ao menu principal (3)\n Encerrar contato (0)')
                select = int(input('Digite aqui... '))
            if select == 1:
                option = 1
            elif select == 2:
                cartoes()
            elif select == 3: ## AVISAR PRO THIAGO!!!
                option = 4
            else:
                option = 0
            

        elif option == 2:
            bloqCancel()
            print('\nO que deseja fazer agora?\n Voltar ao menu anterior (1)\n Voltar ao menu [Cartões] (2)\n Voltar ao menu principal (3)\n Encerrar contato (0)')
            select = int(input('Digite aqui... '))
            while select != 0 and select != 1 and select != 2 and select != 3:
                for i in range (50):
                    print()
                print('Opção inválida...')
                print('\nO que deseja fazer agora?\n Voltar ao menu anterior (1)\n Voltar ao menu [Cartões] (2)\n Voltar ao menu principal (3)\n Encerrar contato (0)')
                select = int(input('Digite aqui... '))
            if select == 1:
                option = 1
            elif select == 2:
                bloqCancel()
            elif select == 3:
                option = 4  ## AVISAR PRO THIAGO
            else:
                option = 0


        elif option == 3:
            limites()
            print('\nO que deseja fazer agora?\n Voltar ao menu anterior (1)\n Voltar ao menu [Cartões] (2)\n Voltar ao menu principal (3)\n Encerrar contato (0)')
            select = int(input('Digite aqui... '))
            while select != 0 and select != 1 and select != 2 and select != 3:
                for i in range (50):
                    print()
                print('Opção inválida...')
                print('\nO que deseja fazer agora?\n Voltar ao menu anterior (1)\n Voltar ao menu [Cartões] (2)\n Voltar ao menu principal (3)\n Encerrar contato (0)')
                select = int(input('Digite aqui... '))
            if select == 1:
                option = 1
            elif select == 2:
                limites()
            elif select == 3:
                option = 4  ## AVISAR PRO THIAGO!!
            else:
                option = 0
        

        else:
            for i in range (50):
                print()
            print('Opção inválida...')
            print('Escolha a informação que deseja saber sobre cartões de crédito\n Solicitação de cartão de crédito(1)\n Desbloqueio, bloqueio ou cancelamento(2)\n Limites de crédito(3)\n Voltar ao menu principal(4)\n Encerrar atendimento(0)\n')
            option = int(input('Digite aqui... '))
    
    if option == 4 or select == 3:
        return 1

    elif option == 0 or select == 0:
        print('Agradecemos....')
        return 0