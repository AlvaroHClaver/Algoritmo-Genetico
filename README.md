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

O **problema da mochila** consiste em escolher, entre um conjunto de itens (cada um com um peso e um valor), quais itens levar para maximizar o valor total sem exceder a capacidade máxima permitida da mochila.

No código, cada solução é representada por uma lista de bits (0 ou 1), onde cada posição indica se o item correspondente é incluído ou não. A função de aptidão calcula o valor total dos itens escolhidos, mas só considera soluções válidas (onde o peso total não passa da capacidade). O algoritmo cria uma população inicial de soluções aleatórias e, por meio de **seleção** (escolhendo as melhores opções), **cruzamento** (combinando partes de duas soluções) e **mutação** (alterando aleatoriamente alguns bits), vai gerando novas soluções. Ao final, o algoritmo retorna a melhor solução encontrada, ou seja, a combinação de itens que oferece o maior valor sem ultrapassar o limite de peso.
