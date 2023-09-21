# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 08:32:29 2023

@author: Katia
"""

import networkx as nx #Es un libreria que sirve para crea un gráfico vacío sin nodos ni aristas.

# Crear un grafo dirigido ponderado
G = nx.Graph()

# Agregar nodos al grafo
G.add_node('A')
G.add_node('B')
G.add_node('C')
G.add_node('D')
G.add_node('E')
G.add_node('F')
G.add_node('X')

# Agregar bordes ponderados al grafo
G.add_edge('A', 'B', weight=7)
G.add_edge('A', 'E', weight=4)
G.add_edge('A', 'X', weight=27)
G.add_edge('B', 'C', weight=1)
G.add_edge('B', 'D', weight=3)
G.add_edge('B', 'F', weight=7)
G.add_edge('C', 'D', weight=5)
G.add_edge('D', 'X', weight=4)
G.add_edge('E', 'F', weight=6)
G.add_edge('F', 'X', weight=8)

# Realizar la búsqueda por costo uniforme desde A a E
inicio = 'A'
objetivo = 'X'
ruta = nx.shortest_path(G, source=inicio, target=objetivo, weight='weight', method='dijkstra')
#shortest_path es el que calcula los caminos más cortos en el gráfico.
#source es donde indicamos el nodo inicial
#target es donde indicamos el nodo final


# Calcular el costo total de la ruta
costo_total = nx.shortest_path_length(G, source=inicio, target=objetivo, weight='weight', method='dijkstra')
#shortest_path_length es el que calcula las longitudes de camino más cortas en el gráfico.
#source es donde indicamos el nodo inicial
#target es donde indicamos el nodo final

if ruta:
    print("Ruta encontrada:", ruta)
    print("Costo total:", costo_total)
else:
    print("No se encontró una ruta desde", inicio, "hasta", objetivo)
