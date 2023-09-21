import heapq

class Nodo:
    def __init__(self, estado, costo, camino):
        self.estado = estado  # El estado actual del nodo
        self.costo = costo    # El costo acumulado para llegar a este nodo
        self.camino = camino  # El camino acumulado desde el nodo inicial hasta este nodo

    def __lt__(self, otro):
        return self.costo < otro.costo

def busqueda_uniforme(grafo, inicio, objetivo):
    # Inicializar la cola de prioridad con el nodo de inicio
    cola_prioridad = []
    heapq.heappush(cola_prioridad, Nodo(inicio, 0, [inicio]))

    # Inicializar un conjunto de nodos visitados
    visitados = set()

    while cola_prioridad:
        # Extraer el nodo de la cola de prioridad
        nodo_actual = heapq.heappop(cola_prioridad)

        # Verificar si hemos alcanzado el nodo objetivo
        if nodo_actual.estado == objetivo:
            return nodo_actual.camino

        # Marcar el nodo como visitado
        visitados.add(nodo_actual.estado)

        # Expandir el nodo y agregar sus sucesores a la cola de prioridad
        for sucesor, costo in grafo[nodo_actual.estado].items():
            if sucesor not in visitados:
                nuevo_costo = nodo_actual.costo + costo
                nuevo_camino = nodo_actual.camino + [sucesor]
                heapq.heappush(cola_prioridad, Nodo(sucesor, nuevo_costo, nuevo_camino))

    # Si no se encuentra un camino, retornar None
    return None

# Ejemplo de uso
grafo = {
    'A': {'B': 7, 'E': 4,'X':21},
    'B': {'A': 7, 'C': 1, 'D': 3,'F':7},
    'E': {'A': 4, 'F': 6},
    'C': {'B': 1, 'D': 5},
    'D': {'B': 3, 'C': 5, 'X': 4},
    'F': {'B': 7, 'E': 6, 'X': 8},
    'X': {'D': 4, 'F': 8, 'A': 27}
}

inicio = 'A'
objetivo = 'X'
resultado = busqueda_uniforme(grafo, inicio, objetivo)

if resultado:
    print(f"El camino más corto desde {inicio} a {objetivo} es: {resultado} con costo total {len(resultado) - 1}")
else:
    print(f"No se encontró un camino desde {inicio} a {objetivo}")
