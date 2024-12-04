# Math Visualization and Equation Solvers

This repository contains two Python scripts designed for visualizing mathematical equations and solving various types of problems. These tools are useful for anyone studying or working with math concepts such as graphing, quadratic equations, and systems of equations.

## Table of Contents
- [Scripts Overview](#scripts-overview)
- [Requirements](#requirements)
- [How to Use](#how-to-use)
  - [equation_plotter_with_zoom.py](#equation_plotter_with_zoompypy)
  - [math_system_solver.py](#math_system_solverpy)
- [Examples](#examples)
- [License](#license)

---

## Scripts Overview

### `equation_plotter_with_zoom.py`
This script provides functionality for:
- Plotting one or more equations (e.g., `y = x**2`, `y = np.sin(x)`).
- Shading areas above or below the graph.
- Zooming into specific ranges of the plot.
- Interactively setting graph ranges or zoom factors.

### `math_system_solver.py`
This script includes tools for:
- Plotting a single equation and displaying its value table.
- Solving systems of linear equations.
- Graphing two equations and finding their intersection points.
- Solving and graphing quadratic equations, including marking roots and the vertex.

---

## Requirements

Ensure you have Python installed on your system. The scripts use the following libraries:
- `numpy`
- `matplotlib`
- `sympy`

Install the required libraries using pip:

```bash
pip install numpy matplotlib sympy
```
## How to use

### equation_plotter_with_zoom.py

Run the script:
```bash
python equation_plotter_with_zoom.py
```
Follow the on-screen menu to:
Plot equations with optional shading.
Solve and plot quadratic equations.
Adjust the graph's zoom level interactively.

### math_system_solver.py

Run the script:
```bash
python math_system_solver.py
```
Use the menu options to:
Graph equations and display value tables.
Solve systems of linear equations.
Graph two equations and display their intersection point.
Solve and graph quadratic equations.

## Examples

```python
Example 1: Plotting an Equation
Input:

plaintext
Copiar código
Enter the equation to plot: y = x**2
Result: A graph of 
𝑦
=
𝑥
2
y=x 
2
  from 
𝑥
=
−
10
x=−10 to 
𝑥
=
10
x=10.

Example 2: Solving a System of Equations
Input:

plaintext
Copiar código
Equation 1: y = 2*x + 1
Equation 2: y = -x + 3
Result: The solution 
𝑥
=
0.67
x=0.67, 
𝑦
=
2.33
y=2.33 is printed and marked on the graph.


```

