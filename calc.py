# Perform simple arithmetic encoded in an input string:
<<<<<<< HEAD
# '1 + 2' -> 3, or '1 - 2' -> -1.def compute(expression):
    values = expression.split(' ')
    num0 = int(values[0])
    operator = values[1]
    num1 = int(values[2])
=======
# '1 + 2' -> 3, or '1 - 2' -> -1.
def compute(expression):
    num0, operator, num1 = expression.split(' ')
    num0, num1 = int(num0), int(num1)
>>>>>>> use-unpacking
    if operator == '+':
        return num0 + num1
    elif operator == '-':
        return num0 - num1
    else:
        print('unknown operator!')
        return None
