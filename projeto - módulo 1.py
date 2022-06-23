from time import sleep 
import conta as ct
import cartao as cr
import transferencia as tr
import menuPagamento as pg



rodando = True # Variável booleana para ser usada no laço de repetição
while rodando == True:  
    
    menu = ct.menu_principal() 
    if menu == 1:     # Condição que fará abrir o submenu selecionado
        menu_conta = ct.menu_conta()
        if menu_conta == False:
            rodando = False
    elif menu == 2:
        menu_transferencia = tr.menu_transferencia()
        if menu_transferencia == False:
            rodando = False
    elif menu == 3:
        menu_pagamento = pg.menuPagamento()
        if menu_pagamento == False:
            rodando = False
    elif menu == 4:
        menu_cartao = cr.cartoes()
        if menu_cartao == False:
            rodando = False
    elif menu == 5:
            print('''\n\33[1mAgradecemos por escolher o Resibank!\33[0m\n\n''')
            rodando = False
    else:
        print ('\n\nDigite uma opção válida')
        sleep (1)
        menu
    
