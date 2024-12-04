# Math and Physics Game Collection

Welcome to the **Math and Physics Game Collection**, a set of interactive games designed to challenge your problem-solving skills with a mix of algebra and projectile motion simulations. These games are suitable for players looking to improve their mathematical abilities and have fun while doing it. 

## Table of Contents

1. [Project Overview](#project-overview)
2. [Game 1: Algebra Practice](#game-1-algebra-practice)
3. [Game 2: Projectile Path](#game-2-projectile-path)
4. [How to Run the Games](#how-to-run-the-games)
5. [License](#license)

---

## Project Overview

This repository includes three games that focus on different aspects of mathematics and physics:

- **Algebra Practice**: Solve algebraic problems, improve your skills with single-step and multi-step equations.
- **Projectile Path**: Simulate the trajectory of a projectile and track its flight path.
- **Scatter Plot Guessing Game**: Guess the coordinates of a randomly placed point on a scatter plot.

Each game has been designed to offer an engaging and educational experience. Whether you're trying to solve algebraic equations or track a flying projectile, these games will test your skills in different ways.

---

## Game 1: Algebra Practice

### Objective:
The goal of this game is to solve algebraic problems based on your chosen difficulty level (easy, medium, or hard). Players will be presented with single-step or multi-step problems, and they need to input the correct answer to progress.

### Gameplay:
1. Choose a difficulty level: **Easy**, **Medium**, or **Hard**.
2. Solve a series of 5 problems (you need to answer more than half correctly to pass).
3. Each problem can involve basic arithmetic operations like addition, subtraction, multiplication, or division.
4. After each answer, the game will tell you whether you were correct or not and provide the correct answer if necessary.

### Example Problem:
- For difficulty **medium**, you may get a problem like:  
  `(5 + 2) * 3 - 4`

---

## Game 2: Projectile Path

### Objective:
The goal of this game is to simulate the motion of a projectile launched at a specific angle and initial velocity. The player will observe the path of the projectile and see where it lands.

### Gameplay:
1. Set the initial speed (velocity) and launch angle.
2. Watch the projectile launch and follow its path through the air.
3. The game uses a physics-based simulation, and you will be able to view the trajectory over time.
4. The game shows the point where the projectile lands.

### Features:
- Animation of the projectile motion.
- Physics-based calculations (speed, angle, gravity).
- Visual display of the projectile's path and the impact point.

---

## Game 3: Scatter Plot Guessing Game

### Objective:
In this game, you are tasked with guessing the coordinates of a randomly placed point on a scatter plot. The game provides you with hints to help you narrow down the correct position of the point.

### Gameplay:
1. A random point is generated on a scatter plot within a defined range.
2. You have 5 attempts to guess the exact coordinates of the point.
3. For each guess, you will receive feedback on how close you are to the correct answer, including whether you are close on the x or y-axis.
4. If you guess correctly, you win; if not, the game will reveal the correct coordinates after 5 attempts.

### Features:
- Different levels of difficulty (easy, medium, hard).
- Interactive feedback system.
- Graphical representation of the scatter plot.
- Limited attempts to guess the correct coordinates.

---

## How to Run the Games

These games are implemented in Python. To run them, you will need:

1. **Python 3.x** installed on your computer.
2. Necessary Python libraries such as:
   - `matplotlib`
   - `numpy`
   - `IPython` (for displaying animations)

### Installation:

To install the required libraries, you can run:

```bash
pip install matplotlib numpy IPython
```

### Running the Games:
Running the Games:
Download or clone this repository to your local machine.
Navigate to the folder containing the Python files for the game you want to play.
Open a terminal or command prompt, and run the corresponding Python script.
For example, to run the Algebra Practice game:
```bash
python algebra_game.py
```
To run the Projectile Path game:
```bash
python projectile_game.py
```
To run the Scatter Plot Guessing Game:
```bash
python scatter_plot_game.py
```

