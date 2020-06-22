# Socratica tutorial
# Exceptions

# Syntax error example - missing : at end of for statement
# for i in range(5):
#    print("Hello world!")

# Division by zero always generates an error
# 1/0

# Opening a non-existant file
#with open("x_files.txt") as xf:
#    the_truth = xf.read()

# print(the_truth)

# trying an operation on mismatched values (str and int)
# 1 + 2 + "three"

# Square root of a complex number
# import math

#print(math.sqrt(-1))

# handling errors and exceptions with try, except, else, and finally
import logging
import time

# Create a logger
logging.basicConfig(filename = "c:\\Users\\David\\Documents\\Scripts\\python\\socratica\\problem.log", level = logging.DEBUG)
logger = logging.getLogger()

def read_file_timed(path):
    """Return the contents of the file at 'path' and measure the time required."""
    start_time = time.time()
    try:
        f = open(path, mode="rb")
        data = f.read()
        return data
    except FileNotFoundError as err:
        logger.error(err)
        raise
    else:
        f.close()
    finally:
        stop_time = time.time()
        dt = stop_time - start_time
        logger.info("Time required for {file} = {time}".format(file=path, time=dt))


# data = read_file_timed("c:/Users/David/Music/ABBA/ABBA/04 S.O.S.mp3")
# data = read_file_timed("c:/Users/David/Videos/Abigail/test.mov")
data = read_file_timed("c:/Users/David/Documents/imaginary_file.png")
