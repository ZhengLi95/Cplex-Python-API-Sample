import cplex

# ============================================================
# Input all the data and parameters here
num_decision_var = 3
num_constraints = 3

A = [
    [1.0, -2.0, 1.0],
    [-4.0, 1.0, 2.0],
    [-2.0, 0, 1.0]
]
b = [11.0, 3.0, 1.0]
c = [-3.0, 1.0, 1.0]

constraint_type = ["L", "G", "E"]
# ============================================================

# Examine if the vectors and matrix meet the requirement
if len(A) != num_constraints:
    print("Please check the Matrix A!")
    exit()

for sub_A in A:
    if len(sub_A) != num_decision_var:
        print("Please check the Matrix A!")
        exit()

if len(b) != num_constraints:
    print("Please check the Vector b!")
    exit()

if len(c) != num_decision_var:
    print("Please check the Vector c!")
    exit()

# Establish the Linear Programming Model
myProblem = cplex.Cplex()

# Add the decision variables and 
myProblem.variables.add(names= ["x"+str(i) for i in range(num_decision_var)])

for i in range(num_constraints):
    myProblem.linear_constraints.add(
        lin_expr= [cplex.SparsePair(ind= ["x"+str(j) for j in range(num_decision_var)], val= A[i])],
        rhs= [b[i]],
        names = ["c"+str(i)],
        senses = [constraint_type[i]]
    )

for i in range(num_decision_var):
    myProblem.objective.set_linear([("x"+str(i), c[i])])

myProblem.objective.set_sense(myProblem.objective.sense.minimize)

myProblem.solve()
print(myProblem.solution.get_values())