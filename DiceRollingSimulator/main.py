import random


def define_random():
    _MIN = 1
    _MAX = 6
    return random.randrange(_MIN, _MAX)


def check_true(inp_char):
    if inp_char == 'Y' or inp_char == 'y':
        return True
    return False


if __name__ == "__main__":
    choice = True
    while choice:
        x = define_random()
        print("Random number: ", x)
        print("Press Y to continue; any character to stop.")
        if check_true(input()):
            choice = True
        else:
            choice = False
