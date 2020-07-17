# Crash Course
# Chapter 9 - Classes
# Exercise 9-9. Battery Upgrade: 
# Use the final version of electric_car.py from 
# this section. Add a method to the Battery class 
# called upgrade_battery(). This method should check the 
# battery size and set the capacity to 100 if it isn’t 
# already. Make an electric car with a default battery size, 
# call get_range() once, and then call get_range() a second 
# time after upgrading the battery. You should see an increase 
# in the car’s range.

class Car():
    """A simple class to represent a car
    """
    def __init__(self, year, make, model):
        """initialize attributes to describe the car

        Args:
            year (str): The year the car was produced
            make (str): The car company that made the vehicle
            model (str): The model of the car
            odometer_reading (int): mileage of the car
        """
        self.year = year
        self.make = make
        self.model = model
        self.odometer_reading = 0


    def getFullName(self):
        """Return a neatly formated string about the car"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


    def read_odometer(self):
        """Read the cars odometer
        """
        print(f"This car has {self.odometer_reading} kiometers on it.")


    def update_odometer(self, mileage):
        """Set the odometer to a given reading
            Reject the change if it attempts to roll-back the
            odometer.

        Args:
            mileage ([int): the current odometer reading of the car
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Shame on you. You cannot roll back an odometer!")


    def increment_odometer(self, kilometers):
        """Add the given amount to the odometer reading.

        Args:
            kilometers (int): additional miles driven
        """
        self.odometer_reading += kilometers


class Battery():
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size


    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")


    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 518
        elif self.battery_size == 100: 
            range = 564
        else:
            range = 647
        print(f"This car can go about {range} kilometers on a full charge.")
    
    def upgrade_battery(self):
        """Upgrade the battery to a larger range"""
        if self.battery_size < 100:
            self.battery_size = 100


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, year, make, model):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()


# my_tesla = ElectricCar(2020, 'tesla', 'model 3')
# my_tesla = ElectricCar(2020, 'tesla', 'model s')
my_tesla = ElectricCar(2020, 'tesla', 'model x')

print("")
print(my_tesla.getFullName())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
print("")
# print(my_tesla2.getFullName())
# my_tesla2.battery.describe_battery()
# my_tesla2.battery.get_range()
# print("")
# print(my_tesla3.getFullName())
# my_tesla3.battery.describe_battery()
# my_tesla3.battery.get_range()

# new_car = Car('2020', 'toyota', 'camary')
# print(new_car.getFullName())
# new_car.update_odometer(900)
# new_car.read_odometer()

# used_car = Car(1999, 'subaru', 'forester')
# print(used_car.getFullName())
# used_car.update_odometer(23500)
# used_car.read_odometer()
# used_car.increment_odometer(250)
# used_car.read_odometer()
