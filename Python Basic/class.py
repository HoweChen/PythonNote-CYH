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
my_dog.sit()
my_dog.roll_over()


class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print('The car has' + str(self.odometer_reading) + ' miles on it')

    def update_odometer(self, milege):
        if milege >= self.odometer_reading:
            self.odometer_reading = milege
        else:
            print('You cannot roll over the milege')

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # self.battery_size = 70
        self.battery = Battery()

    # def describe_battery(self):
    #     print("This car has a " + str(self.battery_size) + "-kWh battery.")


class Battery():

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.read_odometer()
# my_tesla.describe_battery()
my_tesla.battery.describe_battery()
