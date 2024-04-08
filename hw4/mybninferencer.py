# get XML file parser from aabha

#import dependencies
import numpy as np
import pandas as pd

vars = [] #TODO: get from parser
child_pa = {} ##TODO: get from parser; key: child variables, value: parent variables
e={} #dictionary of evidence variables and their values, args from commmand line
domain = {} #TODO: get from parser
tables = {} #TODO: get from parser


def parse_table(tables, parents)->dict:
    parsed_tables = {}
    for key, vars in parents:
        if  vars is not None:
            negative_values = ['~'+var for var in vars]
            #TODO: by Aabha - add the values in the dataframe
            #TODO: by Aabha - add the finished table into parsed_tables like parsed_tables[B]=cpt 
        else: 
            cpt = pd.DataFrame(columns=[key, "withSelf"], index=key)
            #TODO: by Aabha - add the values in the dataframe
            #TODO: by Aabha - add the finished table into parsed_tables like parsed_tables[B]=cpt 
  

    return parsed_tables

parsed_tables = parse_table(tables, parents)



def isEmpty(v):
    return len(v)==0

def pos_prob(random_var, value, parsed_tables, given_random_var=None, given_val=None):
    
    if given_random_var is None:
        df=parsed_tables[random_var]
        filter = (df[random_var]==value)
        return float(df[filter]['withSelf'])
    
    elif given_random_var is not None and given_val is not None:
        df = parsed_tables[random_var]
        filter = True
        for p in given_random_var:
            filter = filter & (df[p]=='true')
        if value=='true':
            return float(df[filter][random_var])
        elif value =='false':
            return 1-float(df[filter][random_var])
    else:
        return 0 

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

#given a distribution, normalize it
def Normalize(dist:list):
    alpha = (1/sum(dist))
    return alpha*np.array(dist).tolist()

def enumerate_ask(X, e):
    #distribution with X having n values in its domain will have an array of lenth n
    distribution = []
    for i in range(len(domain[X])):
        distribution[i]=enumerate_all(vars, {**e, X:domain[X][i]},parsed_tables)
    return Normalize(distribution)






        