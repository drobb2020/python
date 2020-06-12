a_list = list(range(1, 10))
# print(a_list)
for a in a_list:
    print(a)
for a in a_list:
    if a == 1:
        print(f"{a}st")
    elif a == 2:
        print(f"{a}nd")
    elif a == 3:
        print(f"{a}rd")
    else:
        print(f"{a}th")

print("there are all your numbers.")
