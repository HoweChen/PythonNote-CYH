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
