import sys
import itertools
disjunction = lambda *args: any(args)




def find_pure(clauses, assignment):
    pure = {}
    deleted = []
    for clause in clauses:
        for lit in clause:
            if lit[0]=='~':
                c = lit[1:]
                if c in assignment:
                    continue
                
                elif c in pure:
                    if pure[c]!=False:
                        del pure[c]
                        deleted.append(c)

                elif c not in deleted:
                    pure[c]=False
                    
            else:
                if lit in assignment:
                    continue
                elif lit in pure:
                    if pure[lit]!=True:
                        del pure[lit]
                        deleted.append(lit)
                elif lit not in deleted:
                    pure[lit]=True
    
    #add the clause index where index = find(pure)
    '''listOfRemovals = []
    for j in range(len(clauses)):'''

    
    return pure

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

#extract literals, clauses
def extract(lines):
    literals = set()
    clauses = []
    
    for line in lines:
    #each clause is a disjunction in cnf form
        clause = []
        for c in line.split(','):
            literals.add(c if c[0]!='~' else c[1:]) #add positive literal only
            clause.append(c)
        clauses.append(clause)

    return list(literals), clauses

def allLiteralsinAssign(clause, assignment):
    withoutsigns = []
    for lit in clause:
        if lit[0]=='~':
            if lit[1:] not in assignment:
                return False
        else:
            if lit not in assignment:
                return False
    return True
       
#early termination
#given some clauses and incomplete assignments, is it enough to conclude true or false?
#if yes, return the assignment. if no, None.
def isClauseTrue(clauses, assignment):
    if len(clauses)==0 or len(assignment)==0:
        return None
    
    for clause in clauses:
        clause_isTrue = False
        
        for literal in clause:
            if literal[0]=='~':
                c = literal[1:]
                if c in assignment and assignment[c]==False:
                    clause_isTrue = True
                    break
            else:
                if literal in assignment and assignment[literal]==True:
                    clause_isTrue=True
                    break
                
        if clause_isTrue is False:
            return None
    return assignment

def isAnyClauseFalse(clauses, assignment):
    if len(clauses)==0 :
        return False
    if len(assignment)==0:
        return False
    
    #for each clause
    for clause in clauses:
        truth_val = []
        #check if all literals in clause are in assignment
        if allLiteralsinAssign(clause, assignment):
            for literal in clause:
                if literal[0]=='~':
                    truth_val.append(not assignment[literal[1:]])
                else: 
                    truth_val.append(assignment[literal])             
        #if any disjunction is False, the entire CNF expression will be false
            if disjunction(*truth_val) is False:
                return True #clause is False
    return False #cannot determine

                    


def DPLL(clauses, literals, model,length,doUnit=True, doPure=True):

    if len(literals)==0: #all assigned
        #find if model is satisfiable with current clauses #satisfiable should return True or False
        if isSat(clauses, model):
            return model
        else:
            return None
   
    else:
        #else, does the assignment entail True?
        entailTrue = isClauseTrue(clauses, model)
        if entailTrue:
            #assign the unassigned literals, here literals, to True
            return  {**model, **(dict.fromkeys(literals, True))}

        entailFalse = isAnyClauseFalse(clauses,model)
        if entailFalse:
            return None
        

    #if doUnit only before recursion or first iteration
    if doUnit and model=={}:
        unit_assign, updated_clauses = unit_heuristic(clauses, {})
        if unit_assign is None:
            return None
        model.update(unit_assign)
        clauses = updated_clauses
    
    #only check pure for first iteration
    if doPure and model=={}:
        pure = find_pure(clauses, model)
        model.update(pure)



    if len(model)==length:
        #print("STUCK AT SAT")
        #print()
        if isSat(clauses,model):
            return model
        else:
            return None

    rest = [i for i in literals if i not in model.keys()]     #unassigned_keys
    first = rest.pop()


    
    return DPLL(clauses, rest, {**model, **{first:True}}, length) or DPLL(clauses, rest, {**model, **{first:False}}, length)





######### main

def main():

    inputLines = sys.stdin.read().splitlines()
    literals, clauses = extract(inputLines)
    length = len(literals)


    doUnit = '--nounit' not in sys.argv
    doPure = '--nopure' not in sys.argv

    ans = DPLL(clauses,literals, {}, length, doUnit, doPure)
    if ans:
        print("satisfiable", end = " ")
        for key in ans.keys():
            print(key+'='+str(ans.get(key))[0],end=' ')
        print()
    else:
        print("unsatisfiable")

main()

