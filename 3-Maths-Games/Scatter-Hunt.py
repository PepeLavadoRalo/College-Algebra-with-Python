import random
import matplotlib.pyplot as plt

# Function to define grid limits based on difficulty level
def define_limits(difficulty):
    if difficulty == 'easy':
        return 3, 3  # Limits for a 3x3 grid and graph size 3.5x3.5
    elif difficulty == 'medium':
        return 5, 5  # Limits for a 5x5 grid and graph size 5.5x5.5
    elif difficulty == 'hard':
        return 7, 7  # Limits for a 7x7 grid and graph size 7.5x7.5
    else:
        print("Invalid difficulty, defaulting to 'easy'.")
        return 3, 3

# Display the final grid with the guessed point
def show_final_grid(limit_x, limit_y, point_x, point_y, graph_size_x, graph_size_y):
    plt.figure(figsize=(graph_size_x, graph_size_y))  # Adjust the graph size
    plt.grid(True)
    plt.xlim(-limit_x, limit_x)
    plt.ylim(-limit_y, limit_y)
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.title("Scatter Plot - Point Found")
    plt.scatter(point_x, point_y, color="green", s=100, label="Point Found")  # Highlight the found point
    plt.legend(fontsize=8)  # Adjust legend size
    plt.show()

# Display the initial grid with the generated point
def show_initial_graph(limit_x, limit_y, point_x, point_y, graph_size_x, graph_size_y):
    plt.figure(figsize=(graph_size_x, graph_size_y))  # Adjust the graph size
    plt.grid(True)
    plt.xlim(-limit_x, limit_x)
    plt.ylim(-limit_y, limit_y)
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.title("Reference Graph - Target Point")
    plt.scatter(point_x, point_y, color="red", s=100, label="Target Point (hidden)")  # Target point in red
    plt.legend(fontsize=8)  # Adjust legend size
    plt.show()

# Main game logic
def scatter_hunt_game():
    print("Welcome to the Scatter Hunt Game.")

    # Select difficulty level
    difficulty = input("Choose difficulty (easy, medium, hard): ").strip().lower()
    limit_x, graph_size_x = define_limits(difficulty)
    limit_y, graph_size_y = define_limits(difficulty)

    # Increase graph limits slightly for better visibility
    graph_size_x += 0.5
    graph_size_y += 0.5

    # Generate a random point within the defined integer limits
    point_x = random.randint(-int(limit_x), int(limit_x))
    point_y = random.randint(-int(limit_y), int(limit_y))

    # Show the initial graph with the hidden target point
    show_initial_graph(limit_x, limit_y, point_x, point_y, graph_size_x, graph_size_y)

    # Prompt the player to guess the point
    print("Now try to guess the point!")

    # Number of attempts and hint tracking
    attempts = 5
    x_correct = False
    y_correct = False

    for attempt in range(attempts):
        try:
            # Ask the player for coordinates
            guess_x = int(input("Enter X-coordinate: "))
            guess_y = int(input("Enter Y-coordinate: "))

            # Check if the player guessed correctly
            if guess_x == point_x and guess_y == point_y:
                print("Correct! You found the point.")
                show_final_grid(limit_x, limit_y, point_x, point_y, graph_size_x, graph_size_y)  # Display success
                return  # End the game on a correct guess

            # Check individual coordinates and provide feedback
            if guess_x == point_x:
                x_correct = True
                print("Correct! The X-coordinate is correct.")
            else:
                x_correct = False

            if guess_y == point_y:
                y_correct = True
                print("Correct! The Y-coordinate is correct.")
            else:
                y_correct = False

            # Provide detailed hints for incorrect guesses
            if not x_correct:
                print("Incorrect X-coordinate.")
                distance_x = abs(guess_x - point_x)
                if distance_x == 1:
                    print("For X-coordinate: Very close.")
                elif distance_x <= limit_x // 2:
                    print("For X-coordinate: Close.")
                else:
                    print("For X-coordinate: Far.")

            if not y_correct:
                print("Incorrect Y-coordinate.")
                distance_y = abs(guess_y - point_y)
                if distance_y == 1:
                    print("For Y-coordinate: Very close.")
                elif distance_y <= limit_y // 2:
                    print("For Y-coordinate: Close.")
                else:
                    print("For Y-coordinate: Far.")

            # Suggest adjustments if needed
            if guess_x < point_x and not x_correct:
                print("The X value is higher.")
            elif guess_x > point_x and not x_correct:
                print("The X value is lower.")

            if guess_y < point_y and not y_correct:
                print("The Y value is higher.")
            elif guess_y > point_y and not y_correct:
                print("The Y value is lower.")

        # Handle invalid inputs
        except ValueError:
            print("Please enter valid numbers for the coordinates.")

   
