import json

numbers = [2, 3, 5, 7, 11, 13]
fileName = '/users/howechen/GitHub/PythonNote-CYH/Python Basic/JSON/numbers.json'

# output two a json style file
with open(fileName, 'w') as file_object:
    json.dump(numbers, file_object)

# read from json file
with open(fileName) as file_object:
    new_numbers = json.load(file_object)
print(new_numbers)
