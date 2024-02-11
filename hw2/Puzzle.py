from queue import PriorityQueue
import sys, copy
from state import *


class Puzzle:
    #initialize the puzzle with initial state, size and goal state
    def __init__(self, initial: State, size:int):
        self.initial = initial #initial state
        self.size = size #size of the puzzle like nxn
        self.goal = State(np.arange(size*size).reshape(size,size))  #goal state
        self.path = [] #Queue


    def initialBoards(self):
        return self.initial
    
    
    def isGoal(self,someState : State):
        return someState.board==self.goal.board
    
    def action(self, s: State, a: str)-> State:
        s_arr = s.board.flatten().tolist() #the puzzle as a 1d array
        if a=='U' and s.blank_x>0:
            #swap
            s_arr[self.size * (s.blank_x) + s.blank_y], s_arr[self.size * (s.blank_x-1) + s.blank_y] = s_arr[self.size * (s.blank_x-1) + s.blank_y], s_arr[self.size * (s.blank_x) + s.blank_y]
            return State(np.array(s_arr), level=s.level+1, parent=s)
        
        if a=='D' and s.blank_x>(size-1):
            s_arr[self.size * (s.blank_x) + s.blank_y], s_arr[self.size * (s.blank_x+1) + s.blank_y] = s_arr[self.size * (s.blank_x+1) + s.blank_y], s_arr[self.size * (s.blank_x) + s.blank_y]
            return State(np.array(s_arr), level=s.level-1, parent=s)
        
        if a=='L' and s.blank_y>0:
            s_arr[self.size * (s.blank_x) + s.blank_y], s_arr[self.size * (s.blank_x) + (s.blank_y-1)] = s_arr[self.size * (s.blank_x) + (s.blank_y-1)], s_arr[self.size * (s.blank_x) + s.blank_y]
            return State(np.array(s_arr), level=s.level, parent=s)
        
        if a=='R' and s.blank_y<(size-1):
            s_arr[self.size * (s.blank_x) + s.blank_y], s_arr[self.size * (s.blank_x) + (s.blank_y+1)] = s_arr[self.size * (s.blank_x) + (s.blank_y+1)], s_arr[self.size * (s.blank_x) + s.blank_y]
            return State(np.array(s_arr), level=s.level, parent=s)

        return None
        
    def BFS(self):

        if self.isGoal(self.initial):
            return self.path
        frontier = PriorityQueue(maxsize=100000)
        frontier.put(self.initial)
        reached = {self.initial: self.score}

        
        curr = frontier.get()
        while not self.isGoal(curr):
            up, down, left, right = self.action(curr, 'U'), self.action(curr, 'D'), self.action(curr, 'L'), self.action(curr, 'R')
            moves = [up, down, left, right]

            #rState: resulting state
            for rState in moves:
                if rState is not None and (curr not in dict.keys(reached) or reached[rState]>rState.getCost()):
                    reached[rState]=rState.getCost()
                    frontier.put(rState)
                    
            curr=frontier.get()

        

           

        




                

        
        

    

size = int(sys.stdin.readline().strip('\n'))



