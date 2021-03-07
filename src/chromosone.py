#chromosone object
import board
import math
import numpy as np
import random

class Chromosone :
    start_point = (10,0)
    gene_size = 40

    def __init__(self):
        self.genes = [self.start_point]     #path
        self.fitness = -1
        self.end_point = (0,0)

    def calc_fitness(self, board):
        self.set_end_point()
        fit = (board.end_goal_coord[0] - self.end_point[0])**2 + (board.end_goal_coord[1] - self.end_point[1])**2
        self.fitness = math.sqrt(fit)

    def get_fitness(self):
        return self.fitness

    def set_end_point(self):
        self.end_point = self.genes[-1]

    def init_genes(self, board):

        for cur_step in range(self.gene_size):

            cur_x = self.genes[cur_step][0]
            cur_y = self.genes[cur_step][1]
            x = math.floor(random.random()*3) - 1 
            y = math.floor(random.random()*3) - 1 
            new_x = cur_x + x
            new_y = cur_y + y
            
            #still within board check
            if new_x < board.dim_x and new_y < board.dim_y and new_x >= 0 and new_y >= 0:
                self.genes.append((new_x, new_y))

            else:
                if new_x < 0 or new_x > board.dim_x:
                    new_x = cur_x
                
                if new_y < 0 or new_y > board.dim_y:
                    new_y = cur_y
                
                self.genes.append((new_x, new_y))

        self.set_end_point()


    def crossover(self, chromosone):
        #genes of chromosone = 1st half of chromesone 1 and 2nd half of chromesone 2
        new_chromosone = Chromosone()
        crossover_point = math.floor(random.random()*(self.gene_size - 1)) + 1

        new_genes_1 = self.genes[:crossover_point] #1st half of chrom1
        x_add = new_genes_1[-1][0] - chromosone.genes[crossover_point][0]  #x to be added to 2nd half of chrom2 (to connect the 2 paths)
        y_add = new_genes_1[-1][1] - chromosone.genes[crossover_point][1]  #y to be added to 2nd half of chrom2 (to connect the 2 paths)
        
        coord_add = (x_add, y_add)
        new_genes_2 = []
        for c in chromosone.genes[crossover_point:] :
            new_genes_2.append(tuple(np.add(c, coord_add)))
        
        new_chromosone.genes = new_genes_1 + new_genes_2
        print("crossover_point: ",crossover_point)
        new_chromosone.set_end_point()

        return new_chromosone

