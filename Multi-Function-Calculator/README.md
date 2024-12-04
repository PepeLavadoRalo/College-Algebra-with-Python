# Multifunctional Calculator

This project is an interactive **Multifunctional Calculator** implemented in Python. It provides a range of mathematical tools, including solving equations, working with proportions, and converting between decimals, fractions, and percentages. The calculator is designed to be both user-friendly and flexible.

---

## Features

1. **Solve Proportions**  
   Calculates the unknown variable \( x \) in a proportion of the form \( \frac{a}{b} = \frac{c}{x} \).

2. **Solve Equations**  
   Solves linear or simple equations for the variable \( x \).  
   Example: `2*x + 3 = 5` → Solution: `x = 1`.

3. **Factorize Square Roots**  
   Decomposes square roots into their factors for easier computation.  
   Example: \( \sqrt{50} = 5\sqrt{2} \).

4. **Convert Decimal to Fraction and Percentage**  
   Converts a decimal number into its fraction and percentage equivalents.  
   Example: `0.75` → Fraction: \( \frac{3}{4} \), Percentage: `75%`.

5. **Convert Fraction to Decimal and Percentage**  
   Converts a fraction into its decimal and percentage equivalents.  
   Example: \( \frac{1}{2} \) → Decimal: `0.5`, Percentage: `50%`.

6. **Convert Percentage to Decimal and Fraction**  
   Converts a percentage into its decimal and fraction equivalents.  
   Example: `25%` → Decimal: `0.25`, Fraction: \( \frac{1}{4} \).

---

## Usage

1. Run the program in a Python interpreter.
2. Select an option from the menu by entering its corresponding number.
3. Follow the prompts to input the required data.
4. View the result of the calculation.

---

## Code Example

```python
# Example of solving an equation for x:
equation_str = '2*x + 3 = 5'
result = solve_equation(equation_str)
print("Result x =", result)
# Output: Result x = 1
```

## Installation and Requirements
Python Version: The program requires Python 3.x.
Libraries: The following libraries are used:
sympy: For symbolic mathematics (solving equations and factorization).
fractions: For fraction manipulation and conversion.

## Example Interaction
```python
--- Multifunctional Calculator ---
1: Solve proportions (a/b = c/x)
2: Solve an equation for x
3: Factorize a square root
4: Convert decimal to fraction and percentage
5: Convert fraction to decimal and percentage
6: Convert percentage to decimal and fraction
0: Exit

Select an option: 2
Enter the equation (e.g., '2*x + 3 - 5 = 0'): 3*x - 9 = 6
Result x = 5
```
