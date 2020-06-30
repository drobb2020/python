# Crash Course
# Chapter 7 - User input and while loops

"""Let's see if you are tall enough to safely ride on a roller coster. This
    is not discrimination, this is to make sure you are safe on the ride."""

# Ask how tall the person is
height = input("How tall are you, in inches? ")

# Convert the answer from a string to an integer (str > int)
height = int(height)

# Evaluate the height to see if they can ride
if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
