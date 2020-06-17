# fibonacci sequence
from functools import lru_cache

@lru_cache(maxsize = 1000)
# fibonacci_cache = {}

def fibonacci(n):
    # if we have cached the value, then return it
  #  if n in fibonacci_cache:
  #      return fibonacci_cache[n]
    
    # Check that the input is a positive integer
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 1:
        raise ValueError("n must be a positive int")

    #compute the nth term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

    # Cache the value and return it
    # fibonacci_cache[n] = value
    # return value

# fibonacci sequence
for n in range(1, 51):
    print(n, ":", fibonacci(n))

# golden ratio
for n in range(1, 51):
    print(fibonacci(n+1) / fibonacci(n))
