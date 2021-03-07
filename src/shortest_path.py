#Steps in GA:

# 1. Initialize population 
# 2. Calculate fitness
# 3. Selection 
# 4. Crossover
# 5. Mutation

#Repeat from 2.

import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append(".")

from board import Board
from chromosone import Chromosone

# we start off with a fixed start and end location. The goal is to get from the start to the end in as few moves possible.
# For now: a 20 x 20 board
# Start point: (10,0) (x,y)
# End point: (10,20)

def main():
    board_1 = Board(20, 20, (10,20)) 

    #init population and genes
    population_size = 100
    population = []
    for _ in range(population_size):
        chrom = Chromosone()
        chrom.init_genes(board_1)
        chrom.calc_fitness(board_1)
        population.append(chrom)

    # select best 10 chromosones
    fitness_all = [(chrom.get_fitness(), chrom) for chrom in population]
    top_chroms = sorted(fitness_all, key=lambda x: x[0])[:10]

    #crossover
    new_population = []
    parent_1 = top_chroms[0][1]
    parent_2 = top_chroms[1][1]

    child = parent_1.crossover(parent_2) 
    new_population.append(child)

    # test
    new_population.append(parent_1)
    new_population.append(parent_2)

    print(child.genes)

    plot_population(board_1,new_population)

def plot_population(board, population):
    
    plt.plot(board.end_goal_coord[0], board.end_goal_coord[1], 'mo')
    col = 'b'
    count = 0
    for c in population:
        count +=1
        chrom_genes = c.genes
        x = [i for i, _ in chrom_genes] 
        y = [j for _, j in chrom_genes] 

        start_x = c.start_point[0]
        start_y = c.start_point[1]
        
        end_x = c.end_point[0]
        end_y = c.end_point[1]

        if count == 2:
            col = 'r'

        if count == 3:
            col = 'y'
 

        plt.plot(x, y, color = col)
        plt.plot(start_x, start_y, 'bo')
        plt.plot(end_x, end_y, 'go')
    plt.show()
    



if __name__ == "__main__":
    main()

