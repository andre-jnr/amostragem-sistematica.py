from random import randint


def somarValores(chave, grupos):
    soma_qtde = 0

    for nome_grupo, valores in grupos.items():
        soma_qtde += valores[chave]

    return soma_qtde


def menorValor(chave, grupos):
    menorValor = float('inf')
    idValor = ''
    resultado = dict()

    for nome_grupo, dicionario_interno in grupos.items():
        valor_atual = dicionario_interno[chave]
        if (valor_atual < menorValor) and (valor_atual != 0):
            menorValor = dicionario_interno[chave]
            idValor = nome_grupo

    resultado[idValor] = menorValor
    return resultado


def coletarGrupos(qtde_grupos):
    grupos = dict()
    for i in range(qtde_grupos):
        nome = str(input(f'Nome do {i + 1}º grupo: '))
        qtde = int(input('Quantidade de elementos desse grupo: '))
        grupos[nome] = qtde

    return grupos


def definirGrupos(qtde_grupos):
    grupos = coletarGrupos(qtde_grupos)
    populacao = sum(grupos.values())
    for key, value in grupos.items():
        percentual = (value / populacao) * 100
        grupos[key] = {'qtde': value, 'percentual': round(percentual, 2)}
    return grupos


def inserindoValor(qtde_amostra, populacao):
    amostras = list()
    contador = 0
    while contador < qtde_amostra:
        valor = randint(1, populacao)
        if valor not in amostras:
            amostras.append(valor)
            contador += 1
    return amostras


def coletarAmostra(qtde_grupos, tamanho_amostra):
    qtde_amostra_geral = 0
    grupos = definirGrupos(qtde_grupos)
    populacao = somarValores('qtde', grupos)
    for key, value in grupos.items():
        qtde_amostra = round((tamanho_amostra * value['percentual']) / 100)
        qtde_amostra_geral += qtde_amostra

        grupos[key]['qtde_amostra'] = qtde_amostra
        amostras = inserindoValor(qtde_amostra, populacao)
        grupos[key]['amostras'] = amostras

    if qtde_amostra_geral != tamanho_amostra:
        comMenorValor = menorValor('qtde_amostra', grupos)
        chave_menor_valor = next(iter(comMenorValor.keys()))
        valor_menor_valor = comMenorValor[chave_menor_valor]

        if qtde_amostra_geral < tamanho_amostra:
            grupos[chave_menor_valor]['qtde_amostra'] = valor_menor_valor + 1
        else:
            grupos[chave_menor_valor]['qtde_amostra'] = valor_menor_valor - 1
        amostras = inserindoValor(qtde_amostra, populacao)
        grupos[chave_menor_valor]['amostras'] = amostras

    return grupos


def mostrarTabela(grupos):
    from rich.table import Table
    from rich.console import Console

    console = Console()
    tabela = Table(title='AMOSTRAGEM PROPORCIONAL ESTRATIFICADA')
    tabela.add_column('Grupo')
    tabela.add_column('População')
    tabela.add_column('Percentual')
    tabela.add_column('Amostra')

    for nome_grupo, valores in grupos.items():
        tabela.add_row(nome_grupo, str(valores['qtde']), str(
            valores['percentual']), str(valores['qtde_amostra']))

    tabela.add_row('TOTAL', str(somarValores('qtde', grupos)), str(round(somarValores('percentual', grupos), 2)),
                   str(somarValores('qtde_amostra', grupos)))

    console.print(tabela)
