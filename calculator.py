import sys

operator_list = ['+', '-', '*', '/']
operator_priority = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3
}

number_stack = []
operator_stack = []


def is_num(str):
    try:
        int(str)
        return True
    except Exception:
        return False


def arithmetic_operation(left, operator, right):
    result = 0
    if operator == '+':
        result = left + right
    elif operator == '-'
        result = left - right
    elif operator == '*':
        result = left * right
    elif operator == '/':
        result = left / right
    elif operator == '^':
        result = left ** right
    return result


def calculate(input_str):
    if is_num(input_str):
        return int(input_str)
    else:
        for operator in operator_list:
            if operator not in input_str and ' ' in input_str:
                return 'Error'
        # till here, which means the expression is correct
        input_str = input_str.replace(' ', '')
        for char in input_str:
            if is_num(char):
                number_stack.append(int(char))
            else:
                if char != ')':
                    operator_stack.append(char)
                else:
                    right = number_stack.pop()
                    left = number_stack.pop()
                    operator = operator_stack.pop()
                    result = arithmetic_operation(left, operator, right)
                    number_stack.append(result)
        while len(number_stack > 1):

        return result


if __name__ == '__main__':
    input_str = sys.stdin.readline()
    print(calculate(input_str))
