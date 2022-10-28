import requests

bearer = "BQBHUXcLHBo0f0KBrQHNeUZwvKnrKlwwh5rfgLooJ6UJYVYkR53MW5MAE-MlbaX3EJgkiwnHvoKJQ17spJCDtQ98KeyxycAFtoweQUKcTNXmqLLEKc21FGJFaz30tZZTCJj90SVU2No74eRrCK-nez35Y7FymAQ49ytF_dx271BAxwkfeg"
main_playlist_id = "6PtI8T8ZBWE4fn4jIPtIyr"
test_playlist_id = "056NsgfUH3ebxMUoT3sNPw"


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

# If they are, delete them from the test playlist


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
                duplicate_song['uri'] = test_song['track']['uri']
                duplicates.append(duplicate_song.copy())

    return duplicates


print(check_for_duplicates(main_playlist_id, test_playlist_id, bearer))
