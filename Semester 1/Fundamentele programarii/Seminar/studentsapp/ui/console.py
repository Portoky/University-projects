from studentsapp.domain.operations import add_student


def read_command():
    command = input(">")
    pos = command.find(" ")
    if pos == -1:
        return command, []
    cmd = command[:pos]
    args = command[pos + 1:]
    args = args.split(',')
    args = [s.strip() for s in args]
    return cmd, args


def add_students(all_students, id, name, grade):
    try:
        id = int(id)
        grade = int(grade)
        name = str(name)
        operations.add_student(all_students, id, name,grade)
    except ValueError as ve:
        print("Invalid input", ve)

def print_command(commands):
    print(*list(commands.keys()),"exit",sep="\n")


def print_all(all_students):
    print(all_students)


def run_console():
    commands = {"add": add_student, "print": print_all}
    all_students = []
    while True:
        print_command(commands)
        cmd, args = read_command()
        if cmd == "exit":
            break
        try:
            commands[cmd](all_students, *args)
        except KeyError as ke:
            print("This option is not yet implemented", ke)
        except TypeError as te:
            print("Invalid use of the function: ",te)