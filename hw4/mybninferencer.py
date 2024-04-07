# get XML file parser from aabha


'''
function Enumerate-All(vars,e) returns a real number 
if Empty?(vars) then return 1.0
Y ← First(vars)
if Y has value y in e
then return P (y | P a(Y )) × Enumerate-All(Rest(vars), e) else return !y P (y | P a(Y )) × Enumerate-All(Rest(vars), ey )
where ey is e extended with Y = y
'''


child_pa = {} #key: child variables, value: parent variables
e={} #dictionary of evidence variables and their values
        
def isEmpty(v):
    return len(v)==0

def pos_prob(query, given):
    #TODO
    return 0

def marginalize(over, vars, e):
    #P (y | P a(Y )) × Enumerate-All(Rest(vars), e) else return !y P (y | P a(Y )) × Enumerate-All(Rest(vars), ey )
    return 0

def enumerate_all(vars, e) -> int:
    if isEmpty(vars):
        return 1   
    Y = vars.pop()
    if Y in e.keys():
        return pos_prob(e[Y], child_pa[Y])*enumerate_all(vars,e)
    else:
        marginalize(Y, vars, e)

"""function Enumeration-Ask(X,e,bn) returns a distribution over X inputs: X, the query variable
e, observed values for variables E
bn, a Bayesian network with variables {X} ∪ E ∪ Y
Q(X ) ← a distribution over X, initially empty for each value xi of X do
extend e with value xi for X
Q(xi ) ← Enumerate-All(Vars[bn], e) return Normalize(Q(X ))"""



        