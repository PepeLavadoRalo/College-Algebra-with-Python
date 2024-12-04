import math

# 1. Calculate the annuity with monthly or continuous growth
def calculate_annuity(growth, P, r, t, n=12):
    if growth == 'monthly':
        A = P * ((1 + r/n)**(n*t) - 1) / (r/n)
    elif growth == 'continuous':
        A = P * math.exp(r * t)
    else:
        return "Invalid growth type. Choose 'monthly' or 'continuous'."
    return A

# 2. Calculate the monthly mortgage payment
def calculate_mortgage_payment(P, r, n):
    M = P * (r * (1 + r)**n) / ((1 + r)**n - 1)
    return M

# 3. Estimate the investment balance for retirement
def estimate_investment_balance(P, r, t):
    A = P * (1 + r)**t
    return A

# 4. Determine how long it takes to double an amount (Rule of 72)
def time_to_double(r):
    t = 72 / r
    return t

# 5. Solve logarithmic equations (log_b(x) = y)
def solve_logarithm(b, y):
    x = b**y
    return x

# 6. Convert between scientific and standard notation
def to_scientific_notation(value):
    return "{:.6e}".format(value)

def from_scientific_notation(value):
    return float(value)

# Main function to interact with the user
def financial_app():
    print("Financial Calculator")
    print("1. Calculate Annuity")
    print("2. Calculate Mortgage Payment")
    print("3. Estimate Investment Balance for Retirement")
    print("4. Determine Time to Double an Amount")
    print("5. Solve Logarithmic Equations")
    print("6. Convert to and from Scientific Notation")

    choice = int(input("Choose an option (1-6): "))

    if choice == 1:
        attempts = 0
        while attempts < 2:
            growth = input("Is the growth 'monthly' or 'continuous'? ").lower()
            if growth == 'monthly' or growth == 'continuous':
                P = float(input("Enter the periodic payment (P): "))
                r = float(input("Enter the annual interest rate (r): ")) / 100
                t = float(input("Enter the time in years (t): "))
                if growth == 'monthly':
                    n = int(input("Enter the number of payment periods per year (n): "))
                    print("The annuity value is:", calculate_annuity(growth, P, r, t, n))
                else:
                    print("The annuity value is:", calculate_annuity(growth, P, r, t))
                return  # Ends the function after a correct calculation
            else:
                print("You are not entering the correct value. Choose 'monthly' or 'continuous'.")
                attempts += 1

        print("You have exceeded the limit of attempts. Exiting the program.")
        return  # Exits the program if 2 attempts are reached

    elif choice == 2:
        P = float(input("Enter the loan amount (P): "))
        r = float(input("Enter the annual interest rate (r) in %: ")) / 100 / 12
        n = int(input("Enter the number of payments (n) in months: "))
        print("The monthly payment is:", calculate_mortgage_payment(P, r, n))

    elif choice == 3:
        P = float(input("Enter the initial investment amount (P): "))
        r = float(input("Enter the annual interest rate (r) in %: ")) / 100
        t = float(input("Enter the number of years (t): "))
        print("The estimated investment balance is:", estimate_investment_balance(P, r, t))

    elif choice == 4:
        r = float(input("Enter the annual interest rate (r) in %: ")) / 100
        print("The time to double is:", time_to_double(r), "years")

    elif choice == 5:
        b = float(input("Enter the logarithm base (b): "))
        y = float(input("Enter the logarithm value (y): "))
        print("The value of x is:", solve_logarithm(b, y))

    elif choice == 6:
        value = float(input("Enter the value to convert to scientific notation: "))
        print("In scientific notation:", to_scientific_notation(value))
        scientific_value = input("Enter the value in scientific notation to convert to standard: ")
        print("In standard notation:", from_scientific_notation(scientific_value))

    else:
        print("Invalid option")

# Run the application
if __name__ == "__main__":
    financial_app()
