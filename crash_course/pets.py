pet_0 = {
    'pet': 'dog',
    'owner': 'david'
}
pet_1 = {
    'pet': 'cat',
    'owner': 'tracy'
}
pet_2 = {
    'pet': 'rabbit',
    'owner': 'john'
}
pet_3 = {
    'pet': 'turtle',
    'owner': 'fraser'
}

pets = [pet_0, pet_1, pet_2, pet_3]

for pet in pets:
    for key, value in pet.items():
        print(key, ":", value)

pets2 = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets2)

while 'cat' in pets2:
    pets2.remove('cat')

print(pets2)


def describe_pet(animal_breed, pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_breed.title()}'s name is {pet_name.title()}.")
    
describe_pet('west highland white terrier', 'abigail')
describe_pet('chihuahua', 'champ')
describe_pet(animal_type='hamster', animal_breed='golden', pet_name='harry')
describe_pet()
