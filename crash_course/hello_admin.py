usernames = []

if usernames:
    for name in usernames:
        if name == 'admin':
            print(f"Hello {name.title()}, would you like to see a status report?")
        else:
            print(f"Hello {name.title()}, thank you for logging in again!")
else:
    print("We really need to find some users!")
