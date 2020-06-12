# requested_toppings = ['extra cheese', 'pineapple', 'ham']
# if requested_toppings != 'anchovies':
#    print("Hold the anchovies!")
# if 'pepperoni' in requested_toppings:
#    print("Adding Pepperoni")
# if 'mushrooms' in requested_toppings:
#    print("Adding mushrooms")
# if 'bacon' in requested_toppings:
#    print("Adding bacon")
# if 'ham' in requested_toppings:
#    print("Adding ham.")
# if 'pineapple' in requested_toppings:
#    print("Adding pineapple.")
# if 'extra cheese' in requested_toppings:
#    print("Adding extra cheese.")
#
# if 'pepperoni' and 'bacon' and 'mushrooms' in requested_toppings:
#    print("You ordered a Canadian pizza")
#
# if 'extra cheese' and 'ham' and 'pineapple' in requested_toppings:
#    print("You ordered a cheesy Hawaiian pizza")

# requested_toppings = ['pepperoni', 'mushrooms', 'green peppers', 'extra cheese']
# for requested_topping in requested_toppings:
#    print(f"Adding {requested_topping}.")
# print("\nFinished making your pizza!")

# for requested_topping in requested_toppings:
#    if requested_topping == 'green peppers':
#        print("Sorry, we are out of green peppers right now.")
#    else:
#        print(f"Adding {requested_topping}.")
#
# print("\nFinished making your pizza!")

# requested_toppings = []
# if requested_toppings:
#    for requested_topping in requested_toppings:
#        print(f"Adding {requested_topping}.")
#        print("\nFinished making your pizza!")
# else:
#    print("Are you sure you want a plain pizza?")
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese',
                      'black olives', 'green olives', 'ham',
                      'chicken', 'spinach', 'sausage']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")
