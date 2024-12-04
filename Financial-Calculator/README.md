# Financial Calculator Application

This is a Python-based financial calculator that allows users to perform various financial operations, such as calculating annuities, mortgage payments, retirement investment balances, and more. The app provides an interactive interface where the user can choose from multiple options, input necessary values, and receive the results.

## Features

1. **Calculate Annuity with Monthly or Continuous Growth**  
   The user can choose to calculate an annuity with either monthly or continuous growth. This feature helps users determine the future value of a series of payments or investments over time.

2. **Calculate Mortgage Payment**  
   Users can calculate the monthly mortgage payment based on the loan amount, interest rate, and the number of monthly payments.

3. **Estimate Retirement Investment Balance**  
   This feature estimates the final value of an investment after a given number of years based on an initial deposit and a specified annual interest rate.

4. **Determine Time to Double an Investment (Rule of 72)**  
   The Rule of 72 is used to estimate how many years it will take for an investment to double based on a fixed annual interest rate.

5. **Solve Logarithmic Equations**  
   Users can solve equations of the form `log_b(x) = y` for `x`, using a specified logarithm base and value.

6. **Convert to and from Scientific Notation**  
   This feature allows users to convert numbers to and from scientific notation, which is often useful in financial calculations involving large or small numbers.

## Requirements

- Python 3.x
- `math` module (standard Python library)
- No external libraries are required.

## How to Run the Application

1. **Clone or Download the Repository**  
   You can clone or download the repository to your local machine.

2. **Run the Python Script**
   Open a terminal, navigate to the project folder, and run the script:
  ```bash
  python financial_calculator.py
  ```
3. **Interact with the Application**
   Once the script runs, the program will present a menu of options.
   Choose the number corresponding to the desired financial operation and input the required values as prompted.

   ## Functions
## Functions

- `calculate_annuity(growth, P, r, t, n=12)`
  - **Purpose**: Calculate the annuity with either monthly or continuous growth.
  - **Parameters**:
    - *growth*: The type of growth ('monthly' or 'continuous').
    - *P*: The periodic payment (initial amount).
    - *r*: The annual interest rate (in decimal form, e.g., 5% = 0.05).
    - *t*: The number of years.
    - *n*: The number of payment periods per year (default is 12 for monthly).
  - **Returns**: The calculated annuity value.

- `calculate_mortgage_payment(P, r, n)`
  - **Purpose**: Calculate the monthly mortgage payment.
  - **Parameters**:
    - *P*: The loan amount (principal).
    - *r*: The monthly interest rate (annual rate divided by 12).
    - *n*: The number of payments (in months).
  - **Returns**: The monthly mortgage payment.

- `estimate_retirement_balance(P, r, t)`
  - **Purpose**: Estimate the balance of an investment after a given number of years.
  - **Parameters**:
    - *P*: The initial investment amount.
    - *r*: The annual interest rate (in decimal form).
    - *t*: The number of years.
  - **Returns**: The estimated final balance.

- `time_to_double(r)`
  - **Purpose**: Use the Rule of 72 to estimate the time it will take for an investment to double.
  - **Parameters**:
    - *r*: The annual interest rate (in decimal form).
  - **Returns**: The number of years it will take for the investment to double.

- `solve_logarithm(b, y)`
  - **Purpose**: Solve for x in the logarithmic equation log_b(x) = y.
  - **Parameters**:
    - *b*: The base of the logarithm.
    - *y*: The value of the logarithm.
  - **Returns**: The value of x that satisfies the equation.

- `convert_to_scientific(value)`
  - **Purpose**: Convert a value to scientific notation.
  - **Parameters**:
    - *value*: The number to be converted.
  - **Returns**: The number in scientific notation.

- `convert_from_scientific(value)`
  - **Purpose**: Convert a number from scientific notation to standard format.
  - **Parameters**:
    - *value*: The number in scientific notation as a string.
  - **Returns**: The number in standard form.

```
   
   
  
  
