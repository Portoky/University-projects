import numpy as np
import matplotlib.pyplot as plt

# Set the values of p
p = [1.25, 1.5, 3, 8]

# Create a figure and axes
fig, ax = plt.subplots()

# Set the x and y limits of the axes
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)

# Loop through the values of p
for p_val in p:
    # Generate the points on the unit circle
    t = np.linspace(0, 2 * np.pi, 100)
    x = np.cos(t)
    y = np.sin(t)

    # Compute the p-norm of the points
    r = (np.abs(x) ** p_val + np.abs(y) ** p_val) ** (1 / p_val)

    # Plot the points
    ax.plot(r * x, r * y, label=f'p = {p_val}')

# Add a legend
ax.legend()

# Show the plot
plt.show()
