import matplotlib.pyplot as plt
import numpy as np

# Define the functions
def f1(x, y):
    return (1/2) * x**2 + (1/2) * y**2

def f2(x, y):
    return 2 * x**2 + y**2

def f3(x, y):
    return (-1/2) * x**2 + (-1/2) * y**2

def f4(x, y):
    return -2 * x**2 - y**2

def f5(x, y):
    return (1/2) * x**2 + (-1/2) * y**2

def f6(x, y):
    return 2 * x**2 + -y**2

# Set up the plot
fig, axs = plt.subplots(2, 3, figsize=(9, 6))

# Create a grid of points
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)

# Plot the contour lines and the gradient at three different points for each function
for ax, func in zip(axs.flatten(), [f1, f2, f3, f4, f5, f6]):
    # Calculate the gradient
    grad = np.gradient(func(X, Y))
    # Plot the contour lines
    ax.contour(X, Y, func(X, Y), levels=[-2, 0, 2])
    # Plot the gradient at three different points
    ax.quiver(1, 1, grad[0][50][50], grad[1][50][50], scale=10, color='red')
    ax.quiver(-1, -1, grad[0][0][0], grad[1][0][0], scale=10, color='green')
    ax.quiver(0, 0, grad[0][50][0], grad[1][50][0], scale=10, color='blue')

# Show the plot
plt.show()
