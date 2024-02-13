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
    '''
    heuristic means use heuristic to count cost
    goal_digit_pos is a HashMap of row-column values for each digit's position on the game board, represented by a numpy array.
    if we need heuristic, we compute "manhattan heuristic" and add it to cost
    '''
    def getCost(self, heuristic=False, goal_digit_pos:dict={}):

        manhattan = 0 #default manhattan val
        if heuristic and len(goal_digit_pos)!=0:
           for i in self.board.flatten().tolist():
               x2, y2 = np.where(self.board==i)
               x2, y2 = int(x2), int(y2)
               manhattan+= abs(x2-goal_digit_pos[i][0]) +  abs(y2-goal_digit_pos[i][1])
        self.cost+=manhattan
           
        return self.cost
        
    def getParent(self):
        return self.parent
    def getMove(self):
        return self.move

    

    

    
    
