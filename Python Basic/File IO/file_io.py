with open('/users/howechen/GitHub/PythonNote-CYH/Python Basic/File IO/test.txt') as file_object:
    # print contents line by line
    # for line in file_object:
    #     print(line.rstrip())

    # print contents
    # contents = file_object.read()
    # print(contents)

    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))


# different mode of open() 'w', 'r', 'a', 'r+'
with open('/users/howechen/GitHub/PythonNote-CYH/Python Basic/File IO/write.txt', 'w') as file_object:
    file_object.write('Fuck you')
