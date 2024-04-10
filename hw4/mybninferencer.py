# get XML file parser from aabha

#import dependencies
import numpy as np
import pandas as pd
from itertools import product
import xml.dom.minidom
import sys

# takes xml doc
# returns tuple of (varnames, domains)
# varnames is list of varnames
# domains is dict from varname to list of values

## Exact Inference
def vars_and_domains(doc):
    vars = []
    domains = {}
    for v in doc.getElementsByTagName("VARIABLE"):
        varname = v.getElementsByTagName("NAME")[0].childNodes[0].nodeValue
        vars.append(varname)
        outcomes = v.getElementsByTagName("OUTCOME")
        outcomes = [_.childNodes[0].nodeValue for _ in outcomes]
        domains[varname] = outcomes
    return vars, domains


# takes xml doc
# returns tuple of (tables,parents)
# tables is dict from var name to list of floats
# parents is dict from var name to list of var names
#TODO: copied
def tables_and_parents(doc):
    tables = {}
    parents = {}
    for d in doc.getElementsByTagName("DEFINITION"):
        f = d.getElementsByTagName("FOR")[0].childNodes[0].nodeValue
        g = d.getElementsByTagName("GIVEN") 
        g = [_.childNodes[0].nodeValue for _ in g]
        if g:
            parents[f] = g
        else:
            parents[f] = None
        values = []
        for t in d.getElementsByTagName("TABLE"):
            for c in t.childNodes:
                if c.nodeType == xml.dom.minidom.Node.TEXT_NODE:
                    c = c.nodeValue.strip()
                    for v in c.split():
                        if v:
                            values.append(float(v))
        tables[f] = values
    return tables, parents




def parse_table(tables, parents):
    parsed_tables = {}
    for key, vars in parents.items():
        if vars is not None:
            vars_list = list(vars)
            parents_num = len(vars)
            combos = product(['true', 'false'], repeat=parents_num)
            combos_list = list(combos)
            prob_list = list(tables[key])
            df_list = list()
            i = 4*parents_num #num of prob values in output of A
            j = 0
            while j != i:
                df_list.append(prob_list[j])
                j += 2

            df_key=pd.DataFrame(df_list, columns=[key])
            cpt = pd.DataFrame(combos_list, columns=vars_list)
            cpt[key] = df_key
            parsed_tables[key] = cpt

        else:
            combos_list = ['true', 'false']
            cpt = pd.DataFrame(combos_list, columns=[key])
            prob_list = list(tables[key])
            df_key=pd.DataFrame(prob_list)
            cpt['withself'] = df_key
        parsed_tables[key] = cpt
    return parsed_tables

def isEmpty(v):
    return len(v)==0

#TODO generalize for domain
def pos_prob(random_var, value, parsed_tables, given_random_var=None, given_val = None):
    #print(given_random_var)
    if given_random_var is None:
        df=parsed_tables[random_var]
        filter = (df[random_var]==value)
        return float(df[filter]['withself'])
    
    elif given_random_var is not None:
        df = parsed_tables[random_var]
        filter = True
        for p in given_random_var:
            filter = filter & (df[p]==given_val[p])
        if value=='true':
            return float(df[filter][random_var])
        elif value =='false':
            return 1-float(df[filter][random_var])
    else:
        return 0 

def enumerate_all(vars, e, parsed_tables, parents, domains) -> int:
    if isEmpty(vars):
        return 1.0 

    Y = vars[0]
    vars = vars[1:]

    if Y in e.keys():
        par = parents[Y]
        val_of_par = None
        if par is not None:
            val_of_par = {parent: e[parent] for parent in par}
        p = pos_prob(Y,e[Y],parsed_tables, par,val_of_par )
        rec = enumerate_all(vars, e, parsed_tables, parents, domains)
        return p*rec
    else:
        sum = 0
        for y in domains[Y]:
            par = parents[Y]
            val_of_par = None
            if par is not None:
                val_of_par = {parent: e[parent] for parent in par}
            p = pos_prob(Y,y,parsed_tables,par, val_of_par)
            rec = enumerate_all(vars, {**e,Y:y}, parsed_tables, parents, domains)
            sum += (p*rec)
        return sum

#given a distribution, normalize it
def Normalize(dist:list):
    alpha = (1/sum(dist))
    return (alpha*(np.array(dist))).tolist()

def enumerate_ask(X, e, bn, parsed_tables):
    #distribution with X having n values in its domain will have an array of lenth n
    (vars, domains, tables, parents) = bn
    distribution = []
    for i in range(len(domains[X])):
        distribution.append(enumerate_all(vars, {**e, X:domains[X][i]},parsed_tables, parents, domains))
    return Normalize(distribution)


## Approximate Inference - Likelihood Weighting
def weighted_sample(bn,e:dict, parsed_tables):
    (vars, domains, tables, parents) = bn
    w = 1
    event_arr = [0]*len(vars)
    event_dict = {}
    #fix the event
    for i in range(len(vars)):
        
        var = vars[i]
        par = parents[var]
        val_of_par = None
        if par is not None:
            val_of_par = {parent: event_dict[parent] for parent in par}

        if var in e.keys():
            val = e[var]
            #fix
            event_arr[i] = val
            event_dict[var]=val
            w=w*pos_prob(var, val, parsed_tables, par, val_of_par)
        else:
            #sample var 
            domain = domains[var]
            prob_vec = []
            for d in domain:
                prob_vec.append(pos_prob(var, d, parsed_tables, par, val_of_par))

            #print("Prob vec:", prob_vec) #TODO : debug

            sampled_val = np.random.choice(domain, p=prob_vec)
            event_arr[i] = sampled_val
            event_dict[var] = sampled_val
    
    return event_arr, event_dict, w

def likelihood_wt(X, e , bn, parsed_tables, no_of_samples):
    (vars, domains, tables, parents) = bn
    W = [] #array of weights
    W_idx = {} #keeps track of which values of X correspond to which index in W
    for i in range(len(domains[X])):
        W.append(0)
        W_idx[domains[X][i]]=i
    #actual algo
    for j in range(no_of_samples):
        event_arr, event_dict, w = weighted_sample(bn, e, parsed_tables)
        val_in_event = event_dict[X]
        idx = W_idx[val_in_event] #index where this value is found
        W[idx]+=w

    #After all weights are added
    return Normalize(W)



if __name__=='__main__':
    #1000 aima-alarm.xml B J true M true
    doc = xml.dom.minidom.parse(sys.argv[2])
    (vars,domains) = vars_and_domains(doc)
    (tables,parents) = tables_and_parents(doc)
    bn = (vars, domains, tables, parents)

    parsed_tables = parse_table(tables, parents)

    no_of_samples = int(sys.argv[1])
    X = sys.argv[3]
    e = {sys.argv[i]:sys.argv[i+1] for i in range(4,len(sys.argv),2)}
    print("With Exact Inference: ", enumerate_ask(X, e, bn, parsed_tables))
    print("With Approximate Inference: ", likelihood_wt(X,e,bn,parsed_tables,no_of_samples))

    




    




        