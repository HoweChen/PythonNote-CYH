import string
import re
import sys


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack(object):
    def __init__(self):
        self.top = None

    def peek(self):
        if self.top != None:
            return self.top.val
        else:
            return None

    def push(self, n):
        n = Node(n)
        n.next = self.top
        self.top = n
        return n.val

    def pop(self):
        if self.top == None:
            return None
        else:
            tmp = self.top.val
            self.top = self.top.next
            return tmp


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mult(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


operation = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div
}


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


weight = {
    '(': 3,
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
    None: 0
}

num1 = 0
num2 = 0
result = 0
data_stack = Stack()
oper_stack = Stack()


def deal_data():
    p = oper_stack.pop()
    num2 = float(data_stack.pop())
    num1 = float(data_stack.pop())
    result = operation[p](num1, num2)
    data_stack.push(result)
    return result


if __name__ == '__main__':
    equation = sys.stdin.readline().strip()
    operator = ['+', '-', '*']
    is_error = False

    for i in operator:
        if i not in equation and equation.find(' ') == True:
            is_error = True
            break

    if is_error:
        print('Error')
    else:
        equation = equation.replace(' ', '')

        try:
            equation = int(equation)
            print(equation)
        except Exception:

            while equation:
                cur = re.search(r'((^\d+\.?\d*)|(^\(\-\d+\.?\d*)|\(|\)|\+|\-|\*|/)', equation).group()
                if "(-" in cur:

                    bracket = cur[0]
                    oper_stack.push(bracket)
                    equation = equation[1:]

                    num = cur[1:]
                    data_stack.push(num)
                    equation = equation[len(num):]
                else:
                    lenth = len(cur)
                    if is_number(cur):
                        data_stack.push(cur)
                    else:
                        if cur == "(":
                            oper_stack.push(cur)
                        elif cur == ")":
                            deal_data()

                            while oper_stack.peek() != "(":
                                deal_data()
                            oper_stack.pop()

                        else:
                            if oper_stack.peek() == None:
                                oper_stack.push(cur)
                            else:

                                if weight[cur] > weight[oper_stack.peek()]:
                                    oper_stack.push(cur)
                                else:
                                    if oper_stack.peek() == "(":
                                        oper_stack.push(cur)
                                    else:
                                        deal_data()
                                        while weight[cur] == weight[oper_stack.peek()]:
                                            deal_data()
                                        oper_stack.push(cur)

                    equation = equation[lenth:]

            result = deal_data()
            while oper_stack.peek() != None:
                result = deal_data()

            print(int(result))
