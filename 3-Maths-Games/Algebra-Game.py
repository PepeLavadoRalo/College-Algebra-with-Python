import random

# Function to generate a math problem based on difficulty
def generate_problem(difficulty):
    # Determine the range of numbers based on the difficulty level
    if difficulty == "easy":
        number_range = (-5, 5)
    elif difficulty == "medium":
        number_range = (-10, 10)
    else:  # hard
        number_range = (-20, 20)

    # Randomly choose between a one-step or two-step problem
    problem_type = random.choice(["one", "two"])

    if problem_type == "one":
        # One-step problem (addition or subtraction)
        num1 = random.randint(number_range[0], number_range[1])
        num2 = random.randint(number_range[0], number_range[1])
        operation = random.choice(["+", "-"])
        if operation == "+":
            correct_answer = num1 + num2
        else:
            correct_answer = num1 - num2
        problem = f"{num1} {operation} {num2}"

    elif problem_type == "two":
        # Two-step problem (combination of operations)
        num1 = random.randint(number_range[0], number_range[1])
        num2 = random.randint(number_range[0], number_range[1])
        num3 = random.randint(number_range[0], number_range[1])
        operation1 = random.choice(["+", "-", "*", "/"])
        operation2 = random.choice(["+", "-", "*", "/"])

        # First operation
        if operation1 == "+":
            intermediate_result = num1 + num2
        elif operation1 == "-":
            intermediate_result = num1 - num2
        elif operation1 == "*":
            intermediate_result = num1 * num2
        else:
            intermediate_result = num1 / num2 if num2 != 0 else num1  # Avoid division by zero

        # Second operation
        if operation2 == "+":
            correct_answer = intermediate_result + num3
        elif operation2 == "-":
            correct_answer = intermediate_result - num3
        elif operation2 == "*":
            correct_answer = intermediate_result * num3
        else:
            correct_answer = intermediate_result / num3 if num3 != 0 else intermediate_result

        problem = f"({num1} {operation1} {num2}) {operation2} {num3}"

    return problem, correct_answer

# Main game function
def play_game():
    print("Welcome to the Algebra Challenge!")
    print("You need to solve 5 questions to pass.")
    print("To pass, you must answer more than half of the questions correctly.")

    # Choose difficulty level
    difficulty = ""
    while difficulty not in ["easy", "medium", "hard"]:
        difficulty = input("Choose your difficulty level (easy, medium, hard): ").lower()

    number_of_questions = 5  # Total number of questions
    score = 0

    # Loop through each question
    for _ in range(number_of_questions):
        problem, correct_answer = generate_problem(difficulty)
        print("\nSolve the following problem:")
        print(problem)
        try:
            user_answer = float(input("Your answer: "))
            if user_answer == correct_answer:
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect. The correct answer was {correct_answer}.")
        except ValueError:
            print("Please enter a valid number.")

    # Determine if the player passes
    if score > number_of_questions / 2:
        print(f"\nCongratulations! You passed with a score of {score}/{number_of_questions}.")
    else:
        print(f"\nSorry, you didn't pass. Your score was {score}/{number_of_questions}.")

# Start the game
play_game()
