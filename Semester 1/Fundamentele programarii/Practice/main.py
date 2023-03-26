"""
Create a calculator program for rational numbers with the following functionalities:
    + add a rational number to the calculator
    u undo the last operation
    x exit
"""
from math import gcd

def create_calculator():
    '''Creates the entity of the calculator.
    return: the mentioned calculator represented as a dictionary with two objects: the total, and the history
    total: a list with a pair of nominator and denominatorr
    history: a list containing previous total values
    '''

    return {"Total" : [0, 1], "history" : []}
def create_rational_number(nominator : int, denominator : int = 1):
    divider = gcd(nominator, denominator)
    nominator //= divider
    denominator //= divider