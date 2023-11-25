# Amostragens estatisticas

Tive a ideia de desenvolver um programa que gerar toda a amostragem sistemática quando o professor estava com dificuldade de implementar em `C`, com o tempo resolvi implementar outras amostragens estudadas em sala de aula.

- Amostragem casual simples.
- Amostragem sistematica.
- Amostragem proporcional estratificada.

## Descrição

### Amostragem casual simples

A amostragem casual simples é um método de amostragem probabilística em que cada elemento da população tem a mesma probabilidade de ser selecionado para a amostra. Para realizar uma amostragem casual simples, é necessário enumerar todos os elementos da população e, em seguida, selecionar aleatoriamente um número entre 1 e o tamanho da população. Os elementos correspondentes aos números selecionados serão os membros da amostra.

### Amostragem sistemática

A amostragem sistemática é um método de amostragem probabilística em que os elementos da amostra são selecionados a intervalos regulares da população. Para realizar uma amostragem sistemática, é necessário primeiro dividir a população em intervalos iguais. Em seguida, um número aleatório entre 1 e o intervalo é selecionado. Os elementos da população que correspondem aos números selecionados serão os membros da amostra.

### Amostragem proporcional estratificada

A amostragem proporcional estratificada é um método de amostragem probabilística em que a população é dividida em estratos com base em características relevantes. Em seguida, uma amostra aleatória simples é selecionada de cada estrato. O tamanho da amostra em cada estrato é proporcional ao tamanho do estrato na população.

## Requisitos

- `Python 3.10` ou superior.
- Instalar a biblioteca `rich` (para visualização de tabelas).
  - Adicionado uma alternava para visualização de dados sem tabela.
    > Ainda recomendo que instale a biblioteca `rich`
