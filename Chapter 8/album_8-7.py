# Try It Yourself Exercise - Pg.142
# 8-7 Album
########################################################################################################################
# Write a function called make_album() that builds a dictionary describing a music album
# Should take in an artist name, and album title
# Should return a dictionary containing these two pieces of information
# Make 3 dictionaries representing different albums
# Print each return value to show that the dictionaries are storing the album information correctly
# Use None as an optional parameter to that allows you to store the number of songs on an album
########################################################################################################################

def make_album(artist_name, album_title, song_numbers=None):
    """Return a dictionary about a music album."""
    album = {'artist': artist_name, 'album': album_title}
    if song_numbers:
        album['songs'] = song_numbers
    return album

blink = make_album('blink-182', 'Enema of the State', 12)
print(blink)

stirling = make_album('Lindsey Stirling', 'Artemis', song_numbers=13)
print(stirling)

blackmill = make_album(album_title='Miracle', artist_name='Blackmill', song_numbers=11)
print(blackmill)