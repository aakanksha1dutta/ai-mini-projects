from queue import PriorityQueue
from state import *


class Game:
    #initialize the puzzle with initial state, size and goal state
    def __init__(self, initial: State, size:int):
        self.initial = initial #initial state
        self.size = size #size of the puzzle like nxn
        self.goal = State(np.arange(size*size).astype(str).reshape(size,size))  #goal state 
        self.path=[] #stores the best moves
        self.goal_digit_pos = {}

        #maintain a Hashmap of Goal State's digits positions
        for i in range(size*size):
            x, y = np.where(self.goal.board==f"{i}")
            self.goal_digit_pos[f"{i}"] = (int(x), int(y))


    def initialBoards(self):
        return self.initial
    
    
    def isGoal(self,someState : State):
        return np.array_equal(someState.board, self.goal.board)
    
    #TODO: Add name of moves in State
    def action(self, s: State, a: str)-> State:
        s_arr = s.board.flatten().tolist() #the puzzle as a 1d array
        #level of child is parent.level+1
        if a=='U' and s.blank_x>0:
            #swap
            s_arr[self.size * (s.blank_x) + s.blank_y], s_arr[self.size * (s.blank_x-1) + s.blank_y] = s_arr[self.size * (s.blank_x-1) + s.blank_y], s_arr[self.size * (s.blank_x) + s.blank_y]
            return State(np.array(s_arr).reshape(self.size, self.size), level=s.level+1, parent=s, move="UP")
        
        if a=='D' and s.blank_x<(self.size-1):
            s_arr[self.size * (s.blank_x) + s.blank_y], s_arr[self.size * (s.blank_x+1) + s.blank_y] = s_arr[self.size * (s.blank_x+1) + s.blank_y], s_arr[self.size * (s.blank_x) + s.blank_y]
            return State(np.array(s_arr).reshape(self.size, self.size), level=s.level+1, parent=s, move="DOWN")
        
        if a=='L' and s.blank_y>0:
            s_arr[self.size * (s.blank_x) + s.blank_y], s_arr[self.size * (s.blank_x) + (s.blank_y-1)] = s_arr[self.size * (s.blank_x) + (s.blank_y-1)], s_arr[self.size * (s.blank_x) + s.blank_y]
            return State(np.array(s_arr).reshape(self.size, self.size), level=s.level+1, parent=s, move="LEFT")
        
        if a=='R' and s.blank_y<(self.size-1):
            s_arr[self.size * (s.blank_x) + s.blank_y], s_arr[self.size * (s.blank_x) + (s.blank_y+1)] = s_arr[self.size * (s.blank_x) + (s.blank_y+1)], s_arr[self.size * (s.blank_x) + s.blank_y]
            return State(np.array(s_arr).reshape(self.size, self.size), level=s.level+1, parent=s, move="RIGHT")

        return None

    #default is astar  
    def search(self, method):

        if self.isGoal(self.initial):
            return self.path
        frontier = PriorityQueue()
        if method=="astar":
            self.initial.getCost(True, self.goal_digit_pos) #calculate with heuristic if method is A-star
        frontier.put(self.initial)
        reached = {self.initial: self.initial.cost}


        expanded = 0 #count no of expanded nodes

        curr = frontier.get()
        while not self.isGoal(curr):

            up, down, left, right = self.action(curr, 'U'), self.action(curr, 'D'), self.action(curr, 'L'), self.action(curr, 'R')
            moves = [up, down, left, right]

            expanded+=1

            #rState: resulting state
            for rState in moves:
                if rState is not None:
                    #if astar, update cost to add manhattan heuristic
                    if method=="astar":
                        rState.getCost(True, self.goal_digit_pos)
                    if rState not in dict.keys(reached) or reached[rState]>rState.getCost():                    
                        reached[rState]=rState.getCost()
                        frontier.put(rState)
                    
            curr=frontier.get()
        
        #curr is goal
        while curr is not self.initial:
            self.path.append(curr.getMove())
            curr = curr.getParent()
        
        return self.path
        

    

  
   

           
        




                

        
        

    





