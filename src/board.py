#board object

# - dimensions of board: X,Y - 2d array
# - End point - coordinates (x,y)
import numpy as np

class Board:

    def __init__(self, dim_x, dim_y, end_goal_coord):
        self.dim_x = dim_x
        self.dim_y = dim_y
        self.board = np.zeros(shape = (dim_x, dim_y))

        self.end_goal_coord = end_goal_coord

    def change_end_goal(self, new_coord):
        self.end_goal_coord = new_coord
