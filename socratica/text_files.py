# Socratica tutorial
# working with text files

# print(help(open))
#f = open("c:/Users/David/Documents/Scripts/python/socratica/guido_bio.txt")
#text = f.read()
#f.close()

#print(text)

try:
     with open("c:/Users/David/Documents/Scripts/python/socratica/guido_bio.txt") as f:
         text = f.read()
except FileNotFoundError:
    text = None

print(text)

oceans = ["Pacific", "Atlantic", "Indian", "Southern", "Arctic"]

with open("c:/Users/David/Documents/Scripts/python/socratica/oceans.txt", "w") as f:
    for ocean in oceans:
#        f.write(ocean)
#        f.write("\n")
        print(ocean, file=f)

with open("c:/Users/David/Documents/Scripts/python/socratica/oceans.txt", "a") as f:
    print(39*"=", file=f)
    print("These are the five oceans of the world.", file=f)
s