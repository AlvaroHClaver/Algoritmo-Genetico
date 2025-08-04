# Algoritmo-Genetico

Algoritmos Genéticos  são técnicas de otimização inspiradas na evolução natural. Eles simulam o processo de seleção natural através dos seguintes conceitos fundamentais:

- População: Conjunto de soluções candidatas
- Seleção : Processo de escolha dos indivíduos mais aptos para participarem do cruzamento, favorecendo os melhores candidatos.
- Recombinação: Nesse operador, dois indivíduos (pais) são combinados para criar descendentes. A recombinação mistura partes dos cromossomos dos pais, permitindo que características positivas de ambos sejam combinadas em novos indivíduos, potencialmente gerando soluções melhores.
- Mutação: Mantém a diversidade na população e evitar que o algoritmo fique preso em ótimos locais, permitindo a exploração de novas regiões do espaço de soluções.
- Elitismo: Mecanismo garante que os melhores indivíduos encontrados até o momento sejam preservados para a próxima geração.

**Problemas de roteamento**: Roteamento de veículos, roteamento de redes, design de sistemas de distribuição.

Aplicar um algoritmo genético para problemas de roteamento envolve representar cada rota como um cromossomo e avaliar sua qualidade com uma função de aptidão que considera distância, tempo, custos e restrições. Aplicando operadores como seleção, cruzamento, mutação e elitismo, o algoritmo evolui uma população de soluções ao longo de várias gerações, aprimorando as rotas e aproximando-se do ótimo.

**Problemas de Agendamento**: Escalonamento de tarefas, programação de produção, programação de pessoal

Cada solução é representada como uma sequência (ou cromossomo) que determina a ordem dos eventos, enquanto uma função de aptidão avalia critérios essenciais, como a minimização do tempo total, a redução de atrasos e o balanceamento da carga de trabalho, levando em conta restrições operacionais.

**Otimização de Parâmetros:** Encontrar valores ótimos para parâmetros

Ao pensar na otimização de parâmetros como "carregar uma mochila", cada parâmetro pode ser visto como um item que contribui com um valor específico e possui um custo ou "peso". O objetivo, então, é selecionar a combinação ideal de parâmetros (ou itens) que maximize a performance do modelo ou sistema sem exceder uma determinada capacidade, semelhante a como se escolhe itens para maximizar o valor total sem ultrapassar o limite de peso da mochila. 

As principais vantagens dos algoritmos genéticos são explorar espaços de solução complexos e não lineares, lidar com múltiplos objetivos e encontrar soluções aproximadas para problemas difíceis.

```
import random

# Definição dos itens (peso, valor) e capacidade máxima da mochila
itens = [(12, 4), (2, 2), (1, 2), (1, 1), (4, 10)]
capacidade = 15

# Parâmetros do algoritmo
tam_pop = 20      # Tamanho da população
geracoes = 50     # Número de gerações
taxa_mut = 0.1    # Taxa de mutação

# Cria um indivíduo representado por uma lista de 0s e 1s
def cria_individuo():
    return [random.randint(0, 1) for _ in itens]

# Calcula a aptidão do indivíduo: soma dos valores se o peso não exceder a capacidade, caso contrário 0
def aptidao(ind):
    peso = sum(g * i[0] for g, i in zip(ind, itens))
    valor = sum(g * i[1] for g, i in zip(ind, itens))
    return valor if peso <= capacidade else 0

# Seleção por torneio: escolhe o melhor dentre três indivíduos aleatórios
def seleciona(pop):
    candidatos = random.sample(pop, 3)
    return max(candidatos, key=aptidao)

# Crossover de um ponto: combina dois pais para criar um novo indivíduo
def cruzamento(p1, p2):
    ponto = random.randint(1, len(itens)-1)
    return p1[:ponto] + p2[ponto:]

# Mutação: inverte um gene (0 para 1 ou 1 para 0) com uma probabilidade definida
def mutacao(ind):
    return [1 - gene if random.random() < taxa_mut else gene for gene in ind]

# Algoritmo genético principal
def ga():
    pop = [cria_individuo() for _ in range(tam_pop)]
    melhor = max(pop, key=aptidao)
    for _ in range(geracoes):
        nova_pop = []
        for _ in range(tam_pop):
            p1 = seleciona(pop)
            p2 = seleciona(pop)
            filho = cruzamento(p1, p2)
            filho = mutacao(filho)
            nova_pop.append(filho)
        pop = nova_pop
        atual = max(pop, key=aptidao)
        if aptidao(atual) > aptidao(melhor):
            melhor = atual
    return melhor, aptidao(melhor)

melhor_solucao, melhor_valor = ga()
peso_total = sum(g * i[0] for g, i in zip(melhor_solucao, itens))

print("Melhor solução:", melhor_solucao)
print("Valor total:", melhor_valor)
print("Peso total:", peso_total)
```

O **problema da mochila** consiste em escolher, entre um conjunto de itens (cada um com um peso e um valor), quais itens levar para maximizar o valor total sem exceder a capacidade máxima permitida da mochila.

No código, cada solução é representada por uma lista de bits (0 ou 1), onde cada posição indica se o item correspondente é incluído ou não. A função de aptidão calcula o valor total dos itens escolhidos, mas só considera soluções válidas (onde o peso total não passa da capacidade). O algoritmo cria uma população inicial de soluções aleatórias e, por meio de **seleção** (escolhendo as melhores opções), **cruzamento** (combinando partes de duas soluções) e **mutação** (alterando aleatoriamente alguns bits), vai gerando novas soluções. Ao final, o algoritmo retorna a melhor solução encontrada, ou seja, a combinação de itens que oferece o maior valor sem ultrapassar o limite de peso.
