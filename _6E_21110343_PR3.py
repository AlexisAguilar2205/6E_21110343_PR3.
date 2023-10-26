
import sys

class Grafo:
    def __init__(self):
        self.vertices = set()
        self.aristas = {}

    def agregar_vertice(self, valor):
        self.vertices.add(valor)
        if valor not in self.aristas:
            self.aristas[valor] = {}

    def agregar_arista(self, desde, hacia, peso):
        self.aristas[desde][hacia] = peso

def dijkstra(grafo, inicio):
    distancia = {vertice: sys.maxsize for vertice in grafo.vertices}
    distancia[inicio] = 0
    visitados = set()

    while visitados != grafo.vertices:
        vertice_actual = None
        for vertice in grafo.vertices:
            if vertice not in visitados:
                if vertice_actual is None:
                    vertice_actual = vertice
                elif distancia[vertice] < distancia[vertice_actual]:
                    vertice_actual = vertice

        if distancia[vertice_actual] == sys.maxsize:
            break

        visitados.add(vertice_actual)
        for vecino, peso in grafo.aristas[vertice_actual].items():
            if distancia[vertice_actual] + peso < distancia[vecino]:
                distancia[vecino] = distancia[vertice_actual] + peso

    return distancia

# Ejemplo de uso
grafo = Grafo()

grafo.agregar_vertice("A")
grafo.agregar_vertice("B")
grafo.agregar_vertice("C")
grafo.agregar_vertice("D")

grafo.agregar_arista("A", "B", 1)
grafo.agregar_arista("A", "C", 4)
grafo.agregar_arista("B", "C", 2)
grafo.agregar_arista("B", "D", 5)
grafo.agregar_arista("C", "D", 1)

inicio = "A"
resultados = dijkstra(grafo, inicio)

for vertice, distancia in resultados.items():
    print(f"Distancia desde {inicio} a {vertice}: {distancia}")