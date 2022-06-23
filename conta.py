# Aluna : Luiza Sampaio
import os
from time import sleep 

def menu_principal():   # Função que quando chamada printa o menu principal 
    os.system("cls")
    print ('\nOlá, seja bem vindo(a)... \n')
    sleep (0.5)
    print ('\33[1mEscolha uma das opções abaixo:\n\33[0m')
    print ('[1] Dúvidas sobre conta corrente\n[2] Dúvidas sobre transferências\n[3] Dúvidas sobre pagamento de contas\n[4] Dúvidas sobre cartão\n[5] Sair')
    return int(input('Digite a opção escolhida: '))

def menu_conta(): # Função que quando chamada printa o submenu contas
        print ('\n\n\33[1mDúvidas sobre conta corrente:\33[0m\n')
        print ('[1] Como faço para abrir uma conta? \n[2] Quanto tempo leva para minha conta ficar ativa? \n[3] Como encerro minha conta?\n[4] Voltar ao inicio\n[5] Sair\n')
        pergunta = int(input('Digite a sua opção: '))
        if pergunta == 1:
            print ('''\n\33[1mComo faço para abrir uma conta? \33[0m\n\nVocê pode abrir sua conta-corrente pelo aplicativo do nosso banco ou diretamente na agência.
\33[1m\nPara abrir uma conta diretamente na agência são necessários:\33[0m
-Documento de identificação com foto que esteja dentro do prazo de validade;
-CPF; 
-Comprovante de residência atualizado;
-Comprovante de renda atualizado.
\n\33[1mPara abrir uma conta pelo APP são necessários:\33[0m 
-Foto do RG ou CNH;
-Foto do CPF; 
-Caso seja solicitado, um comprovante de residência e renda atualizados.\n''')
            if sair_retornar() == False:
                return False
        elif pergunta == 2:
            print ('''\n\33[1mQuanto tempo leva para minha conta ficar ativa?\33\n\n[0m.A conta ficará ativa automaticamente em 7 dias úteis Esse é o tempo necessário para a validação de dados.
Caso haja alguma pendência o usuário será notificado pelo aplicativo.
Porém se ao final do tempo limite sua conta não ficar ativa e não constar nenhuma pendência no APP, 
entre em contato com um de nossos atendentes através de um de nossos telefones de contato:
\n0800 123 456
0800 051 212
0800 789 101''')
            if sair_retornar() == False:
                return  False
        elif pergunta == 3:
            print ('''\n\33[1m\Como encerro minha conta?\33\n\n[0mA conta pode ser encerrada pelo APP ou diretamente na agência.
Para encerrar pelo APP basta ir em Menu> Minha conta> Encerrar conta e fornecer os dados necessários.
Para encerrar a conta na agência, basta ir em sua agência e falar com um de nossos atendentes.\n''')
            if sair_retornar() == False:
                return False
        elif pergunta == 4:  #Voltar ao inicio
            menu_conta
        elif pergunta == 5:  # Sair
            print ('''\n\33[1mAgradecemos por escolher o Resibank!\33[0m\n\n''')
            return False
        else:
            print ('\n\33[1;41mDigite uma opção válida\33[0m') # Caso o usuário digite uma opção inválida
            pergunta

def sair_retornar(): # Função para exibir as opções sair ou retornar ao menu
    sair_retornar = int(input('Digite [1] Para retornar ao menu Dúvidas sobre conta [2] Para encerrar o atendimmento: '))
    if sair_retornar == 1:
        return menu_conta()
    elif sair_retornar == 2:
        print ('''\n\33[1mAgradecemos por escolher o Resibank!\33[0m\n\n''')      
        return False


