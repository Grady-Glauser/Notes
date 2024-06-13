import sympy as sym

# Define the equation as a string variable
equation_str = "2*x + 5 = 15"

# Parse the equation string and create a symbolic expression object
equation_obj = sym.parse_expr(equation_str)

# Solve the equation for the variable of interest
solutions = sym.solve(equation_obj, 'x')

# Display the solution(s) to the user
print("The solution(s) for x are:")
for solution in solutions:
    print(solution)