# This is a sample Python script.
import pickle
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from math import sqrt

def is_prime(n : int):
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(sqrt(n))):
        if n % i == 0:
            return False
    return True

def _test_is_prime():
    assert is_prime(2) == True, "It should be True"
    assert is_prime(3) == True, "Should be True"
    assert is_prime(4) == False, "Should be False"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
