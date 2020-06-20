# Socratica tutorial
# working with json files

import json
# print(dir(json))

json_file = open("c:/Users/David/Documents/Scripts/Python/socratica/movie_1.txt", "r")
movie = json.load(json_file)
json_file.close()

print(movie)
