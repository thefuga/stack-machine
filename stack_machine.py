import re


def stack_machine():

    push = 'PUSH'
    operations = { 'ADD': add,
                   'SUB': sub,
                   'MULT': mult,
                   'DIV': div }
    stack = []

    try:
        while True:
            entry = input()
            if entry in operations:
                b = stack.pop() if stack else None
                a = stack.pop() if stack else None
                stack.append(operations[entry](a, b))
            elif push in entry:
                stack.append(float(re.sub(' +', ' ', entry).split(' ')[1]))
            else:
                raise EOFError
    except EOFError:
        print(stack.pop())


def add(a, b):
    return a + b if a and b else a or b


def sub(a, b):
    return a - b if a and b else a or b


def mult(a, b):
    return a * b if a and b else a or b


def div(a, b):
    return a / b if a and b else a or b


if __name__ == "__main__":
    stack_machine()
