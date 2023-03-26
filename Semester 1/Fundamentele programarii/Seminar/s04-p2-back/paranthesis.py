"""
@author: radu

Parenthesis: generate all sequences of n parentheses that close correctly.
Example: for n=4 there are two solutions: (()) and ()().
"""


def initial_value():
    return -1


def first(x):
    return 0


def next_elem(x, n):
    if x[-1] == 1:
        return None
    return x[-1] + 1


def consistent(x, n):
    zeros = x.count(0)
    return len(x) - zeros <= zeros <= n // 2


def is_solution(x, n):
    return len(x) == n


def output_solution(x):
    l = ("(" if e == 0 else ")" for e in x)
    print("".join(l))


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


# back_rec([], 4)
back_iter(4)
