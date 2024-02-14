from game import *
import sys
class puzzle:
    
    def main():
        size = int(sys.stdin.readline().rstrip()) #remove the \n character using rstrip
        input_arr = []
        print("Taking in input....")
        print()
        print(f"The size of the array is {size}*{size}:")
        print("Your input:")

        for line in sys.stdin.readlines():
            l = line.rstrip()
            print(l)
            input_arr.append(l.split(' ')) #appends a row of elements
        
        print()
        print("The fastest moves to the goal is:")
        

        arr = np.array(input_arr)
        initial_state = State(arr)
        game = Game(initial_state, size=size)  
        path = game.search() #def is BFS
        while len(path)!=0:
            print(path.pop(), sep=" ")

    if __name__ == "__main__":
        main() 

    
    