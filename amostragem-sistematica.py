pop = int(input('População: '))
n_amostra = int(input('Amostra: '))
calculo = pop / n_amostra
amostragem = round(calculo)
n_inicial = amostragem * amostragem
contador = 0
amostras = []

while n_inicial > amostragem or n_inicial <= 0:
    n_inicial = int(input(f'Digite um número entre 1 e {amostragem}: '))
    if n_inicial > amostragem:
        print('Você digitou um número muito alto')
    if n_inicial == 0:
        print('Você digitou um valor nulo!')

for amostra in range(n_inicial, n_amostra * amostragem, amostragem):
    amostras.append(amostra)

for amostra in amostras:
    print(amostra, end=" ")
