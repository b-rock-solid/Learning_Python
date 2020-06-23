# Try It Yourself Exercise - Pg.142
# 8-8 User Albums
########################################################################################################################
# Start with your program from 8-7
# Write a while loop that allows users to enter an album's artist and title
# Once created, call the make_album() with the user's input and print the dictionary that's created
# Be sure to include a quite value
########################################################################################################################

def make_album(artist_name, album_title, song_numbers=None):
    """Return a dictionary about a music album."""
    album = {'artist': artist_name, 'album': album_title}
    if song_numbers:
        album['songs'] = song_numbers
    return album

while True:
    print("\nPlease tell me about an album:")
    print("Enter 'q' at anytime to exit")

    an_artist = input("Artist name: ")
    if an_artist == 'q':
        break

    an_album = input("Album name: ")
    if an_album == 'q':
        break

    album_info = make_album(an_artist, an_album)
    print(f"\n{album_info}")