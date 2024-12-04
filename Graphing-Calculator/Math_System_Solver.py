import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve

# Define functions for each menu option

def graficar_ecuacion(ecuacion):
    """
    Graphs a given equation in the form y = f(x).
    Example input: '5*x + 3', 'x**2 - 4*x + 3', 'np.sin(x)', etc.
    """
    x_vals = np.linspace(-10, 10, 400)  # Generate x values for the graph

    # Remove the 'y=' prefix and process the equation
    ecuacion = ecuacion.replace('y=', '').strip()

    try:
        # Evaluate the equation by replacing "x" with x_vals
        y_vals = [eval(ecuacion) for x in x_vals]

        # Plot the graph
        plt.plot(x_vals, y_vals, label=f'y = {ecuacion}')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(f'Graph of {ecuacion}')
        plt.axhline(0, color='black', linewidth=0.5)  # Add x-axis
        plt.axvline(0, color='black', linewidth=0.5)  # Add y-axis
        plt.grid(True)
        plt.legend()
        plt.show()
    except Exception as e:
        print(f"Error processing the equation: {e}")

def crear_tabla(ecuacion):
    """
    Creates a table of (x, y) values for the given equation.
    """
    x_vals = np.linspace(-10, 10, 21)  # Generate x values for the table
    try:
        # Evaluate the equation by replacing "x" with x_vals
        y_vals = [eval(ecuacion) for x in x_vals]
        print("Table of values (x, y):")
        for x, y in zip(x_vals, y_vals):
            print(f"({x:.2f}, {y:.2f})")
    except Exception as e:
        print(f"Error processing the equation for the table: {e}")

def resolver_sistema_ecuaciones():
    """
    Solves a system of two linear equations and displays the solution.
    """
    x, y = symbols('x y')  # Define symbolic variables
    ecuacion1 = Eq(x + 2*y, 3)  # First equation
    ecuacion2 = Eq(2*x - y, 4)  # Second equation

    # Solve the system of equations
    solucion = solve((ecuacion1, ecuacion2), (x, y))
    print("Solution of the system of equations:")
    print(f"x = {solucion[x]}, y = {solucion[y]}")

def graficar_sistema_ecuaciones():
    """
    Graphs two equations provided by the user and shows their intersection point.
    """
    # Ask the user for the two equations
    print("Enter two equations in the format 'y = f(x)'. Example: y = 2*x + 1")
    ecuacion1 = input("Enter the first equation (e.g., y = 2*x + 1): ").replace('y=', '').strip()
    ecuacion2 = input("Enter the second equation (e.g., y = -x + 3): ").replace('y=', '').strip()

    # Generate x values for the graphs
    x_vals = np.linspace(-10, 10, 400)

    try:
        # Evaluate both equations
        y1_vals = [eval(ecuacion1) for x in x_vals]  # First equation
        y2_vals = [eval(ecuacion2) for x in x_vals]  # Second equation

        # Plot both equations
        plt.plot(x_vals, y1_vals, label=f'y = {ecuacion1}')
        plt.plot(x_vals, y2_vals, label=f'y = {ecuacion2}')

        # Find and display the intersection point
        x, y = symbols('x y')  # Define symbolic variables
        eq1 = Eq(eval(ecuacion1), y)  # First equation
        eq2 = Eq(eval(ecuacion2), y)  # Second equation
        interseccion = solve((eq1, eq2), (x, y))  # Solve for intersection

        if interseccion:
            print(f"The equations intersect at: ({interseccion[x]}, {interseccion[y]})")
            plt.scatter(interseccion[x], interseccion[y], color='red', 
                        label=f'Intersection point ({interseccion[x]:.2f}, {interseccion[y]:.2f})')

    except Exception as e:
        print("Error processing the equations:", e)
        return

    # Configure the plot
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Graph of the two equations')
    plt.legend()
    plt.show()

def resolver_ecuacion_cuadratica(a, b, c):
    """
    Solves a quadratic equation of the form ax^2 + bx + c = 0 and graphs it.
    """
    discriminante = b**2 - 4*a*c  # Calculate the discriminant
    if discriminante >= 0:
        # Calculate real roots
        raiz1 = (-b + np.sqrt(discriminante)) / (2*a)
        raiz2 = (-b - np.sqrt(discriminante)) / (2*a)
        print(f"Roots: x1 = {raiz1}, x2 = {raiz2}")
    else:
        print("No real solutions.")

    # Plot the quadratic equation
    x_vals = np.linspace(-10, 10, 400)
    y_vals = a*x_vals**2 + b*x_vals + c
    plt.plot(x_vals, y_vals, label=f'{a}x^2 + {b}x + {c}')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True)

    # Mark the roots and vertex if they exist
    if discriminante >= 0:
        plt.scatter([raiz1, raiz2], [0, 0], color='red', zorder=5)
    vertex_x = -b / (2*a)
    vertex_y = a*vertex_x**2 + b*vertex_x + c
    plt.scatter(vertex_x, vertex_y, color='green', zorder=5, label=f'Vertex: ({vertex_x:.2f}, {vertex_y:.2f})')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Graph of the quadratic equation')
    plt.legend()
    plt.show()

# Menu of options
def menu():
    while True:
        print("\nMenu of options:")
        print("1. Graph an equation and display a table of values")
        print("2. Solve a system of equations without graphing")
        print("3. Graph two equations and show their intersection point")
        print("4. Solve and graph a quadratic equation")
        print("5. Exit")

        opcion = input("Choose an option (1-5): ")

        if opcion == '1':
            ecuacion = input("Enter an equation in the form y = f(x): ")
            graficar_ecuacion(ecuacion)
            crear_tabla(ecuacion)
        elif opcion == '2':
            resolver_sistema_ecuaciones()
        elif opcion == '3':
            graficar_sistema_ecuaciones()
        elif opcion == '4':
            a = float(input("Enter the value of a: "))
            b = float(input("Enter the value of b: "))
            c = float(input("Enter the value of c: "))
            resolver_ecuacion_cuadratica(a, b, c)
        elif opcion == '5':
            print("Exiting...")
            break
        else:
            print("Invalid option, please choose an option between 1 and 5.")

# Run the menu
menu()
