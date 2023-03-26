
def product_of_list_even_pos(list):

    if len(list) == 1:
        return None
    else:
        prod = product_of_list_even_pos(list[2:])
        if prod is not None:
            return list[1] * product_of_list_even_pos(list[2:])
        else:
            return list[1]

if __name__ == '__main__':
    list = [2,4,7,8,9]
    print(product_of_list_even_pos(list))
