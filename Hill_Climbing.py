import Utils
import random

def solutionDistance(graph, solution):
    distance = 0
    for i in range(len(solution) - 1):
        distance += graph.distanceBetweenVertices(solution[i], solution[i+1])
    return distance

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

    solution = random.sample(cities, len(cities))
    distance = solutionDistance(graph, solution)
    neighbours = getNeighbours(solution)

    while neighbours:
        bestNeighbour = min(neighbours, key=lambda x: solutionDistance(graph, x))
        bestNeighbourDistance = solutionDistance(graph, bestNeighbour)

        if bestNeighbourDistance < distance:
            solution = bestNeighbour
            distance = bestNeighbourDistance
            neighbours = getNeighbours(solution)
        else:
            break

    return solution, distance
