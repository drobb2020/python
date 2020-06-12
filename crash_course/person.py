'''person.py dictionaries'''
person_0 = {
    'first_name': 'caroline',
    'last_name': 'cannon',
    'age': 52,
    'city': 'portage la prairie'
}

person_1 = {
    'first_name': 'robert',
    'last_name': 'telka',
    'age': 45,
    'city': 'barhaven'
}

person_2 = {
    'first_name': 'ben',
    'last_name': 'mulroney',
    'age': 48,
    'city': 'toronto'
}

people = [person_0, person_1, person_2]

for person in people:
    for key, value in person.items():
        print(key, ":", value)
    # print(person['first_name'])
    # print(person['last_name'])
    # print(person['age'])
    # print(person['city'])
    # # print(f"\tLocation: {p[city.title()]}")
    # # for first_name, last_name, age, city in person_0.items():
    # #     full_name = f"{first_name} {last_name}"
    # #     print(full_name)
    # print(person.get('fist_name')),
    # print(person.get('age')),
    # print(person.get('city')),
