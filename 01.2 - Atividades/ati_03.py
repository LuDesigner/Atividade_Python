# Atividade 03
print("""
        *** Escolha uma das opções da semana ***
        1 - Segunda-Feira;
        2 - Terça-Feira;
        3 - Quarta-Feira;
        4 - Quinta-Feira;
        5 - Sexta-Feira;
        6 - Sábado;
        7 - Domingo;
      """)

opcao_escolhida = input('Digite o número escolhido: \n')

if opcao_escolhida == '1' :
    print('\nOpção escolhida foi Segunda-Feira\n')
elif opcao_escolhida == '2':
    print('\nOpção escolhida foi Terça-Feira\n')
elif opcao_escolhida == '3':
    print('\nOpção escolhida foi Quarta-Feira\n')
elif opcao_escolhida == '4':
    print('\nOpção escolhida foi Quinta-Feira\n')
elif opcao_escolhida == '5':
    print('\nOpção escolhida foi Sexta-Feira\n')
elif opcao_escolhida == '6':
    print('\nOpção escolhida foi Sábado\n')
elif opcao_escolhida == '7':
    print('\nOpção escolhida foi Domingo\n')
else:
    print('\nValor Inválido\n')