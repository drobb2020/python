# prime number checker
n = int(input("Enter a number to check, n: "))
if n >= 2:
    divisors = []
    for divisor in range(2, n):
        if n % divisor == 0:
            divisors.append(divisor)

    if len(divisors) == 0:
        print("{:d} is a prime number!".format(n))
    else:
        print("{:d} is not a prime number because {:} divide {:d}".format(n, str(divisors), n))
