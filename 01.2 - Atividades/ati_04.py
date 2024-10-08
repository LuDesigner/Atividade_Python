# Atividade 04
numb_01 = int(input('\nQual o primeira número? '))
numb_02 = int(input('\nQual o segunda número? '))
numb_03 = int(input('\nQual o terceiro número? '))

maior = numb_01
if numb_02 > numb_01 and numb_02 > numb_03:
    maior = numb_01

if numb_03 > numb_01 and numb_03 >= numb_02:
    maior = numb_03

menor = numb_01
if numb_02 < numb_03 and numb_02 < numb_01:
    menor = numb_02
    
if numb_03 <= numb_02 and numb_03 < numb_01:
    menor = numb_03

print(f"\nO menor número digitado foi {menor}")
print(f"\nO maior número digitado foi {maior}")