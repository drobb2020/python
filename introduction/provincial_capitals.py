capitals_dict = {
'Alberta' : 'Edmonton',
'British Columbia' : 'Victoria',
'Manitoba' : 'Winnipeg',
'New Brunswick' : 'Fredricton',
'Newfoundland and Labrador' : 'St. Johns',
'Nova Scotia' : 'Halifax',
'Ontario' : 'Toronto',
'Prince Edward Island' : 'Charlottetown',
'Quebec' : 'Quebec City',
'Saskatchewan' : 'Regina',
'Northwest Territories' : 'Yellowknife',
'Yukon' : 'Whitehorse',
'Nunavut' : 'Iqaluit',
}

import random

provinces = list(capitals_dict.keys())
for i in [1, 2, 3, 4, 5]:
    prov = random.choice(provinces)
    capital = capitals_dict[prov]
    capital_guess = input("What is the capital of " + prov + "? ")

    if capital_guess == capital:
        print("Correct! Nice job.")
    else:
        print("Incorrect. The capital of " + prov + " is " + capital + ".")

print("All done")