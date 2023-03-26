"""
@author: radu

N-Queens: chessboard queens can attack horizontally, vertically, and diagonally.
Display all possibilities of placing n queens on an nxn chessboard such that they don't
attack each other.
"""


def first(x):
    return 0


def consistent(x, n):
    k = len(x) - 1
    if x[k] in x[:k]:
        return False
    for i in range(k):
        if k - i == abs(x[k] - x[i]):
            return False
    return True


def is_solution(x, n):
    return len(x) == n


def output_solution(x):
    print(x)


def next_elem(x, n):
    if x[len(x) - 1] == n - 1:
        return None
    return x[len(x) - 1] + 1


def initial_value():
    return -1


def back_rec(x, n):
    el = first(x)
    x.append(el)
    while el is not None:
        if consistent(x, n):
            if is_solution(x, n):
                output_solution(x)
            else:
                back_rec(x[:], n)
        el = next_elem(x, n)
        x[-1] = el




back_rec([], 8)






















def back_iter(n):
    x = [initial_value()]
    while len(x) > 0:
        el = next_elem(x, n)
        while el is not None:
            x[-1] = el
            if consistent(x, n):
                if is_solution(x, n):
                    output_solution(x)
                else:
                    x.append(initial_value())
                    break
            el = next_elem(x, n)
        if el is None: x = x[:-1]


back_rec([], 4)
# back_iter(4)
