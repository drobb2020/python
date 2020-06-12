import datetime as dt


def record_time(message, time=dt.datetime.now()):
    # save to a file or print
    print("{:}, time: {:}".format(message, time))


record_time("It is the morning")

# def add(a, b, c):
#    return a + b + c

# print(add(1, 2, 3))


def add(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total


print(add(1, 2, 3, 4, 5, 6))
