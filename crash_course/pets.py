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
        print(key,":", value)
