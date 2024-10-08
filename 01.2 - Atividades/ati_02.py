# Atividade 02
opcao_escolhida = input('Digite F para Feminino ou M para Masculino: \n')
opcao_respondida = opcao_escolhida.upper()

if opcao_respondida == 'F' :
    print('\nOpção escolhida: F - Feminino.')
elif opcao_respondida == 'M':
    print('\nOpção escolhida: M - Masculino.')
else:
    print('\nSexo Inválido\n')