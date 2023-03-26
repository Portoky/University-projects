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



if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 23]
    v = 2
    res = exponential_search(l, v)
    if res == -1:
        print(f"The element {v} is not in the array") # fstrings
    else:
        print(f"The element {v} is at position: {res}")