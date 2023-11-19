def criarAmostragem(populacao, qtde_amostras):
    return round(populacao / qtde_amostras)


def lerValorInicial(amostragem):
    valor_inicial = amostragem * amostragem
    print("Digite um número para ser o número inicial")

    while (valor_inicial > amostragem) or (valor_inicial <= 0):
        valor_inicial = int(
            input(f'O número precisa ser entre 1 e {amostragem}: '))
        if valor_inicial > amostragem:
            print('Você digitou um número muito alto')
        if valor_inicial == 0:
            print('Você digitou um valor nulo!')

    return valor_inicial


def coletarAmostra(valor_inicial, populacao, amostragem):
    amostras = list()
    for amostra in range(valor_inicial, populacao, amostragem):
        amostras.append(amostra)

    return amostras


def imprimirAmostra(amostras):
    for amostra in amostras:
        print(amostra, end=" ")
