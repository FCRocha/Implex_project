import Utils
import random
#Calcula a distância percorrida no grafo
def solutionDistance(graph, solution):
    distance = 0
    for i in range(len(solution) - 1):
        distance += graph.distanceBetweenVertices(solution[i], solution[i+1])
    return distance
#Armazena as cidades e um index (vizinhos)
def getNeighbours(solution):
    neighbours = []
    for i, city in enumerate(solution):
        for j in range(i+1, len(solution)):
            neighbour = solution.copy()
            neighbour[i] = solution[j]
            neighbour[j] = city
            neighbours.append(neighbour)
    return neighbours

def run(path):
    graph = Utils.creatGraph(path)
    cities = graph.getAllVerticesIndex().tolist()
    
    #Primeira cidade
    solution = random.sample(cities, len(cities))
    distance = solutionDistance(graph, solution)
    neighbours = getNeighbours(solution)

    while neighbours:
        #Calculo a distancia de cada vizinho para encontrar o melhor
        bestNeighbour = min(neighbours, key=lambda x: solutionDistance(graph, x))
        bestNeighbourDistance = solutionDistance(graph, bestNeighbour)

        #Comparo a distancia atual com a do melhor vizinho
        if bestNeighbourDistance < distance:
            solution = bestNeighbour
            distance = bestNeighbourDistance
            neighbours = getNeighbours(solution)
        else:
            break

    return solution, distance
