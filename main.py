import requests

def request(offset):
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer BQBW7LUO3UZflGIuukeh0zrUdPvOTGfToemyXV8ep5j4w6XaBAEusedeFpx65V22SsBLUeAKeYbRzMfZn6VnXoCDgUMRiz4Xms6d725V0K0hD-bXZhveu901zqG9CgHEEPD8I2utyl-20bDCwsEwgeW1Kr_gDEMahpeEeqMCtayZugT1C-JiIUu4LA1V1-syXg',
    }

    params = {
        'offset': f'{offset}',
    }

    response = requests.get('https://api.spotify.com/v1/playlists/6PtI8T8ZBWE4fn4jIPtIyr/tracks', params=params, headers=headers)

    return response.json()

items = request(0)['items']

songs = []

for song in items:
    songs.append(song['track']['name'])
    print(song['track']['name'])

print(len(songs))
