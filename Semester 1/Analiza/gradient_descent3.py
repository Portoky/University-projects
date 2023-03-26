from sympy import *

def f_derivative(y):
    return diff(y)

x = Symbol('x')
y = 8*pow(x, 2)

x_n = 529
learning_rate = pow(10, -2)
print("a)")
print(f"Our function: {y}, learning rate = {learning_rate}, x = {x_n}")
print(f"The sequence after each iteration until we reach the minimum:")
der = f_derivative(y)
iteration = 0
while round(der.subs(x, x_n), 2) != 0:
    x_new = x_n - learning_rate * der.subs(x, x_n)
    print(f"xn = {round(x_n, 3)}")
    x_n = x_new
    iteration += 1
print(f"In total, {iteration} iteration")

print("b)")
learning_rate = 0.1
x_n = 529
iteration = 0
print(f"Now the same function with a learning rate = {learning_rate}")

while round(der.subs(x, x_n), 2) != 0:
    x_new = x_n - learning_rate * der.subs(x, x_n)
    print(f"xn = {round(x_n, 3)}")
    x_n = x_new
    iteration += 1
print(f"In total, only {iteration} iteration")

print("c)")
learning_rate = 2
x_n = 529
iteration = 0
print(f"Now the same function with a learning rate = {learning_rate}")
for i in range(1, 50):
    x_new = x_n - learning_rate * der.subs(x, x_n)
    print(f"xn = {round(x_n, 3)}")
    x_n = x_new
    iteration += 1
print("... and so on.")
print(f"In total {iteration} iteration. As we can see a too large learning rate led to divergence")




