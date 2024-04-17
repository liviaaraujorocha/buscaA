import heapq

def busca_a_estrela(grafo, inicio, objetivo, heuristica):
    fila_prioridade = []
    heapq.heappush(fila_prioridade, (0, inicio, [inicio]))
    visitados = set([inicio])
    
    while fila_prioridade:
        (_, vertice, caminho) = heapq.heappop(fila_prioridade)
        if vertice == objetivo:
            return caminho
        for proximo_vertice in grafo[vertice]:
            if proximo_vertice not in visitados:
                visitados.add(proximo_vertice)
                novo_caminho = caminho + [proximo_vertice]
                custo = len(novo_caminho) + heuristica(proximo_vertice, objetivo)
                heapq.heappush(fila_prioridade, (custo, proximo_vertice, novo_caminho))

# Função heurística simples - distância em linha reta
def heuristica_distancia_em_linha_reta(vertice, objetivo):
    return abs(vertice[0] - objetivo[0]) + abs(vertice[1] - objetivo[1])

# Exemplo de uso
grafo = {
    (0, 0): [(1, 0), (0, 1)],
    (1, 0): [(0, 0), (2, 0)],
    (0, 1): [(0, 0), (0, 2)],
    (0, 2): [(0, 1), (1, 2)],
    (1, 2): [(0, 2), (2, 2)],
    (2, 0): [(1, 0), (2, 1)],
    (2, 1): [(2, 0), (2, 2)],
    (2, 2): [(1, 2), (2, 1)]
}

inicio = (0, 0)
objetivo = (2, 2)
caminho = busca_a_estrela(grafo, inicio, objetivo, heuristica_distancia_em_linha_reta)
print("Caminho encontrado:", caminho)
