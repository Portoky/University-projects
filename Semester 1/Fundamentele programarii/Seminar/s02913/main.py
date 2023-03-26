"""

@author: radu


 
"""

def check_for_number (l, v):
    if len(l)==0:
        return False
    if v==l[0]:
        return True
    return check_for_number(l[1:],v)

def binary_search(l, v):
    '''
    :param l: list, sorted
    :param v:
    :return:
    '''
    if len(l) == 0:
        return False
    m = len(l)//2
    if v == l[m]:
        return True
    if(v > l[m]):
        return binary_search(l[(m+1):],v)
    return binary_search(l[:m],v)


def merge(left, right):
    result = []
    while len(left)>0 and len(right)>0:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    result.extend(left+right)
    return result

def merge_sort(l):
    if len(l)<2:
        return l
    mid = len(l) // 2
    left = merge_sort(l[:mid])
    right = merge_sort(l[mid:])
    return merge(left, right)


def print_options():
    pass


def run_menu():
    commands = {1:check_for_number, 2:binary_search}
    while True :
        print_options()
        option = input("Option =")
        if option == 'x':
            break
        option = int(option)
        commands[option]()

if __name__ == '__main__':
    print("hello")
    #print (check_for_number([1,4,7,9,11],3))
    print(binary_search([], 9))
    print(merge_sort([1,3,2,7,4,5,10,33,27]))

