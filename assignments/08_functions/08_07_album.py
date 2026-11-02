'''
Logan Eyrich
Chapter 8
Difficulty: 4/10
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
print(make_album('Kanye West', 'Graduation'))
print(make_album('Yeat', 'Up2Me'))
print(make_album('Young Thug', 'Slime Language 2', 23))