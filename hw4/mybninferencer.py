# get XML file parser from aabha

#import dependencies
import numpy as np
import pandas as pd

'''Parents are: {'B': None, 'E': None, 'A': ['B', 'E'], 'J': ['A'], 'M': ['A']}
Tables are: {'B': [0.001, 0.999], 'E': [0.002, 0.998], 
'A': [0.95, 0.05, 0.94, 0.06, 0.29, 0.71, 0.001, 0.999], 'J': [0.9, 0.1, 0.05, 0.95], 'M': [0.7, 0.3, 0.01, 0.99]}'''

def parse_table(tables, parents)->dict:
    parsed_tables = {}
    for key, vars in parents:
        if  vars is not None:
            negative_values = ['~'+var for var in vars]
            cpt = pd.DataFrame(columns=[key, *vars,*negative_values ], index=key)
            #TODO: by Aabha - add the values in the dataframe
            #TODO: by Aabha - add the finished table into parsed_tables like parsed_tables[B]=cpt 
        else: 
            cpt = pd.DataFrame(columns=[key, "withSelf"], index=key)
            #TODO: by Aabha - add the values in the dataframe
            #TODO: by Aabha - add the finished table into parsed_tables like parsed_tables[B]=cpt 
  


    return parsed_tables
def isEmpty(v):
    return len(v)==0

def pos_prob(random_var, value, parsed_tables, given_random_var=None, given_val=None):
    if given_random_var is None:
        return parsed_tables[random_var].loc[value, "withSelf"]
    elif given_random_var is not None and given_val is not None:
        return parsed_tables[random_var].loc[value, given_val]
    else:
        return 0 

'''
function Enumerate-All(vars,e) returns a real number 
if Empty?(vars) then return 1.0
Y ← First(vars)
if Y has value y in e
then return P (y | P a(Y )) × Enumerate-All(Rest(vars), e) else return !y P (y | P a(Y )) × Enumerate-All(Rest(vars), ey )
where ey is e extended with Y = y
'''      

def enumerate_all(vars, e, parsed_tables) -> int:
    if isEmpty(vars):
        return 1   
    Y = vars.pop()
    if Y in e.keys():
        return (pos_prob(Y,e[Y],parsed_tables, child_pa[Y], child_pa[Y])*enumerate_all(vars, e, parsed_tables))
    else:
        sum = 0
        for y in domain[Y]:
            sum += (pos_prob(Y,y,parsed_tables,child_pa[Y], child_pa[Y])*enumerate_all(vars, {**e,Y:y}, parsed_tables))
        return sum

"""function Enumeration-Ask(X,e,bn) returns a distribution over X inputs: X, the query variable
e, observed values for variables E
bn, a Bayesian network with variables {X} ∪ E ∪ Y
Q(X ) ← a distribution over X, initially empty for each value xi of X do
extend e with value xi for X
Q(xi ) ← Enumerate-All(Vars[bn], e) return Normalize(Q(X ))"""

#main function
if __name__=="main":
    vars = [] #TODO: get from parser
    child_pa = {} ##TODO: get from parser; key: child variables, value: parent variables
    e={} #dictionary of evidence variables and their values, args from commmand line
    domain = {} #TODO: get from parser
    tables = {} #TODO: get from parser
    parsed_tables = parse_table(tables, parents)




        