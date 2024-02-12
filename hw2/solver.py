from Puzzle import *
import sys
class Solver:

    def evaluate_heuristic(x1, x2, y1, y2, heuristic=0):
        if heuristic=='manhattan':
            return abs(y2-y1)+abs(x2-x1)
        return 0
    
    def main():
        size = sys.stdin.readline().strip('\n')
        for line in sys.stdin.readlines():
            print(line)

        '''arr = np.array([['1','2', '5'],
                       ['3', '4', '8'],
                       ['6','7','0']])
        initial_state = State(arr)
        puzzle = Puzzle(initial_state, size=3)  
        path = puzzle.BFS()
        while len(path)!=0:
            print(path.pop(), sep=" ")'''

    if __name__ == main:
        main() 

    
    