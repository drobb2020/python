# Crash Course
# Chapter 9 - Classes

class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age, birthday):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
        self.bday = birthday
    
    
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")


    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")
    
    def shake_paw(self):
        """Simulate shaking a paw."""
        print(f"{self.name} is shaking paw!")

    def barking(self):
        """Simulate a dog barking."""
        print(f"{self.name} is barking!")


my_dog = Dog('Abigail', 2, 'July 3rd')
your_dog = Dog('Champ', 2, 'March 15th')

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
print(f"{my_dog.name}'s birthday is {my_dog.bday}.")

my_dog.sit()
my_dog.roll_over()
my_dog.shake_paw()
my_dog.barking()

print(f"My dog's name is {your_dog.name}.")
print(f"My dog is {your_dog.age} years old.")
print(f"{your_dog.name}'s birthday is {your_dog.bday}.")

your_dog.sit()
your_dog.roll_over()
your_dog.shake_paw()
your_dog.barking()
