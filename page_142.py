# print("Hi, Igor")
#
# def make_album(name, album, songs = None):
#     """return a dictionary of music"""
#     album = {'artist_name': name, 'album_name': album}
#     if songs:
#         album['songs'] = songs
#     return album
#
# album_1 = make_album('Bee Gees', 'Staying Alive')
# album_2 = make_album('Beetles', 'Strawberry Fields')
# album_3 = make_album('Baccara', 'I Can Boogie', 12)
#
# print('\n', album_1, '\n', album_2, '\n', album_3)


def make_album(name, album, songs = None):
    """return a dictionary of music"""
    album = {'artist_name': name, 'album_name': album}
    if songs:
        album['songs'] = songs
    return album

while True:
    print('provide inputs, pls: ')
    print("(enter 'q' to quit")
    artist_name = input("name: ")
    if artist_name =='q':
        break
    album_name = input("album: ")
    if album_name =='q':
        break
    new_album = make_album(artist_name, album_name)
    print(f"{new_album}")

# album_1 = make_album('Bee Gees', 'Staying Alive')
# album_2 = make_album('Beetles', 'Strawberry Fields')
# album_3 = make_album('Baccara', 'I Can Boogie', 12)
# print('\n', album_1, '\n', album_2, '\n', album_3)

