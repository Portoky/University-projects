import math


def f(x):
    return 4*pow(x, 2) #f = 4*x^2

def f_derivative(x):
    h = 0000.1
    return (f(x + h) - f(x)) / h #~f'(x)

if __name__ == '__main__':
    x = 17.5
    i = 1
    learning_rate = 000000000000000000.1
    while f_derivative(x) != 0: #if der is 0, than we reached a global minimum
        new_x = x - learning_rate * f_derivative(x)
        x = round(new_x, 3)
        print(x)


