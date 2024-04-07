Name: Aabha Pandit (apandit@u)
CSC242 - Project 3

The goal of this project is to solve implement the DPLL algorithm for solving the Boolean satisfiability prblems.
The SAT problem is either satisfied by some truth assignment to its variables or it is unsatisfiable.
In Project 1, the brute force appraoch was used to tackle boolean satisfiability, however, in this project, with
the implementation of DPLL, we use the Unit Clause & Pure Literal heuristics to simplify the problem.

Benefit of heuristics:

Unit Clause Heuristic: It identifies and assigns truth values to unit clauses, simplyfying the formula by 
reducing the search space. The unit_heuristic method implements this heuristic.

Pure Literal Heuristic: Pure literals are those that only appear with one polarity (either positive or negative)
in the formula. Assigning truth values to pure literals simplifies the formula because the all clauses containing
these literals are either always true or always false. This, again, reduces the search space. 
The pure_heuristic method implements this heuristic.

Organization:
The code is organized into several methods: extract for parsing input CNF formulas, isSat for checking satisfiability, 
find_pure for implementing the pure literal heuristic, unit_heuristic for the unit propagation heuristic, and DPLL 
for the main recursive algorithm. 
Additionally, there are helper methods that check clause truth values and give assignments (to either all variables
or literals that are still left to be assigned after the heuristics). The script reads input from standard input, 
extracts literals and clauses, and then implements the DPLL algorithm with optional heuristic arguments.
Then it prints whether the formula is satisfiable or unsatisfiable, along with a satisfying assignment (given it exists).
