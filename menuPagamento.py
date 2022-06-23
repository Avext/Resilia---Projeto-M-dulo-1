#Esudante: Aline Aparecida

from time import sleep
import conta as ct  

pagamento ='''\n\33[1mComo faço para pagar contas? \33[0m\n\n\33[1mNa página inicial, toque na aba Pagamentos e escolha como quer fazer o pagamento: escaneando o código de barras ou digitando a numeração do boleto. Caso não consiga escanear, você precisará digitar a numeração do boleto. Para facilitar, também dá para copiar a numeração de algum outro local e colar direto no campo de digitação.\33[0m
\n\33[1mOs pagamentos serão compensados em dias úteis (segunda à sexta, exceto sábados, domingos e feriados) das 6h30 às 22h30. Alguns boletos têm horários reduzidos, dependendo do horário estipulado pelo emissor: o app identifica automaticamente e informa no momento do pagamento.\33[0m
\n\33[1mPagamentos após o horário permitido ou no final de semana/feriado serão agendados para o próximo dia útil automaticamente. Você também pode agendar o pagamento manualmente, se preferir.\33[0m
\n\33[1mFeito isso, pedirá sua senha para confirmar. Seu comprovante será disponibilizado automaticamente e você poderá salvar ou encaminhar para quem quiser. Ele fica disponível também na aba Comprovantes, além de ser encontrado facilmente clicando no pagamento correspondente em seu Extrato.\33[0m\n\n'''
compensarPagamento = '''\n\33[1mQual o prazo de compensação após o pagamento?\33[0m\n\nO prazo de compensação do pagamento pode variar de 2 a 3 dias úteis (exceto sábados, domingos e feriados), mas é importante verificar com o banco emissor o tempo que a compensação pode levar. Seu comprovante será disponibilizado automaticamente e você poderá salvar ou encaminhar para quem quiser. Boletos emitidos e pagos aqui no Resibank levam 2 horas úteis para compensar.\33[0m
\n\33[1mEm dúvida se pagou o mesmo boleto duas vezes? Não se preocupe que aqui no Resibank o sistema identifica automaticamente números de boletos iguais e do mesmo valor, bloqueando o segundo pagamento. \33[0m\n\n'''
comprovantePagamento = '''\n\33[1mOnde encontro o comprovante de pagamento?\33[0m\n\n\33[1mAssim que concluir o pagamento, o comprovante ficará disponível para salvar ou enviar para quem você quiser. Caso queira visualizá-lo depois, acesse o aplicativo e toque na aba Comprovantes, ou clique no pagamento correspondente em seu Extrato (o botão do comprovante aparecerá do lado direito). Lá terá o pagamento que você efetuou e ao tocar nele você verá o comprovante no final da página.\33[0m
\n\33[1mCaso tenha agendado o pagamento para os próximos dias, ele ficará dentro da aba Comprovantes sinalizado em azul. Pagamentos já concluídos aparecerão na cor verde. \33[0m\n\n'''
fim = '''\n\33[1mAgradecemos por escolher o Resibank!\33[0m\n\n'''
encerrarVoltar = '''\n\33[1mDeseja encerrar o seu atendimento? Se sim, digite 0 para sair. Se não, digite 1 para voltar para Pagamentos. \33[0m\n\n'''


def menuPagamento():

    print ('''\n\33[1mE quais são as suas dúvidas sobre pagamento?\n\n[1] - Como faço para pagar contas?\n[2] - Qual o prazo de compensação após o pagamento?\n[3] - Onde encontro o comprovante de pagamento?\n[0] - Sair\33[0m\n[9] Voltar para o menu principal \n\n''')
    sleep (1)
    menu = int(input("\n\33[1mDigite uma opção válida: \33[0m"))
    if menu == 1:
        print (pagamento)
        sleep (1)
        print (encerrarVoltar)
        if menuSair(menu) == False:
           return False
    elif menu == 2:
        print (compensarPagamento)
        sleep (1)
        print (encerrarVoltar)
        if menuSair(menu) == False:
            return False
    elif menu == 3: 
        print (comprovantePagamento)
        sleep (1)
        print (encerrarVoltar)
        if menuSair(menu) == False:
            return False
    elif menu==0: #sair do Menu
        print(fim)
        return False
    elif menu == 9:
        ct.menu_principal()
    else:
        print ('''\n\33[1mOpção inválida! Digite uma opçao válida.''')
        sleep (1)

def menuSair(x):
    sair= (int (input ("\n\33[1mDigite uma opção válida: \33[0m")))
    if sair == 1:
        return menuPagamento()
    elif sair== 0:
        print ('''\n\33[1mAgradecemos por escolher o Resibank!\33[0m\n\n''')      
        return False
    else:
        print ('''\n\33[1mOpção inválida!''')
        sleep (1)
        retornaSair = menuSair(x)

