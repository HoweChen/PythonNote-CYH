class Dog():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + "is sitting")

    def roll_over(self):
        print(self.name.title() + "is rolling over")

my_dog = Dog("Willie", 6)
print(my_dog.name)
print(my_dog.age)
