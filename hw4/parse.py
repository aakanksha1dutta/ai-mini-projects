import xml.dom.minidom
import sys

# takes xml doc
# returns tuple of (varnames, domains)
# varnames is list of varnames
# domains is dict from varname to list of values
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

def main():

    file = xml.dom.minidom.parse(sys.argv[1])

    #adjust once inference implemented
    (vars,domains) = vars_and_domains(file)
    print('Variables are:', vars)
    print('Domains are:', domains)
    (tables,parents) = tables_and_parents(file)
    print('Parents are:', parents)
    print('Tables are:', tables)

if __name__ == "__main__":
        main() 


