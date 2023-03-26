import math

def f(x, exponent):
    return pow(x, exponent)


def f_derived(x, exponent):
    x *= exponent
    exponent -= 1
    return x, exponent



def iteration(x, n, exponent):
    x, exponent = f_derived(x, exponent)
    return x - n * f(x, exponent)


if __name__ == '__main__':
    x = int(input("f(x) = x^8. Input the first element of the gradient descent: "))
    learning_rate = 0.001
    exponent = 2
    i = 1
    for i in range(1, 10000):
        x_der, exponent = f_derived(x, exponent)
        x_n = x - learning_rate * f(x_der, exponent)
        print(f"x_n = {x_n}")
        if x_n <= 0:
            break



