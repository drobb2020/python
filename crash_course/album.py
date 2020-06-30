# Crash Course
# Chapter 8 - Functions
# Exercise 8-7. Album: Write a function called 
# make_album() that builds a dictionary describing 
# a music album. The function should take in an 
# artist name and an album title, and it should 
# return a dictionary containing these two pieces 
# of information. Use the function to make three 
# dictionaries representing different albums. 
# Print each return value to show that the 
# dictionaries are storing the album information 
# correctly.Use None to add an optional parameter 
# to make_album() that allows you to store the number 
# of songs on an album. If the calling line includes 
# a value for the number of songs, add that value to 
# the album’s dictionary. Make at least one new function 
# call that includes the number of songs on an album.

def make_album(artist_f_name, artist_l_name, album_name, year=None):
    """Make a dictionary of albums listing artist and album name."""
    album = {'first': artist_f_name, 'last': artist_l_name, 'album': album_name}
    if year:
        album['year'] = year
    return album


while True:
    print("\nPlease provide the name of an Artist, an Album and the year it was relased (if known):")
    print("(enter 'q' at any time to quit)")
    artist_f_name = input("Artist First Name: ")
    if artist_f_name == 'q':
        break
    artist_l_name = input("Artist Last Name: ")
    if artist_l_name == 'q':
        break
    album_name = input("Album Name: ")
    if album_name == 'q':
        break
    year = input("Released: ")
    if year == 'q':
        break

    album_entry = make_album(artist_f_name, artist_l_name, album_name, year)
    print(f"\n{album_entry}!")
