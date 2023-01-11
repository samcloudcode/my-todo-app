FILEPATH = "todos.txt"


def get_todos(filename=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filename, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filename=FILEPATH):
    """ Write list of to-do items to a text file."""
    with open(filename, 'w') as file_local:
        file_local.writelines(todos_arg)