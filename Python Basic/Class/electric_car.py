import car


class ElectricCar(car.Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # self.battery_size = 70
        self.battery = car.Battery()

    # def describe_battery(self):
    #     print("This car has a " + str(self.battery_size) + "-kWh battery.")
