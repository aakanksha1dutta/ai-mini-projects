import sys, copy
from state import *


class Puzzle:
    #initialize the puzzle with initial state, size and goal state
    def __init__(self, initial: State, size:int):
        self.initial = initial #initial state
        self.size = size #size of the puzzle like nxn
        self.goal = State(np.arange(size*size).reshape(size,size))  #goal state


    def initialBoards(self):
        return self.initial
    
    
    def isGoal(self,someState : State):
        return someState.board==self.goal.board
    
    def action(self, s: State, a: str):
        return None
        
            

        




                

        
        

    

size = int(sys.stdin.readline().strip('\n'))



