# Crash Course
# Chapter 8 - Functions

def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
    
    
musician = build_person('jimi', 'hendrix', age=27)
print(musician)

musician = build_person('paul', 'McCartney', age=78)
print(musician)
