def make_pizza(size, *toppings):
    # parameter which accept any numbers of parameters should set at the last
    # of parameter list
    print('Make pizza with the size ' + str(size) +
          ' and the following toppings: \n')
    for topping in toppings:
        print('- ' + topping + '\n')