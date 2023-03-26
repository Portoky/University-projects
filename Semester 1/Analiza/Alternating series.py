import math
import random

def normal_series(n):
    numerator = 1
    series = 0
    for denominator in range(1, n):
        series += numerator / denominator
        numerator *= -1

    print(f"Series = {series}")
    ln2 = math.log(2)
    print(f"ln2 = {ln2}")

def series_with_rearranged_elements(n):
    numerator = 1
    l = []
    for denominator in range(1, n):
         l.append(numerator / denominator)
         numerator *= -1
    pos = []
    neg = []
    for element in l:
        if element > 0:
            pos.append(element)
        else:
            neg.append(element)
    i = 0
    j = 0
    series = 0
    while i < len(pos) and j < len(neg)-1:
        series = pos[i] + neg[j] + neg[j+1]
        i += 1
        j += 2
    
    print(f"Series with rearranged elements: {series}")
    ln2 = math.log(2)
    print(f"ln2 = {ln2}")

if __name__ == '__main__':
    n = int(input("Number of elements you would like in the series:"))
    series_with_rearranged_elements(n)
    normal_series(n)
