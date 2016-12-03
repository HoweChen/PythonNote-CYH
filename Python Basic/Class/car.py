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
        print('The car has ' + str(self.odometer_reading) + ' miles on it')

    def update_odometer(self, milege):
        if milege >= self.odometer_reading:
            self.odometer_reading = milege
        else:
            print('You cannot roll over the milege')

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery():

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            self.range = 240
        elif self.battery_size == 85:
            self.range = 70
        message = "This car can go approximately " + str(self.range)
        message += " miles on a full charge."
        print(message)

# my_tesla = ElectricCar('tesla', 'electric_car', 2016)
# my_tesla.read_odometer()
# my_tesla.describe_battery()
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()
