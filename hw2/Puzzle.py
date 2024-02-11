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
    
    def action(self, s: State, a: str)-> State:
        s_arr = s.board.flatten().tolist() #the puzzle as a 1d array
        if a=='U' and s.blank_x>0:
            #swap
            s_arr[self.size * (s.blank_x) + s.blank_y], s_arr[self.size * (s.blank_x-1) + s.blank_y] = s_arr[self.size * (s.blank_x-1) + s.blank_y], s_arr[self.size * (s.blank_x) + s.blank_y]
            return State(np.array(s_arr), level=s.level+1)


        return None
        
            

        




                

        
        

    

size = int(sys.stdin.readline().strip('\n'))



