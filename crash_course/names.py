names = ['robert', 'Nick', 'Mark', 'Eric', 'Calvin', 'Michael', 'John']

print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())
print(names[4].title())
print(names[5].title())
print(names[6].title())
print("\n")

greeting = "welcome to my Python crash course!"
for n in names:
    print(f"{n.title()}" + "," + " " + f"{greeting}")

transport = ["plane", "train", "automobile", "ship", "sailboat", "bike", "scooters"]

# print(transport)
# print(transport[0])
transport1 = "I like to fly by" + " " + f"{transport[0]}" + "."
transport2 = "I once took a" + " " + \
    f"{transport[1]}" + " " + "trip from London, England to Paris, Frnace \
through the channel tunnel on a high spped " + f"{transport[1]}" + "."
transport3 = "The" + " " + f"{transport[2]}" + " " + \
    "has become the primary mode of transportation for most people."
transport4 = "I worked on a" + " " + f"{transport[3]}" + " " + \
    "for over 12 years with the Canadian Coast Guard. I love the sea."
transport5 = "When I was young, my father owned a" + " " + \
    f"{transport[4]}" + "."
transport6 = "I like to use my" + " " + f"{transport[5]}" \
    + " " + "on Sundays in Ottawa."
transport7 = "My dog, Abigail, is afraid of " + f"{transport[6]}" + "."

print(transport1)
print(transport2)
print(transport3)
print(transport4)
print(transport5)
print(transport6)
print(transport7)
