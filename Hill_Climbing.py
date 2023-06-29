import Utils as Utils
import random


def randomSolution(graph):
    cities = graph.getAllVerticesIndex().tolist()
    solution = []

    for i in range(len(graph.getAllVerticesIndex())):
        randomCity = cities[random.randint(0, len(cities) - 1)]
        solution.append(randomCity)
        cities.remove(randomCity)

    return solution


def solutionDistance(graph, solution):
    distance = 0
    for i in range(len(solution) - 1):
        distance += graph.distanceBetweenVertices(solution[i], solution[i+1])
    return distance


def getNeighbours(solution):
    neighbours = []
    for i in range(len(solution)):
        for j in range(i+1, len(solution)):
            neighbour = solution.copy()
            neighbour[i] = solution[j]
            neighbour[j] = solution[i]
            neighbours.append(neighbour)
    return neighbours


def getBestNeighbour(graph, neighbours):
    bestRouteLength = solutionDistance(graph, neighbours[0])
    bestNeighbour = neighbours[0]
    for neighbour in neighbours:
        currentRouteLength = solutionDistance(graph, neighbour)
        if currentRouteLength < bestRouteLength:
            bestRouteLength = currentRouteLength
            bestNeighbour = neighbour
    return bestNeighbour, bestRouteLength


def run(path):
    graph = Utils.creatGraph(path)

    solution = randomSolution(graph)
    distance = solutionDistance(graph, solution)
    neighbours = getNeighbours(solution)
    bestNeighbour, bestNeighbourDistance = getBestNeighbour(graph, neighbours)

    while bestNeighbourDistance < distance:
        solution = bestNeighbour
        distance = bestNeighbourDistance
        neighbours = getNeighbours(solution)
        bestNeighbour, bestNeighbourDistance = getBestNeighbour(
            graph, neighbours)

    return solution, distance
