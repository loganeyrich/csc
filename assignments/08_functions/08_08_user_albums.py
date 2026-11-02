'''
Logan Eyrich
Chapter 8
Difficulty: 6/10
'''

def make_album(artist_name, album_title, number_of_songs=None):
    """Build a dictionary containing information about an album."""
    album = {
        'artist': artist_name,
        'title': album_title
    }
    if number_of_songs is not None:
        album['Songs'] = number_of_songs
    return album
while True:
    artist_name = input("Enter an artist's name (or 'quit' to stop): ")
    if artist_name.lower() == 'quit':
        break

    album_title = input("Enter an album title (or 'quit' to stop): ")
    if album_title.lower() == 'quit':
        break

    print(make_album(artist_name, album_title))