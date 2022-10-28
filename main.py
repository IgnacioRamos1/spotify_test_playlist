import requests
from authorization import authorize

client_id = '86df2104482c438d89e25692b2dffc95'
client_secret = '2f2be1289a9d4287aa15f6b223bdd888'

scope = "playlist-read-private playlist-read-collaborative playlist-modify-private playlist-modify-public user-library-modify user-library-read ugc-image-upload user-read-playback-state user-modify-playback-state user-read-currently-playing app-remote-control streaming user-follow-modify user-follow-read user-read-playback-position user-top-read user-read-recently-played user-read-email user-read-private"

main_playlist_id = "6PtI8T8ZBWE4fn4jIPtIyr"
test_playlist_id = "056NsgfUH3ebxMUoT3sNPw"

spotify = authorize(scope, client_id, client_secret)
bearer = spotify._auth


def request_playlist_items(offset, bearer, playlist_id):
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {bearer}',
    }

    params = {
        'offset': f'{offset}',
    }

    response = requests.get(f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks',
                            params=params,
                            headers=headers
                            )

    return response.json()


def get_songs(bearer, playlist_id):
    songs = []
    song = {}
    for i in range(0, 10000, 100):
        items = request_playlist_items(i, bearer, playlist_id)['items']
        for item in items:
            if items != []:
                song['name'] = item['track']['name']
                song['id'] = item['track']['id']
                song['uri'] = item['track']['uri']
                songs.append(song.copy())
            else:
                break
    return songs


def check_for_duplicates(main_playlist_id, test_playlist_id, bearer):
    main_playlist_songs = get_songs(bearer, main_playlist_id)
    test_playlist_songs = get_songs(bearer, test_playlist_id)

    duplicates = []
    duplicate_song = {}

    for main_song in main_playlist_songs:
        for test_song in test_playlist_songs:
            if main_song['id'] == test_song['id']:
                duplicate_song['name'] = test_song['name']
                duplicate_song['id'] = test_song['id']
                duplicate_song['uri'] = test_song['uri']
                duplicates.append(duplicate_song.copy())

    return duplicates

def remove_duplicates(main_playlist_id, test_playlist_id, bearer):
    duplicates = check_for_duplicates(main_playlist_id, test_playlist_id, bearer)
    for duplicate in duplicates:
        spotify.playlist_remove_all_occurrences_of_items(test_playlist_id, [duplicate['uri']])
        print(f"Removed {duplicate['name']}")

print(remove_duplicates(main_playlist_id, test_playlist_id, bearer))
