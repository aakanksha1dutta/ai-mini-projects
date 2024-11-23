from game import *
import sys
class Puzzle:
    
    def main():
        args = sys.argv[1:]
        method = args[0].lstrip('--')
        size = int(sys.stdin.readline().rstrip()) #remove the \n character using rstrip
        input_arr = []
        '''
        print("Taking in input....")
        print()
        print(f"The size of the array is {size}*{size}:")
        print("Your input:")
        '''

        for line in sys.stdin.readlines():
            l = line.rstrip()
            #print(l)
            input_arr.append(l.split(' ')) #appends a row of elements
        
        

        arr = np.array(input_arr)
        initial_state = State(arr)
        game = Game(initial_state, size=size) 
        path = game.search(method=method)
        while len(path)!=0:
            print(path.pop(), sep=" ")

    if __name__ == "__main__":
        main() 

    
    