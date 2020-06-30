# Crash Course
# Chapter 7 - User input and while loops
# Exercise 7-5. Movie Tickets: A movie theater 
# charges different ticket prices depending on a 
# person’s age. 
# If a person is under the age of 3, the ticket is free; 
# if they are between 3 and 12, the ticket is $10;
# and if they are over age 12, the ticket is $15. 
# Write a loop in which you ask 
# users their age, and then tell them the cost of 
# their movie ticket.
prompt = ("\nWelcome to tonights movie! Please tell me the ages of everyone with you. ")
prompt += ("Enter '0' when you are done! ")

while True:
    age = input(prompt)
    age = int(age)
    tickets = []

    if age == 0:
        break
    elif age < 3:
        price = 0
        print(
            f"Since you are {age} years old, your admission cost is ${price}.")
        tickets.append(price)
        print(tickets)
    elif age < 13:
        price = 10
        print(
            f"Since you are {age} years old, your admission cost is ${price}.")
        tickets.insert(len(tickets), price)
        print(tickets)
    else:
        price = 15
        print(
            f"Since you are {age} years old, your admission cost is ${price}.")
        tickets.insert(len(tickets), price)
        print(tickets)

print(tickets)
total = 0
ele = 0
# Give a Grand total and enjoy message.
# Iterate each element in list
# and add them in variale total
while(ele < len(tickets)):
    total = total + tickets[ele]
    ele += 1

# printing total value of movie tickets
print(f"Your cost this evening is: ${total}")
print("Enjoy the movie and have a free bag of Popcorn on us.")
