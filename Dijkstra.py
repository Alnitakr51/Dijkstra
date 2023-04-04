# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 09:02:26 2023

@author: Gadiel Jimenez
"""

import sys

class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = [[0 for columna in range(vertices)] 
                      for fila in range(vertices)]

    def imprimir_solucion(self, distancias):
        print("Vertice \tDistancia desde el origen")
        for nodo in range(self.V):
            print(nodo, "\t\t", distancias[nodo])

    def distancia_minima(self, distancias, vertices_visitados):
        min_distancia = sys.maxsize
        for v in range(self.V):
            if distancias[v] < min_distancia and vertices_visitados[v] == False:
                min_distancia = distancias[v]
                nodo_minimo = v
        return nodo_minimo

    def dijkstra(self, nodo_origen):
        distancias = [sys.maxsize] * self.V
        distancias[nodo_origen] = 0
        vertices_visitados = [False] * self.V

        for _ in range(self.V):
            nodo_actual = self.distancia_minima(distancias, vertices_visitados)
            vertices_visitados[nodo_actual] = True
            for v in range(self.V):
                if self.grafo[nodo_actual][v] > 0 and vertices_visitados[v] == False and \
                   distancias[v] > distancias[nodo_actual] + self.grafo[nodo_actual][v]:
                    distancias[v] = distancias[nodo_actual] + self.grafo[nodo_actual][v]

        self.imprimir_solucion(distancias)

# Ejemplo de uso
g = Grafo(9)
g.grafo = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]]

g.dijkstra(0)
