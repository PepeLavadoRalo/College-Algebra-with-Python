import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML

# Projectile parameters
v0 = 50  # Initial velocity in m/s
angle = 45  # Launch angle in degrees
g = 9.81  # Acceleration due to gravity (m/s^2)

# Convert the angle from degrees to radians
theta = np.radians(angle)

# Calculate the total flight time
t_max = 2 * v0 * np.sin(theta) / g

# Create a time array from 0 to t_max
t = np.linspace(0, t_max, num=500)

# Equations of motion for the projectile
x = v0 * np.cos(theta) * t  # Position in the x-direction
y = v0 * np.sin(theta) * t - 0.5 * g * t**2  # Position in the y-direction

# Calculate the landing point
impact_point_x = x[-1]
impact_point_y = 0  # The landing point is at y = 0

# Create a figure and axis for the animation
fig, ax = plt.subplots()
ax.set_xlim(0, max(x))  # Limit the x-axis
ax.set_ylim(0, max(y) + 10)  # Limit the y-axis to allow some space above the highest point

# Create a point for the projectile (initial position)
point, = ax.plot([], [], 'bo', markersize=10)

# Create the impact point (using a red marker)
impact_point, = ax.plot([], [], 'ro', markersize=10, label="Impact point")

# Initialization function for the animation
def init():
    # Set the initial data to empty
    point.set_data([], [])
    impact_point.set_data([], [])
    return point, impact_point

# Update function for the animation (called for each frame)
def update(frame):
    # Update the position of the projectile
    point.set_data(x[frame], y[frame])
    
    # When the animation reaches the last frame, plot the impact point
    if frame == len(t) - 1:
        impact_point.set_data(impact_point_x, impact_point_y)
    
    return point, impact_point

# Create the animation using FuncAnimation
ani = animation.FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=50)

# Display the animation in Google Colab (or Jupyter Notebook)
from IPython.display import display
display(HTML(ani.to_html5_video()))

# Set title and axis labels for the plot
plt.title('Projectile Simulation')
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.grid(True)
