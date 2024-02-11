import numpy as np

class State:
    def __init__(self, board: np.ndarray, level=0):
        self.board = board
        self.level = level
        self.score = level
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

    

    

    
    
