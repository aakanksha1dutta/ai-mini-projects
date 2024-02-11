class Solver:



    def evaluate_heuristic(x1, x2, y1, y2, heuristic=0):
        if heuristic=='manhattan':
            return abs(y2-y1)+abs(x2-x1)
        return 0