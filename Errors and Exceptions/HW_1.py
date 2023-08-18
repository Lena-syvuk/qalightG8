# Task_1

a = input("Input number: ")
try:
    number = int(a)
    print(f' Your number {number}')
except ValueError:
    print("entered not valid data")

# Task_2

a = input("Input number: ")
b = input("Input second number: ")
try:
    a = int(a)
    b = int(b)
    print(f' Your number {a + b} ')
except ValueError:
    print(a + b)

# Task_3
while True:
    try:
        n = input("Please enter an number: ")
        n = int(n)
        break
    except ValueError:
        print(" Please try again ...")
print("Great, you entered an number!")

# Task_4


class OnlyEventError(Exception):
    def __init__(self, parameter):
        self.parameter = parameter


def check_digit(parameter):
    if parameter % 2 == 0:
        return parameter
    else:
        raise OnlyEventError(f'{parameter}, is not a multiple, try again')


print(check_digit(12))

# Task_5


def function(parameter):
    try:
        check_digit(parameter)
    except Exception:
        parameter = parameter + 1
        print(parameter)
    else:
        parameter = int(parameter) * 2
        print(parameter)
    finally:
        print('i always print something')


function(50)