"""

@author: radu

1.
a) Compute the sum of the first n natural numbers.
b) Check if a given integer  number n is prime.
c) Compute the greatest common divisor between two integers a and b.
d) Compute the first prime number greater than a given integer n.
e) Print the first k prime numbers greater than a given integer n.

2. Compute the age of a person in number of days. So, given the date of birth
of a person in the format dd mm yyyy (three integers) and the current date
(in the same format) compute the age of that person in number of days.

"""
from math import sqrt


def sum_of_first_natural_numbers(n):
    """Computes the sum of the first n natural numbers.

    Given a natural number n, we will calculate the sum of the first n natural numbers
    :param n: natural number
    :return: the sum of the first [n] natural numbers
    """
    sum = 0
    for i in range(n):
        sum = sum + i
    return sum


def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a if a > 0 else -a


def check_primality(n):
    if n == 2:
        return True

    if n % 2 == 0 or n < 2:
        return False

    for i in range(3, int(sqrt(n) + 1), 2):
        if n % i == 0:
            return False

    return True


def prime_greater_than(n):
    while True:
        n = n + 1
        if check_primality(n):
            return n

def first_greater_prime_numbers(n,k):
    for i in range(k):
        n=prime_greater_than(n)
        print(n)



if __name__ == '__main__':
    # print(sum_of_first_natural_numbers(4))
    # print(gcd(-3, -6))
    print(check_primality())
