
prefix = " Python is an "
suffix = "awesome language."

astr = prefix + suffix
print(astr)

astr = astr.replace("language", "snake.")
print(astr)

astr = astr * 2
astr = astr.replace("snake.", "language", 1)
print(astr)

n = 11
f = 1.23456789
s ="computer"

print("my number is {:d}".format(n))
print("my number is {:b}".format(n))

print("{:f}".format(f))
print("{:.3f}".format(f))
print("{:011.3f}".format(f))

print("{name} own(s) {amount} of {object}".format(
    name = "William",
    amount = "5",
    object = "bananas"
))
