# Atividade 01
nota_01 = int(input('Qual a primeira nota do aluno? '))
nota_02 = int(input('Qual a segunda nota do aluno? '))
resultado = ((nota_01 + nota_02) / 2)

if resultado == 10:
    print(f'A nota média do aluno foi de {resultado}, aluno Aprovado com distinção')
elif resultado < 7:
    print(f'A nota média do aluno foi de {resultado}, aluno Reprovado')
else:
    print(f'A nota média do aluno foi de {resultado}, aluno Aprovado')