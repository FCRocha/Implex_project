import numpy as np
import math

#Tranforma os dados de TXT em um vetor Numpy
def generateVector(path):
    with open(path) as f_input:
        text = [" ".join(l.split()) for l in f_input]#remove espaços e tem como resultado lista de String

    vector = np.loadtxt(text, dtype=float, delimiter=" ").astype(int)

    return vector

#Cria e retorna um objeto Graph com base no vetor Numpy
def creatGraph(path):
    vector = generateVector(path)

    graph = Graph(vector)

    return graph


class Graph:
    def __init__(self, vector):
        self.vector = vector

    def distanceBetweenVertices(self, v1, v2):
        #Encontra as coordenadas  de v1 e v2
        coordsV1 = [self.vector[v1 - 1][1], self.vector[v1 - 1][2]]
        coordsV2 = [self.vector[v2 - 1][1], self.vector[v2 - 1][2]]
        #Calcula a distancia euclidiana entre v1 e v2
        d = math.sqrt(
            ((coordsV1[0] - coordsV2[0]) ** 2) + ((coordsV1[1] - coordsV2[1]) ** 2)
        )
        return d
    #Gera uma lista com as cooerdenadas dos vértices do grafo
    def getVerticeCoords(self, v):
        result = []
        for x_axis in range(v):
            for y_axis in range(v):
                result.append((x_axis, y_axis))
        return result
    #Retorna todos os index do grafo
    def getAllVerticesIndex(self):
        return self.vector[:, 0]