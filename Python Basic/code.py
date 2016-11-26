# print Ada Lovelace
name = "ada lovelace"
print(name.title())


# print 'Pythonhaha'
favourite_language = "Pythonhaha  "
print("'" + favourite_language.rstrip() + "'")

# print 'Pythonhaha'
favourite_language = "  Pythonhaha"
print("'" + favourite_language.lstrip() + "'")

# list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)  # ['honda', 'yamaha', 'suzuki']
motorcycles.append('fuck')
print(motorcycles)  # ['honda', 'yamaha', 'suzuki', 'fuck']
motorcycles.insert(0, 'test')
print(motorcycles)  # ['test', 'honda', 'yamaha', 'suzuki', 'fuck']
del motorcycles[0]
print(motorcycles)  # ['honda', 'yamaha', 'suzuki', 'fuck']
del motorcycles[motorcycles.__len__() - 1]
print(motorcycles)  # ['honda', 'yamaha', 'suzuki']
popped_element = motorcycles.pop()
print(popped_element)  # suzuki
print(motorcycles)  # ['honda', 'yamaha']
cars = ['audi', 'subaru', 'bmw', 'toyata']
cars.sort()
print(cars)  # ['audi', 'bmw', 'subaru', 'toyata']
cars.sort(reverse=True)
print(cars)  # ['toyata', 'subaru', 'bmw', 'audi']
print('Here is the original order')
print(cars)  # ['toyata', 'subaru', 'bmw', 'audi']
print('Here is the sorted order')
print(sorted(cars))  # ['audi', 'bmw', 'subaru', 'toyata']
print('Here is the original order again')
print(cars)  # ['toyata', 'subaru', 'bmw', 'audi']
print(sorted(cars, reverse=True))  # can also reverse in sorted()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)  # ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)  # ['subaru', 'toyota', 'audi', 'bmw'] different from reverse=True
print(len(cars))

# Tranverese the list
magicians = ['alice', 'david', 'carolina']
for magican in magicians:
    print(magican)
    print(magican.title() + 'has done a great job')

# range()
for value in range(1, 5):
    print(value)
numbers = list(range(1, 6))
print(numbers)
even_numbers = list(range(2, 11, 2))
print(even_numbers)

square = list()
for value in range(1, 11):
    value *= value  # or value = value**2
    square.append(value)
print(square)
for value in square:
    print(value)
print('Min of square')
print(min(square))
print('Max of square')
print(max(square))
print('Sum of square')
print(sum(square))
