import sys
import itertools
disjunction = lambda *args: any(args)



def find_pure(clauses):
    pure = {}
    reached = []
    for clause in clauses:
        for lit in clause:
            if lit[0]=='~':
                if lit[1:] in pure.keys():
                    if pure[lit[1:]]!=False:
                        del pure[lit[1:]]
                elif lit[1:] not in reached:
                    pure[lit[1:]]=False
                    reached.append(lit)
            else:
                if lit in pure.keys():
                    if pure[lit]!=True:
                        del pure[lit]
                elif lit not in reached:
                    pure[lit]=True
                    reached.append(lit)
    
    #add the clause index where index = find(pure)
    '''listOfRemovals = []
    for j in range(len(clauses)):'''

    
    return pure


def unit_heuristic(clauses, assignment):
    clauses2 = clauses.copy()
    for i in range(len(clauses2)):
        clause = clauses2[i]
        if len(clause)==1:
            c = clause[0] 
            if c[0]=="~":
                #add to assignment if it does not exist, if it exists, then it must be from contradicting unit clauses and it is unsat
                if c[1:] in assignment and assignment[c[1:]]!=False:
                    #stands for unsatisfiable
                    return None, None 
                elif c[1:] not in assignment:
                    assignment[c[1:]] = False     
            
            else:
                if c in assignment and assignment[c]!=True:
                    return None, None #stands for unsatisfiable
                elif c not in assignment:
                    assignment[c] = True
            
            #remove clause
            clauses2[i] = None
    
    updated_clauses = [i for i in clauses2 if i is not None]
                    
    return assignment, updated_clauses



#extract literals, clauses and pure literals

def extract(lines):
    literals = set()
    pure = dict() #assignments to pure
    clauses = []
    clause_idx = 0
    
    for line in lines:
    #each clause is a disjunction in cnf form
        clause = []
        for c in line.split(','):
            literals.add(c if c[0]!='~' else c[1:]) #add positive literal only
            clause.append(c)
        clauses.append(clause)

    return list(literals), clauses

#given an assignment, check if assignment returns True for the clauses
def isSat(clauses, assignment):
    for c in clauses:
        clause = []
        for literal in c:
            if literal[0]=='~':
                clause.append(not assignment[literal[1:]])
            else: 
                clause.append(assignment[literal])             
        #if any disjunction is False, the entire CNF expression will be false
        if disjunction(*clause) is False:
            return False
    return True


def DPLL(clauses, literals, model,length):
    if len(literals)==0: #all assigned
        #find if model is satisfiable with current clauses #satisfiable should return True or False
        if isSat(clauses, model):
            return model
        else:
            return None 
    
    unit_assign, updated_clauses = unit_heuristic(clauses, model)
    if unit_assign is None:
        return None
    
    pure = find_pure(updated_clauses)

    #print(unit_assign)
    d3 = {}
    d3.update(pure)
    #print("after pure", d3)
    d3.update(unit_assign)
    #print("after unit", d3)
    d3.update(model)
    #print("after model", d3)


    if len(d3)==length:
        if isSat(clauses,d3):
            return d3
        else:
            return None

    rest = [i for i in literals if i not in d3.keys()] #unassigned_keys
    first = rest.pop()

    
    return DPLL(updated_clauses, rest, {**d3, **{first:True}}, length) or DPLL(updated_clauses, rest, {**d3, **{first:False}}, length)




######### main

def main():
    inputLines = sys.stdin.read().splitlines()
    literals, clauses = extract(inputLines)
    length = len(literals)
    ans = DPLL(clauses,literals, {}, length)
    if ans:
        print("satisfiable", end = " ")
        for key in ans.keys():
            print(key+'='+str(ans.get(key))[0],end=' ')
        print()
    else:
        print("unsatisfiable")

main()

