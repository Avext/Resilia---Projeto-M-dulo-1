#Esudante: Camilla Sampaio

import imp
from time import sleep
import conta as ct

#Função para menu de transferência
def menu_transferencia():

    print('''\033[0mUma transferência bancária é um pagamento eletrônico que envia dinheiro diretamente de uma conta para outra.\nExistem 3 tipos de transferência, TED, DOC e PIX.
    \n\033[1m (1) \033[0mTED
    \n\033[1m (2) \033[0mDOC
    \n\033[1m (3) \033[0mPIX
    \n\033[1m (4) \033[0mVOLTAR AO MENU PRINCIPAL
    \n\033[1m (5) \033[0mSAIR''')  #### mexi aqui
    opcao = int(input('''\n\033[1mEscolha uma das opções para saber mais: '''))

#Estrutura de repetição caso a opção seja inválida
    while opcao != 1 and opcao !=2 and opcao != 3 and opcao != 4 and opcao != 5 : ## mexi aqui

        print('\033[0m\nOpção inválida!')
        sleep(1)
        opcao = int(input('''\n\033[1mEscolha uma opção válida: '''))

    #Condicional para opção 1
    if opcao == 1:
        print ('''\n\033[0mNo \033[1mTED \033[0mo dinheiro cai no mesmo dia se realizada até às 17h, permite transferências maiores do que R$5.000
        \nOs documentos necessários para fazer um TED são:\n-Nome Completo\n-CPF/CNPJ\n-Valor a ser Transferido\n-Tipo de Conta\n-Dados Bancários\n''')
        opcao_1 = int(input('''\033[1m (1) \033[0mVOLTAR PARA MENU DE TRANSFERÊNCIA
        \n\033[1m (2) \033[0mSAIR
        \n\033[1mEscolha uma das opções: '''))
        if opcao_1 == 1:
            menu_transferencia()
        elif opcao_1 == 2: ### mexi aqui
            return False

    #Condicional para opção 2
    elif opcao == 2:
        print ('''\n\033[0mNo \033[1mDOC \033[0mo dinheiro cai no dia seguinte, mas pode levar mais tempo caso seja feito após às 22h, O valor máximo de transferência é de R$ 4.999,99.
        \nOs documentos necessários para fazer um DOC são:\n-Nome Completo\n-CPF/CNPJ\n-Valor a ser Transferido\n-Tipo de Conta\n-Dados Bancários\n''')
        opcao_1 = int(input('''\033[1m (1) \033[0mVOLTAR PARA MENU DE TRANSFERÊNCIA
        \n\033[1m (2) \033[0mSAIR
        \n\033[1mEscolha uma das opções: '''))
        if opcao_1 == 1:
            menu_transferencia()
        elif opcao_1 == 2:   #### mexi aqui
            return False
        

    #Condicional para opção 3
    elif opcao == 3:
        print ('''\n\033[0mO \033[1mPIX \033[0mfuncionará 24 horas por dia, 7 dias da semana, durante o ano todo.\nAs transações serão realizadas em tempo real, ou seja, o dinheiro cairá imediatamente na conta desejada.
        \nPara realizar a transferência em PIX é necessário somente a \033[1mChave PIX!\n''')
        opcao_1 = int(input('''\033[1m (1) \033[0mVOLTAR PARA MENU DE TRANSFERÊNCIA
        \n\033[1m (2) \033[0mSAIR
        \n\033[1mEscolha uma das opções: '''))
        if opcao_1 == 1:
            menu_transferencia()
        elif opcao_1 == 2:
            return False

    elif opcao == 4: ### mexi aqui'''
        return 1
    
    elif opcao == 5: ### mexi aqui
        print('Agradecemos....')
        return False


