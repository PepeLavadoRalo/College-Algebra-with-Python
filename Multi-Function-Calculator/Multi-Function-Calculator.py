import sympy as sp
from fractions import Fraction

# Function to solve equations for x
def solve_equation(equation_str):
    """
    Solves an equation for the variable x.

    Args:
        equation_str (str): The equation as a string (e.g., '2*x + 3 = 5').

    Returns:
        solution: The solution for x if it exists, or "No solution" if none is found.
    """
    x = sp.Symbol('x')
    # Split the equation into left and right sides based on '='
    if '=' in equation_str:
        left_side, right_side = equation_str.split('=')
        equation = sp.Eq(sp.sympify(left_side), sp.sympify(right_side))
    else:
        equation = sp.sympify(equation_str)

    # Solve the equation for x
    solution = sp.solve(equation, x)
    return solution[0] if solution else "No solution"

# Interactive calculator menu
def calculator():
    """
    A multifunctional calculator that offers various mathematical tools:
    1. Solve proportions (a/b = c/x).
    2. Solve equations for x.
    3. Factor square roots.
    4. Convert decimals to fractions and percentages.
    5. Convert fractions to decimals and percentages.
    6. Convert percentages to decimals and fractions.
    0. Exit the calculator.
    """
    while True:
        print("\n--- Multifunctional Calculator ---")
        print("1: Solve proportions (a/b = c/x)")
        print("2: Solve an equation for x")
        print("3: Factorize a square root")
        print("4: Convert decimal to fraction and percentage")
        print("5: Convert fraction to decimal and percentage")
        print("6: Convert percentage to decimal and fraction")
        print("0: Exit")

        choice = input("Select an option: ")

        if choice == '1':
            a = float(input("Enter a: "))
            b = float(input("Enter b: "))
            c = float(input("Enter c: "))
            print("Result x =", solve_proportion(a, b, c))

        elif choice == '2':
            equation_str = input("Enter the equation (e.g., '2*x + 3 - 5 = 0'): ")
            print("Result x =", solve_equation(equation_str))

        elif choice == '3':
            n = int(input("Enter the number to factorize its square root: "))
            print("Result:", factor_square_root(n))

        elif choice == '4':
            decimal = float(input("Enter the decimal number: "))
            fraction, percent = decimal_to_fraction_percent(decimal)
            print("Fraction:", fraction)
            print("Percentage:", percent)

        elif choice == '5':
            numerator = int(input("Enter the numerator: "))
            denominator = int(input("Enter the denominator: "))
            decimal, percent = fraction_to_decimal_percent(numerator, denominator)
            print("Decimal:", decimal)
            print("Percentage:", percent)

        elif choice == '6':
            percent = float(input("Enter the percentage: "))
            decimal, fraction = percent_to_decimal_fraction(percent)
            print("Decimal:", decimal)
            print("Fraction:", fraction)

        elif choice == '0':
            print("Exiting the calculator.")
            break
        else:
            print("Invalid option. Please try again.")

# Run the calculator
calculator()
