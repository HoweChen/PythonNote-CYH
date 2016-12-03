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
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])  # ['martina', 'michael', 'florence']
print(players[:4])  # ['charles', 'martina', 'michael', 'florence']
print(players[2:])  # ['michael', 'florence', 'eli']
print(players[-3:])  # ['michael', 'florence', 'eli']
print(players[::-1])  # ['eli', 'florence', 'michael', 'martina', 'charles']
players.reverse()
print(players)  # ['eli', 'florence', 'michael', 'martina', 'charles']
for itr in reversed(players):
    print(itr)

# copy a list
another_player = players
another_player.append('howe')
print(players)  # ['eli', 'florence', 'michael', 'martina', 'charles', 'howe']
# still have howe insdie because this copy is a shallow copy
# deep copy
another_player = players[:]
another_player.append('howe')
players.append('chen')
print(another_player)
# ['eli', 'florence', 'michael', 'martina', 'charles', 'howe', 'howe']
print(players)
# ['eli', 'florence', 'michael', 'martina', 'charles', 'howe', 'chen']

# logic
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + "not in banned_users")
test_list = []
if test_list:
    print('not empty')
else:
    print('empty')

# dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x'] = 0
alien_0['y'] = 5
print(alien_0)
del(alien_0['points'])
print(alien_0)
favourite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'python',
    'phil': 'ruby'
}
print('Sarah\'s favourite language is ' +
      favourite_language['sarah'].title() + '.\n')
for i, j in favourite_language.items():
    # one way to tranverse a dictionary
    print("\nName: " + i)
    print("\nValue: " + j)
print('\n----------Another way----------')
for key in favourite_language:
    # another way
    print('\nName: ' + key)
    print('\nValue: ' + favourite_language[key])
for key in favourite_language.keys():
    # print only keys
    print(key + '\n')
for key in sorted(favourite_language):
    # temporary sorted dictionary
    print('\nName: ' + key)
    print('\nValue: ' + favourite_language[key] + '\n')
for value in favourite_language.values():
    # print all value but with duplication
    print(value)
print('Without duplication')
for value in set(favourite_language.values()):
    # without duplication
    # change the values into a set which would not allow the duplication
    print(value)

# nested data structure
alien = []

for number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    alien.append(new_alien)
print(alien)

# list in dictionary
pizza = {
    'crust': 'thick',
    'toppings': ['mushroom', 'pineapple']
}
print(pizza['crust'])
for topping in pizza['toppings']:
    print(topping)

favorite_languages = {'jen': ['python', 'ruby'],
                      'sarah': ['c'],
                      'edward': ['ruby', 'go'],
                      'phil': ['python', 'haskell'], }
for key, languages in favorite_languages.items():
    print(key + ': ', end=' ')  # print() without end with newline
    for language in languages:
        print(language, end=' ')
    print()

# nested dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for user_name, user_info in users.items():
    print(user_name)
    for key, value in user_info.items():
        print('\t' + key + ': ' + value)

# user input
# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)


# function


def greet_user(username):
    """显示简单的问候语"""
    print("Hello, " + username.title() + "!")
greet_user('jesse')


def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type='hamster', pet_name='harry')  # keyword parameter

# any size of parameter


def make_pizza(size, *toppings):
    # parameter which accept any numbers of parameters should set at the last
    # of parameter list
    print('Make pizza with the size ' + str(size) +
          ' and the following toppings: \n')
    for topping in toppings:
        print('- ' + topping + '\n')

make_pizza(13, 'pepperoni')
make_pizza(15, 'mushrooms', 'green peppers', 'extra cheese')


def build_profile(first, last, **user_info):
    # in this case user_info is a empty dictionary
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

# send two key-value pairs
user_profile = build_profile(
    'albert', 'einstein', location='princeton', field='physics')

print(user_profile)

# import function and from module import function
import pizza
pizza.make_pizza(13, 'pepperoni')
pizza.make_pizza(15, 'mushrooms', 'green peppers', 'extra cheese')

from pizza import make_pizza
pizza.make_pizza(13, 'pepperoni')
pizza.make_pizza(15, 'mushrooms', 'green peppers', 'extra cheese')


# change the value of a and b
a = 1
b = 2
a, b = b, a
print(a)
print(b)


# zip
nfc = ["Packers", "49ers"]
afc = ["Ravens", "Patriots"]
for teama, teamb in zip(nfc, afc):
    print(teama + " vs. " + teamb)

# list to a string
teams = ["Packers", "49ers", "Ravens", "Patriots"]
print(", ".join(teams))
