from random import randint


def coletarAmostra(populacao, qtde_amostra):
    index = int(0)
    amostras = list()

    while index < qtde_amostra:
        valor_aleatorio = randint(1, populacao)
        if valor_aleatorio not in amostras:
            amostras.append(valor_aleatorio)
            index += 1

    return amostras


def imprimirAmostras(amostras):
    ultimo_indice = len(amostras) - 1
    for indice, amostra in enumerate(amostras):
        print(f'{amostra},', end=' ') if indice < ultimo_indice else print(
            f'{amostra}.')
