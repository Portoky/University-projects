
import Domain.complex as c

def create_repository():
    """
    Creates a dict: list of complex numbers, and history witch preserves previous lists of complex numbers
    :return:
    """
    return {"numbers": [], "history": []}

def save_repo_to_history(repo : dict):
    """
    Appends the list of complex numbers to history
    :param repo: complex number represented by a dictionary and the previous list of numbers
    :return: updated repository
    """
    get_history(repo).append(get_list_of_numbers(repo))

def get_list_of_numbers(repo : dict):
    return repo["numbers"]

def get_history(repo : dict):
    return repo["history"]

def set_list_of_numbers(repo: dict, numbers_list : list):
    '''
    the list of numbers is set to the list added as a parameter
    :param repo:
    :param numbers_list:
    :return:
    '''
    updated_list = get_list_of_numbers(repo)
    updated_list.clear()
    for i in numbers_list:
        updated_list.append(i)


###A###
def add_element(repo : dict, z : dict):
    """
    adds a complex numbers z to the list of numbers
    :param repo: the repository represented by a dictionary
    :param z: complex number represented by a dictionary
    """
    save_repo_to_history(repo)
    get_list_of_numbers(repo).append(z)

def insert_element(repo : dict, z: dict, pos : int):
    """
    Inserts the element z at index pos into list numbers in the repository
    :param repo: the repository represented by a dictionary
    :param z: complex number represented by a dictionary
    :param pos: index
    """
    save_repo_to_history(repo)
    get_list_of_numbers(repo).insert(pos, z)

def test_adding_to_list():
    """
    Testing if functionalities of adding a number to repo works well
    AssertionError raised if something goes wrong
    """
    test_repo = create_repository()
    try:
        z = c.create_complex_number(10, 2)
        add_element(test_repo, z)
        assert z in get_list_of_numbers(test_repo), "It should be there"
        z = c.create_complex_number(-5, 2)
        insert_element(test_repo, z, 1)
        assert z == get_list_of_numbers(test_repo)[1], "Element not inserted!"
        remove_element_position(test_repo, 1)
        assert z == get_list_of_numbers(test_repo)[1], "should not be there"

    except AssertionError as a:
        print(a)

###B###
def remove_element_position(repo : dict, pos : int):
    """
    Removes a complex number from the list at the index pos
    :param repo: the repository represented by a dictionary
    :param pos: the position we want to remove the element
    """
    save_repo_to_history(repo)
    del get_list_of_numbers(repo)[pos]


def remove_between_position(repo: dict, start: int, end: int):
    """
    Remove elements from the list of numbers between postions start to end
    :param repo: the repository represented by a dictionary
    :param start: starting postiong / index
    :param end: ending position / index
    """
    save_repo_to_history(repo)
    new_list_of_numbers = []
    old_repo = get_list_of_numbers(repo)

    for i in range(0, start):
        new_list_of_numbers.append(old_repo[i])
    for i in range(end+1, len(old_repo)):
        new_list_of_numbers.append(old_repo[i])

    set_list_of_numbers(repo, new_list_of_numbers)

def test_removing_from_list():
    test_repo = create_repository()
    z1 = c.create_complex_number(5, 2)
    z2 = c.create_complex_number(3, -2)
    z3 = c.create_complex_number(4, 3)
    add_element(test_repo, z1)
    add_element(test_repo, z2)
    add_element(test_repo, z3)
    remove_between_position(test_repo, 0, 1)
    try:
        assert z3 in get_list_of_numbers(test_repo) and z2 not in get_list_of_numbers(test_repo) and z1 not in \
               get_list_of_numbers(test_repo), "Removal doesnt work!"
    except AssertionError as a:
        print(a)

def list_elements(repo : dict):
    """

    :param repo:
    :return: string containing all the complex numbers in a+bi form
    """
    s = ""
    numbers = get_list_of_numbers(repo)
    for number in numbers:
        s += c.complex_to_string(number)
        s += "; "
    return s








