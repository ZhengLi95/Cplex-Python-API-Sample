import cplex

# ============================================================
# This file gives us a sample to use Cplex Python API to
# establish a Mixed Integer Linear Programming model and then solve it.
# The  problem displayed bellow is as:
#                  min z = cx
#    subject to:      Ax = b
#    and some of x is integer or binary
# ============================================================

# ============================================================
# Input all the data and parameters here
num_decision_var = 2
num_constraints = 2

A = [
    [1, 9/14],
    [-2, 1]
]
b = [51/14, 1/3]
c = [1, 1]

constraint_type = ["L", "L"] # Less, Greater, Equal
# ============================================================

# Establish the Linear Programming Model
myProblem = cplex.Cplex()

# Add the decision variables and set their lower bound and upper bound (if necessary)
myProblem.variables.add(names= ["x"+str(i) for i in range(num_decision_var)])
for i in range(num_decision_var):
    myProblem.variables.set_lower_bounds(i, 0.0)

# Set the type of each variables
myProblem.variables.set_types(0, myProblem.variables.type.integer)
myProblem.variables.set_types(1, myProblem.variables.type.continuous)

# Add constraints
for i in range(num_constraints):
    myProblem.linear_constraints.add(
        lin_expr= [cplex.SparsePair(ind= [j for j in range(num_decision_var)], val= A[i])],
        rhs= [b[i]],
        names = ["c"+str(i)],
        senses = [constraint_type[i]]
    )

# Add objective function and set its sense
for i in range(num_decision_var):
    myProblem.objective.set_linear([(i, c[i])])
myProblem.objective.set_sense(myProblem.objective.sense.maximize)

# Solve the model and print the answer
myProblem.solve()
print(myProblem.solution.get_values())