from cmath import inf

def binary_search(l, start, end, v):

    while(start <= end):
        mid = (start + end) // 2
        if l[mid] < v:
            start = mid + 1
        elif l[mid] > v:
            end = mid - 1
        else:
            return mid

        return -1


def exponential_search(l, v):
    i = 1
    while i <= len(l) and l[i-1] <= v:
        i *= 2

    if i < len(l):
        return binary_search(l, (i//2)-1, i-1, v)#u could have used slices
    else:
        return -1


def exponential_n(x, n):
    if n == 0:
        return 1
    x_power = exponential_n(x, n // 2)
    if n % 2 == 1:
        return x * x_power * x_power
    return x_power * x_power

def max_recursively(l):
    if len(l) == 0:
        return -inf
    if len(l) == 1:
        return l[0]
    else:
        mid = len(l) // 2
        left = max_recursively(l[:mid]) # mid -1
        right = max_recursively(l[mid:])
        if left < right:
            return right
        return left 

def greatest_common_divisor(a, b):
    while b != 0:
        m = a % b
        a = b
        b = m
    return a

def greatest_common_divisor_list(l):
    if len(l) == 1:
        return l[0]
    else:
        mid = len(l) // 2
        return greatest_common_divisor(greatest_common_divisor_list(l[:mid]), greatest_common_divisor_list(l[mid:]))

if __name__ == '__main__':
    '''
    x = 2
    n = 8
    print(exponential_n(2, 8))
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 23]
    v = 2
    res = exponential_search(l, v)
    if res == -1:
        print(f"The element {v} is not in the array") # fstrings
    else:
        print(f"The element {v} is at position: {res}")
    '''
    l = [6, 9, 33, 18]
    print(greatest_common_divisor_list(l))
