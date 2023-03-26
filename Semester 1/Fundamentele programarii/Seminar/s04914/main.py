"""

@author: radu


Division

1. Exponential search
2. Compute x to the power n.
3. Binary search.
4. Find the maximum element from a list of integers.
5. Compute the greatest common divisor of the elements of a list of natural numbers.
 
"""


def x_power_n(x, n):
    if n == 0:
        return 1
    x_power = x_power_n(x, n // 2)
    if n % 2 == 0:
        return x_power * x_power
    return x * x_power * x_power


def binary_search(a, l, r, v):
    while l <= r:
        mid = (l + r) // 2
        if a[mid] == v:
            return mid
        if a[mid] < v:
            l = mid + 1
        else:
            r = mid - 1
    return -1


def exponential_search(a, v):
    i = 1
    while i <= len(a) and a[i - 1] <= v:
        i = i * 2
    if i > len(a):
        i = len(a)

    return binary_search(a, i // 2 - 1, i - 1, v)


def max_element(arr):
    if len(arr) == 1:
        return arr[0]
    mid = len(arr) // 2
    return max(max_element(arr[:mid]), max_element(arr[mid:]))


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def gcd_of_list(l):
    n = len(l)

    if n == 1:
        return l[0]

    a = gcd_of_list(l[n // 2:])
    b = gcd_of_list(l[:n // 2])
    return gcd(a, b)


if __name__ == '__main__':
    '''a = [1, 3, 5, 6, 7, 9]
    v = -17
    res = exponential_search(a, v)
    if res == -1:
        print(f"The element {v} is not in the array")
    else:
        print(f"The element {v} is at position: {res}")'''
    # x = 11
    # n = 3
    # print(x_power_n(x, n))

    arr = [2, 4, 16, 32]
    print(gcd_of_list(arr))
