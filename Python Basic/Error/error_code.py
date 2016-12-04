try:
    one = int(input('First number: '))
    two = int(input('Second number: '))
    result = one / two
except ZeroDivisionError as ZDE:
    print('You cannot divide by zero')
else:
    print(result)
