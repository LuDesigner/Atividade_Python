# Atividade 05
nota_01 = int(input('\nQual a primeira nota do aluno? '))
nota_02 = int(input('\nQual a segunda nota do aluno? '))
resultado = ((nota_01 + nota_02) / 2)

if resultado > 9 and resultado >= 10:
    print(f'A nota média do aluno foi de {resultado} , Conceito A')
elif resultado >7.51 and resultado <= 9:
    print(f'A nota média do aluno foi de {resultado} , Conceito B')
elif resultado >6.1 and resultado <= 7.5:
    print(f'A nota média do aluno foi de {resultado} , Conceito C')
elif resultado >4 and resultado <= 6:
    print(f'A nota média do aluno foi de {resultado} , Conceito D')
else:
    print(f'A nota média do aluno foi de {resultado} , Conceito E')