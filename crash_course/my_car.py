# Crash Course
# Chapter 9 - Classes

from car import Car, ElectricCar

my_new_car = Car('audi', 'a4', 2019)

print(f'\nI have a new car it is a {my_new_car.get_descriptive_name()}')

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
print("")
my_tesla = ElectricCar('tesla', 'model x', 2020)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
