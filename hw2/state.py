import numpy as np

class State:
    def __init__(self, board: np.ndarray, level=0, parent=None, move=None):
        self.board = board
        self.level = level
        self.cost = level
        self.parent=parent
        self.move = move #"up", "down", "left", "right"
        x, y = np.where(board=='0') #keep track of where 0 is
        self.blank_x, self.blank_y = int(x), int(y)

    #defining hash function for HashMap / Python Dict
    def __hash__(self) -> int:
        return hash(str(self))

    #defining custom comparators for Priority Queue
    def __eq__(self, other):
        return self.cost==other.cost
    
    def __ne__(self, other):
        return self.cost!=other.cost
    
    def __lt__(self, other):
        return self.cost < other.cost

    def __gt__(self, other):
        return self.cost > other.cost

    def __ge__(self, other):
        return self.cost >= other.cost
    def __le__(self, other):
        return self.cost <= other.cost
    
    #updates and/or gets cost method
    def getCost(self, addBy=0):
        self.cost += addBy #adds to the cost, will be used for updating with heuristic in case of Astar
        return self.cost
    def getParent(self):
        return self.parent
    def getMove(self):
        return self.move

    

    

    
    
