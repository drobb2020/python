# Crash Course
# Chapter 9 - Classes


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
    def __init__(self, battery_size=100):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size


    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")


    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100: 
            range = 490

        print(f"This car can go about {range} kilometers on a full charge.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, year, make, model):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar(2020, 'tesla', 'model x')

print(my_tesla.getFullName())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


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
