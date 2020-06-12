'''Dictionary exercise'''
glossary = {
    'variables': 'a name associated to a int or string.',
    'int': 'an integer or whole number',
    'float': 'a float is a decimal number',
    'string': 'a single word or multiple words together',
    'lists': 'a list of values stored in an array',
    'if statement': 'a way to evaluate an item, true or false, or equal',
    'dictionaries': 'a list of key, value pairs.',
}

for key, value in glossary.items():
    print(key, ': ', value)
