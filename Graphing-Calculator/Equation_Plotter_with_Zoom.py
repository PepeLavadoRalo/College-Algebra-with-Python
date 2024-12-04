import numpy as np
import matplotlib.pyplot as plt

# Function to plot one or more equations
def graficar_ecuacion(ecuaciones, rango=(-10, 10), sombreado=None):
    """
    This function plots one or more equations in the form y = f(x).
    It also allows shading the area above or below the graph.

    Parameters:
    - ecuaciones: List of equations as strings (e.g., ['y = x**2', 'y = 2*x + 1']).
    - rango: Tuple specifying the range of x values (default is -10 to 10).
    - sombreado: Specifies shading ('arriba' for above, 'abajo' for below).
    """
    # Generate x values within the specified range
    x_vals = np.linspace(rango[0], rango[1], 400)

    # Loop through each equation provided
    for ecuacion in ecuaciones:
        ecuacion = ecuacion.replace('y=', '').strip()  # Clean up the equation
        try:
            # Use lambda to create the mathematical function
            f = lambda x: eval(ecuacion)
            y_vals = [f(x) for x in x_vals]  # Evaluate the equation for each x value
            plt.plot(x_vals, y_vals, label=f'y = {ecuacion}')  # Plot the equation

            # Apply shading if specified
            if sombreado == 'arriba':
                plt.fill_between(x_vals, y_vals, color='blue', alpha=0.3)
            elif sombreado == 'abajo':
                plt.fill_between(x_vals, y_vals, color='red', alpha=0.3)

        except Exception as e:
            # Handle errors during equation evaluation
            print(f"Error processing the equation: {e}")

    # Add gridlines, axis lines, and labels to the plot
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(loc='upper right')
    plt.title("Graph of the Equation(s)")
    plt.show()


# Function to zoom into a graph by changing the range
def zoom_graph():
    """
    Allows zooming into the graph by adjusting the range of x values.

    The user can either zoom in by a factor or set a custom range.
    """
    # Ask the user for the equation to graph
    ecuacion = input("Enter the equation to plot (e.g., y = x**2): ").replace('y=', '').strip()

    # Default range for the graph
    rango = (-10, 10)

    # Ask if the user wants to zoom into the current range
    zoom_in = input(f"Do you want to zoom into the current range {rango}? (yes/no): ")

    if zoom_in.lower() == 'yes':
        # Ask the user for the zoom factor
        factor = float(input("How much do you want to reduce the range? (e.g., 0.5 for zoom in): "))
        rango = (rango[0] * factor, rango[1] * factor)  # Adjust the range
        print(f"New range: {rango}")
    else:
        # Allow the user to set a new range
        while True:
            try:
                nuevo_rango_input = input("Enter a new range in the format (min, max) (e.g., -5, 5): ")
                nuevo_rango = tuple(map(float, nuevo_rango_input.split(',')))
                if len(nuevo_rango) == 2:
                    rango = nuevo_rango
                    print(f"New range set: {rango}")
                    break
                else:
                    print("Incorrect format. Make sure to enter two values separated by a comma.")
            except ValueError:
                print("Error: The range format is incorrect. Please use the format (min, max), e.g., (-5, 5).")

    # Plot the equation with the new range
    graficar_ecuacion([f"y = {ecuacion}"], rango=rango)


# Main menu function
def menu():
    """
    Displays a menu to the user with options to:
    - Plot equations
    - Solve and graph systems of equations
    - Plot equations with shading
    - Solve and graph quadratic equations
    - Zoom into a graph
    - Exit the program
    """
    while True:
        print("\nMenu Options:")
        print("1. Plot one or more equations and show value table")
        print("2. Solve a system of equations and graph the intersection point")
        print("3. Plot equations with shading (above or below)")
        print("4. Solve and plot a quadratic equation")
        print("5. Zoom into a graph")
        print("6. Exit")

        # Get the user's choice
        opcion = input("Select an option: ")

        if opcion == '1':
            # Plot one or more equations
            ecuaciones = input("Enter the equations separated by commas (e.g., y = x**2, y = 2*x + 1): ").split(',')
            ecuaciones = [eq.strip() for eq in ecuaciones]
            graficar_ecuacion(ecuaciones)
        elif opcion == '2':
            # Solve and graph a system of equations
            ecuacion1 = input("Enter the first equation (e.g., y = x + 2): ")
            ecuacion2 = input("Enter the second equation (e.g., y = -x + 3): ")
            resolver_sistema_ecuaciones(ecuacion1, ecuacion2)
        elif opcion == '3':
            # Plot equations with shading
            ecuaciones = input("Enter the equations to plot (separated by commas): ").split(',')
            sombreado = input("Do you want to shade the area? (above/below): ")
            graficar_ecuacion([eq.strip() for eq in ecuaciones], sombreado=sombreado)
        elif opcion == '4':
            # Solve and graph a quadratic equation
            a = float(input("Enter the value of a: "))
            b = float(input("Enter the value of b: "))
            c = float(input("Enter the value of c: "))
            resolver_ecuacion_cuadratica(a, b, c)
        elif opcion == '5':
            # Zoom into the graph
            zoom_graph()
        elif opcion == '6':
            # Exit the program
            break
        else:
            print("Invalid option, please try again.")

# Execute the menu
menu()
