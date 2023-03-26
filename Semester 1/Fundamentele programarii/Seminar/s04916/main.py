"""

@author: radu


Division

1. Exponential search
2. Compute x to the power n.
3. Binary search.
4. Find the maximum element from a list of integers.
5. Compute the greatest common divisor of the elements of a list of natural numbers.
 
"""


def binary_search(array, left, right, value):
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == value:
            return mid
        elif array[mid] < value:
            return binary_search(array, mid + 1, right, value)
        elif array[mid] > value:
            return binary_search(array, left, mid - 1, value)
    return -1


def exponential_search(array, value):
    i = 1
    n = len(array)
    while i < len(array) and array[i] <= value:
        i = i * 2
    if i >= n:
        i = n - 1
    return binary_search(array, i // 2, i, value)

def expo_search(sorted_list, index, value):
    count = len(sorted_list)
    if index > count:
        return binary_search(sorted_list, index//2, count, value)

    if value < sorted_list[index]:
        return binary_search(sorted_list, index//2, index, value)

    return expo_search(sorted_list, index*2, value)

def x_to_power_n(x, power):
    if power == 0:
        return 1

    result = x_to_power_n(x, power // 2)
    result = result * result

    if power % 2 == 1:
        result = result * x

    return result


def gdc_list(list):
    if len(list) == 1:
        return list[0]

    mid = len(list) // 2
    x = gdc_list(list[:mid])
    y = gdc_list(list[mid:])

    return gdc(x, y)


def gdc(x, y):
    if y == 0:
        return x
    return gdc(y, x % y)


if __name__ == '__main__':
    print(gdc_list([4, 12, 34, 64, 72, 56]))
    #print(expo_search([1,3,4,6,7,11,12,23,53,124,543,566], 1, 0))
