pop = int(input('População: '))
amostra = int(input('Amostra: '))
calculo = pop / amostra
amostragem = round(calculo)
n_inicial = amostragem * amostragem
contador = 0

while n_inicial > amostragem or n_inicial <= 0:
    n_inicial = int(input(f'Digite um número entre 1 e {amostragem}: '))
    if n_inicial > amostragem:
        print('Você digitou um número muito alto')
    if n_inicial == 0:
        print('Você digitou um valor nulo!')
amostras = [n_inicial]

while contador < amostra - 1:
    n_amostra = n_inicial + amostragem
    amostras.append(n_amostra)
    n_inicial += amostragem
    contador += 1
print(amostras)
