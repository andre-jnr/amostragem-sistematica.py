from amostragens import sistematica as sis
from amostragens import casualSimples as cs

while True:
    print('[1] - Amostragem simples casual')
    print('[2] - Amostragem sistematica')
    print('[3] - Amostragem proporcional estratificada')
    opcao = int(input('-> '))

    if opcao in [1, 2, 3]:
        break
    else:
        print('Opção inválida')

pop = int(input('População: '))
tamanho_amostra = int(input('Amostra: '))

match opcao:
    case 1:
        amostras = cs.coletarAmostra(pop, tamanho_amostra)
        cs.imprimirAmostras(amostras)
    case 2:
        amostragem = sis.criarAmostragem(pop, tamanho_amostra)

        numeroInicial = sis.lerValorInicial(amostragem)
        amostras = sis.coletarAmostra(numeroInicial, pop, amostragem)
        sis.imprimirAmostra(amostras)
    case 3:
        print("Amostragem proporcional estratificada em desenvolvimento!")
