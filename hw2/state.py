import numpy as np

class State:
    def __init__(self, board: np.ndarray, level=0, heuristic=0):
        self.board = board
        self.cost = level+heuristic
        #self.blank_pos = np.where(board=='0') #keep track of where 0 is
    def getCost(self):
        return self.cost
    
