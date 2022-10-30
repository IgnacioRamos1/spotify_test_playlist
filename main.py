from authorization import authorize

client_id = '86df2104482c438d89e25692b2dffc95'
client_secret = '2f2be1289a9d4287aa15f6b223bdd888'

scope = "playlist-read-private playlist-read-collaborative playlist-modify-private playlist-modify-public user-library-modify user-library-read ugc-image-upload user-read-playback-state user-modify-playback-state user-read-currently-playing app-remote-control streaming user-follow-modify user-follow-read user-read-playback-position user-top-read user-read-recently-played user-read-email user-read-private"

main_playlist_id = "6PtI8T8ZBWE4fn4jIPtIyr"
test_playlist_id = "056NsgfUH3ebxMUoT3sNPw"

spotify = authorize(scope, client_id, client_secret)


def request_playlist_tracks(playlist_id, offset):
    playlist_items = spotify.playlist_items(
                                            playlist_id,
                                            limit=100,
                                            offset=offset
                                            )
    return playlist_items


def get_songs(playlist_id):
    songs = {}

    for i in range(0, 10000, 100):
        items = request_playlist_tracks(playlist_id, i)['items']
        if items != []:
            for item in items:
                songs[item['track']['id']] = {
                                                "id": item['track']['id'],
                                                "name": item['track']['name'],
                                                "uri": item['track']['uri']
                                                }
        else:
            break
    return songs


def check_for_duplicates(main_playlist_id, test_playlist_id):
    main_playlist_songs = get_songs(main_playlist_id)
    test_playlist_songs = get_songs(test_playlist_id)

    main_song_id = []
    test_song_id = []
    duplicates = []

    for info in main_playlist_songs.values():
        main_song_id.append(info['id'])

    for info in test_playlist_songs.values():
        test_song_id.append(info['id'])

    main_song_id.sort()
    test_song_id.sort()

    i = 0
    j = 0

    if len(main_song_id) > len(test_song_id):
        while (j <= len(test_song_id) - 1):
            if main_song_id[i] < test_song_id[j]:
                i += 1
            elif main_song_id[i] > test_song_id[j]:
                j += 1
            else:
                duplicates.append(test_playlist_songs[test_song_id[j]])
                i += 1
    else:
        while (i <= len(main_song_id) - 1):
            if main_song_id[i] < test_song_id[j]:
                i += 1
            elif main_song_id[i] > test_song_id[j]:
                j += 1
            else:
                duplicates.append(test_playlist_songs[test_song_id[j]])
                i += 1

    return duplicates


def remove_duplicates(main_playlist_id, test_playlist_id):
    duplicates = check_for_duplicates(main_playlist_id, test_playlist_id)
    for duplicate in duplicates:
        spotify.playlist_remove_all_occurrences_of_items(test_playlist_id, [duplicate['uri']])
        print(f"Removed {duplicate['name']}")


if __name__ == "__main__":
    remove_duplicates(main_playlist_id, test_playlist_id)
