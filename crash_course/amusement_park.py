age = 45
if age < 4:
    print("you are a child, your admission cost is $0.")
elif age < 18:
    print("You are a adolecsent, your admission cost is $25.")
else:
    print("You are an adult, your admission cost is $40.")

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Since you are {age}, your admission cost is ${price}.")

age = 67

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"You are {age}, your admission cost is ${price}.")
