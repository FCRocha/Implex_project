import Hill_Climbing as HC
import Simulated_Annealing as SA

if __name__ == '__main__':
    paths = ['Data_input/att48.tsp.txt',
             'Data_input/berlin52.tsp.txt',
             'Data_input/bier127.tsp.txt',
             'Data_input/eil76.tsp.txt',
             'Data_input/kroA100.tsp.txt',
             'Data_input/pr76.tsp.txt',
             'Data_input/rat99.tsp.txt',
             'Data_input/st70.tsp.txt']
             
    
    Tmax = int(input('Digite a Temperatura inicial(Tmax): '))
    Tmin = int(input('Digite a Temperatura final(Tmin): '))
    k = float(input('Digite a Razão de resfriamento(k): '))
    iteracoes = int(input('Digite a Quantidade de iterações(Kt): '))

    for path in paths:
        print('.................................................')
        print('File:', path)

        iteracoes_int = int(iteracoes)

        solutionSA, iteracoes = SA.run(path, Tmax, Tmin, k, iteracoes_int)
        print('\n###### Simulated Annealing ######')  
        print() 
        print('Distance:', iteracoes)
        print()
        print('Solution:', solutionSA)

        
        solution, iteracoes = HC.run(path)
        print('\n###### Hill-Climbing ######') 
        print()
        print('Distance:', iteracoes) 
        print()
        print('Solution:', solution)

    print('.................................................')

