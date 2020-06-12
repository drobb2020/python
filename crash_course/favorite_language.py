'''More dictionaries'''
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'java'],
    'phil': ['cobol', 'haskill'],
    'david': ['python', 'bash'],
    'erin': ['java', 'javascript'],
    'brianna': ['bash', 'c++'],
    }

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are: ")
    for language in languages:
        print(f"\t{language.title()}")

# Default:for name, language in favorite_languages.items():
# Default:print(f"{name.title()}'s favorite language is {language.title()}.")

# for name in favorite_languages:
#    print(name.title())

# Default:
# Default:print("\n")
# Default:for name in sorted(favorite_languages.keys()):
# Default:print(f"{name.title()}, thank you for taking the poll.")

# Default:
# Default:if 'erin' not in favorite_languages.keys():
# Default:print("\nErin, please take our poll!")

# Default:
# Default:print("\nThe following languages have been mentioned:")
# Default:for language in set(favorite_languages.values()):
# Default:print(language.title())

# Default:
# Default:print("\n")
# Default:friends = ['phil', 'sarah', 'david']

# Default:
# Default:for name in favorite_languages:
# Default:print(f"Hi {name.title()}.")
# Default:if name in friends:
# Default:language = favorite_languages[name].title()

# candidates = ['josh', 'bryan', 'robert', 'david', 'edward', 'sarah', 'erin', 'jessica']

# for name_c in candidates:
#     for name in favorite_languages.keys():
#         print(f"{name.title()} thank you for taking the poll.")
#     else:
#         print(f"{name_c.title()} please take the favorite languages poll.")
