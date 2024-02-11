import numpy as np

class State:
    def __init__(self, board: np.ndarray, level=0, parent=None, move=None):
        self.board = board
        self.level = level
        self.score = level
        self.parent=parent
        self.move = move
        x, y = np.where(board=='0') #keep track of where 0 is
        self.blank_x, self.blank_y = int(x), int(y)

    def __eq__(self, other):
        return self.score==other.score
    
    def __ne__(self, other):
        return self.score!=other.score
    
    def __lt__(self, other):
        return self.score < other.score

    def __gt__(self, other):
        return self.score > other.score

    def __ge__(self, other):
        return self.score >= other.score
    def __le__(self, other):
        return self.score <= other.score
    
    #updates and/or get cost method
    def getCost(self, addBy=0):
        self.score += addBy #adds to the cost, will be used for updating with heuristic in case of Astar
        return self.score
    def getParent(self):
        return self.parent
    def getMove(self):
        return self.move

    

    

    
    
