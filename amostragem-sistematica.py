# amostra simples - probabilidade e estatitica
from math import floor

pop = int(input('População: '))
amostra = int(input('Amostra: '))
cal = pop / amostra
ini = floor(cal) * floor(cal)
while ini > cal or ini <= 0:
    ini = int(input(f'Digite um número entre 1 e {floor(cal)}: '))
    if ini > cal:
        print('Você digitou um número muito alto!')
    if ini == 0:
        print('Você digitou um valor nulo!')
lista = [ini]
c = 0
while c < amostra - 1:
    v = ini + floor(cal)
    lista.append(v)
    ini += floor(cal)
    c += 1
print(lista)
