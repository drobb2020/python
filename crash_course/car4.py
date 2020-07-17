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
        """Return a neatly formated string about the car
        """
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


new_car = Car('2020', 'toyota', 'camary')
print(new_car.getFullName())
new_car.update_odometer(900)
new_car.read_odometer()

used_car = Car(1999, 'subaru', 'forester')
print(used_car.getFullName())
used_car.update_odometer(23500)
used_car.read_odometer()
used_car.increment_odometer(250)
used_car.read_odometer()
