# Crash Course
# Chapter 9 - Classes
"""A class that can be used to represent a car."""

class Car():
    """A simple class to represent a car"""
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


    def get_descriptive_name(self):
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
            mileage (int): the current odometer reading of the car
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
