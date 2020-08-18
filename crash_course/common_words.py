# Python Crash Course 2e
# Chapter 10 - Files and Exceptions
# common_words.py
# Exercise 10-10 - Common words:
# Write a program that reads the files you found at Project Gutenberg 
# and determines how many times the word 'the' appears in each text. 
# This will be an approximation because it will also count words such as 
# 'then' and 'there'. Try counting 'the ', with a space in the string, 
# and see how much lower your count is.

def count_common_words(filename, word):
    """Count how many times word appears in the text."""
    # Note: This is a really simple approximation, and the number returned
    #   will be higher than the actual count.
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        word_count = contents.lower().count(word)

        msg = f"'{word}' appears in {filename} about {word_count} times."
        print(msg)


filename = 'moby_dick.txt'
count_common_words(filename, 'the')
