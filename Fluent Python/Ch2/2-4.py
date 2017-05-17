colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)

# another way to code

for color in colors:
    for size in sizes:
        print((color, size))
        # or we could just set it as a list then change to tuple
        # print(tuple([color, size]))
