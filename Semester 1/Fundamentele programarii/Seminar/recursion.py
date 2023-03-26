"""Given a list of integers and a value we wold like to return true or false whether the value is in the list or not."""


def verify_if_number_is_in_list(l, v):
    """
    :param l: list
    :param v: number searched
    :return: True/False whether n is in the list or not
    """
    if len(l) == 0:  # BASE CASE
        return False
    if l[0] == v:
        return True
    return verify_if_number_is_in_list(l[1:], v)


# preconiditin here: the list sorted
def binary_search(l, v):
    if len(l) == 0:
        return False
    m = len(l) // 2  # <==> int(len(l) / 2) whole division
    if l[m] > v:
        return binary_search(l[:m], v)  # < m
    if l[m] < v:
        return binary_search(l[m + 1:], v)
    else:
        return True


"""Merge Sort"""
def merge(left, right):
    sol = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            sol.append(left.pop(0))
        else:
            sol.append(right.pop(0))
    sol.extend(left + right)# Adds the elements of the list to the end of the list -- if we would
                            # have used a .append it would have added a whole list as an element
    return sol


def merge_sort(list):
    if len(list) <= 1:
        return list

    mid = len(list) // 2
    left = merge_sort(list[0: mid])
    right = merge_sort(list[mid:])
    return merge(left, right)

def print_options():
    print("1. Verify if a number is in a list.")
    print("2.Verify if a number is in a sorted list.")
    print("3.Sorts a list")

#not allowed to do computation
def ui_verify_if_number_is_in_list():
    l = [0, 9, 8, 7, 3, 4, 2, 8, 9, 10, 15, 13]
    val = 0
    print(verify_if_number_is_in_list(l, val))

def ui_binary_search():
    l = [0, 2, 3, 4, 7, 8, 8, 9, 9, 10, 13, 15]
    val = 0
    print(binary_search(l, val))

def ui_merge_sort():
    pass #todo
def run_menu():

    options = {1 :ui_verify_if_number_is_in_list, 2 :ui_binary_search, 3:ui_merge_sort}
    while True:
        print_options()
        opt = input("Input your option: ")
        if opt == "x":
            break
        opt = int(opt)
        options[opt]()

        # too much ifs!!
        '''
        if opt == "x":
            break
        opt = int(opt)
        if opt == 1:
            print(verify_if_number_is_in_list(l, val))
        elif opt == 2:
            print(binary_search(l, val))
        elif opt == 3:
            print(merge_sort(l))
        '''


if __name__ == '__main__':
    # testcases to cover each line!
    l = [4, 2, 6, 3 ,1, 7]
    v = 7
    # print(verify_if_number_is_in_list(l, v))
    run_menu()
