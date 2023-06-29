import numpy as np
import Utils as Utils
import random


def solutionDistance(graph, solution):
    distance = 0
    for i in range(len(solution) - 1):
        distance += graph.distanceBetweenVertices(solution[i], solution[i + 1])
    return distance


def randomSolution(graph):
    cities = graph.getAllVerticesIndex().tolist()
    solution = random.sample(cities, len(cities))
    return solution


def run(path, Tmax, Tmin, k, iterations):
    graph = Utils.creatGraph(path)
    T = Tmax

    # Ponto corrente de forma randomica
    solution = randomSolution(graph)

    # Simulated Annealing
    cost0 = solutionDistance(graph, solution)

    while T > Tmin:
        for _ in range(iterations):
            # Troca duas coordenadas e obtém a solução vizinha
            r1, r2 = np.random.randint(0, len(solution), size=2)
            new_solution = solution.copy()
            new_solution[r1], new_solution[r2] = new_solution[r2], new_solution[r1]

            # Calcula o custo da nova solução
            new_cost = solutionDistance(graph, new_solution)

            if new_cost < cost0:
                # Aceita a nova solução se o custo for menor
                solution = new_solution
                cost0 = new_cost
            else:
                # Calcula a probabilidade de aceitar a nova solução com base na temperatura
                probability = np.exp((cost0 - new_cost) / T)
                if random.random() < probability:
                    # Aceita a nova solução com base na probabilidade
                    solution = new_solution
                    cost0 = new_cost

        T *= k

    return solution, cost0
