current_users = ['michael', 'John', 'David', 'James', 'andrew']
new_users = ['brenda', 'robert', 'nick', 'DAVID', 'ANDREW']
print("Before")
print(current_users)
print(new_users)
current_users = [element.lower() for element in current_users]
new_users = [element.lower() for element in new_users]
print("After")
print(current_users)
print(new_users)

for user in new_users:
    if user not in current_users:
        print(f"Adding account for {user}.")
    else:
        print(f"{user} already exists. Try another name!")

print("\nFinished adding new users!")
