import sistematica as sis

pop = int(input('População: '))
tamanho_amostra = int(input('Amostra: '))
amostragem = sis.criarAmostragem(pop, tamanho_amostra)

numeroInicial = sis.lerValorInicial(amostragem)
amostras = sis.coletarAmostra(numeroInicial, pop, amostragem)
sis.imprimirAmostra(amostras)
