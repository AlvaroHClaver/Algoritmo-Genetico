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
