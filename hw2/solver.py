from Puzzle import *
import sys
class Solver:

    def evaluate_heuristic(x1, x2, y1, y2, heuristic=0):
        if heuristic=='manhattan':
            return abs(y2-y1)+abs(x2-x1)
        return 0
    
    def main():
        size = sys.stdin.readline().rstrip()
        input_arr = []
        print("Taking in input....")
        print()
        print(f"The size of the array is {size}*{size}:")
        print("Your input:")

        for line in sys.stdin.readlines():
            l = line.rstrip()
            print(l)
            input_arr.append(l.split(' '))
        
        print()
        print("The fastest moves to the goal is:")
        

        arr = np.array(input_arr)
        initial_state = State(arr)
        puzzle = Puzzle(initial_state, size=3)  
        path = puzzle.BFS()
        while len(path)!=0:
            print(path.pop(), sep=" ")

    if __name__ == "__main__":
        main() 

    
    