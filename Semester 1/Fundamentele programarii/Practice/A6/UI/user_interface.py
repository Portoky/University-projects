import Domain.repository as r

from Domain.complex import create_complex_number

def ui_list_elements(repo: dict):
    s = r.list_elements(repo)
    print(s)

def ui_add_element(repo : dict, z1 : str):
    pos1 = z1.find("+")
    pos2 = z1.find("-")

    if pos1 != -1:
        pos = pos1
    else:
        pos = pos2
    try:
        real_part = int(z1[:pos])
        im_part = int(z1[pos:len(z1)-1])
    except ValueError:
        print("Wrong arguments for complex numbers.")
        return
    complex_number = create_complex_number(real_part, im_part)
    r.add_element(repo, complex_number)


def ui_remove_element(repo : dict):
    pass

def get_command():
    line = input(">")
    pos = line.find(" ")
    if pos == -1:
        return line, []
    cmd = line[:pos]
    args = line[pos+1:]
    args = args.split(" ")
    for arg in args:
        arg = arg.strip()
    return cmd, args

def solve():
    repo = r.create_repository()
    while True:
        command_0_arg = {"remove": ui_remove_element, "list": ui_list_elements}
        command_1_arg = {"add": ui_add_element}
        cmd, args = get_command()
        if len(args) == 0:
            if cmd == "exit":
                break
            try:
                command_0_arg[cmd](repo)
            except KeyError:
                print("Command not implemented yet")
        if len(args) == 1:
            try:
                command_1_arg[cmd](repo, *args)
            except KeyError:
                print("Command not implemented yet")
            except TypeError:
                print("Wrong syntax")





