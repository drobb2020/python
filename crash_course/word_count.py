# Python Crash Course 2e
# Chapter 10 - Files and Exceptions
# word_count.py

def count_words(filename):
    """count words in a file
    """
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # print(f"Sorry, the file {filename} does not exist.")
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filename = 'alice.txt'
count_words(filename)

filenames = ['a_tale_of_two_cities.txt', 'bleak_house.doc', 'david_copperfield.txt', 'great_expectations.txt', 'hard_times.txt', 'martin_chuzzlewit.txt', 'nicholas_nickleby.txt']
for filename in filenames:
    count_words(filename)
