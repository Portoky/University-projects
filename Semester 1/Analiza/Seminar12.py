import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

def f(x, y, b):
    return 0.5 * (x**2 + b * y**2)

def grad_f(x, y, b):
    return np.array([x, b * y])

def grad_descent(x_init, y_init, b, num_iterations):
    x_vals = [x_init]
    y_vals = [y_init]
    for i in range(num_iterations):
        grad = grad_f(x_vals[-1], y_vals[-1], b)
        res = minimize_scalar(lambda s: f(x_vals[-1] - s * grad[0], y_vals[-1] - s * grad[1], b))
        step_size = res.x
        x_vals.append(x_vals[-1] - step_size * grad[0])
        y_vals.append(y_vals[-1] - step_size * grad[1])
    return x_vals, y_vals

b_values = [1, 0.5, 0.2, 0.1]
x_init = 10
y_init = 10
num_iterations = 20

x = np.linspace(-20, 20, 100)
y = np.linspace(-20, 20, 100)
X, Y = np.meshgrid(x, y)

for b in b_values:
    Z = f(X, Y, b)
    x_vals, y_vals = grad_descent(x_init, y_init, b, num_iterations)
    plt.figure()
    plt.title("b = {}".format(b))
    plt.contour(X, Y, Z, levels=np.logspace(0, 5, 35))
    plt.scatter(x_vals, y_vals)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
