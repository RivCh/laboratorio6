import heapq

grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

heuristica = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 3,
    'E': 1,
    'F': 0
}

def a_star(inicio, objetivo):
    cola = [(0, inicio)]
    visitados = set()
    costos = {inicio: 0}
    padres = {inicio: None}

    while cola:
        prioridad_actual, actual = heapq.heappop(cola)

        if actual == objetivo:
            break

        if actual in visitados:
            continue

        visitados.add(actual)

        for vecino, costo in grafo[actual]:
            nuevo_costo = costos[actual] + costo

            if vecino not in costos or nuevo_costo < costos[vecino]:
                costos[vecino] = nuevo_costo
                # f(n) = g(n) + h(n)
                prioridad = nuevo_costo + heuristica[vecino]
                heapq.heappush(cola, (prioridad, vecino))
                padres[vecino] = actual

    return padres

nodo_inicial = 'A'
nodo_objetivo = 'F'

resultado_padres = a_star(nodo_inicial, nodo_objetivo)

def reconstruir_camino(padres, inicio, objetivo):
    camino = []
    actual = objetivo
    while actual is not None:
        camino.append(actual)
        actual = padres.get(actual)
    camino.reverse()
    return camino


camino_optimo = reconstruir_camino(resultado_padres, nodo_inicial, nodo_objetivo)

# Imprimir resultados solicitados en la guía
print("--- RESULTADOS DEL LABORATORIO ---")
print(f"Diccionario de padres generado: {resultado_padres}")
print(f"Camino óptimo encontrado de {nodo_inicial} a {nodo_objetivo}: {' -> '.join(camino_optimo)}")