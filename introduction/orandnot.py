
# or, and, not

T = True
F = False

statement1 = 3 > 4  # False
statement2 = 10 % 5 == 0  # True
statement3 = "A".lower() == "a"  # True

# or
if F or F:
    print("F or F")
if F or T:
    print("F or T")
if T or F:
    print("T or F")
if T or T:
    print("T or T")

# and
if F and F:
    print("F and F")
if F and T:
    print("F and T")
if T and F:
    print("T and F")
if T and T:
    print("T and T")

# not
if not F:
    print("Not F")
if not T:
    print("Not T")
