import requests


def request(offset, bearer):
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {bearer}',
    }

    params = {
        'offset': f'{offset}',
    }

    response = requests.get('https://api.spotify.com/v1/playlists/6PtI8T8ZBWE4fn4jIPtIyr/tracks', params=params, headers=headers)

    return response.json()


bearer = "BQBD_e4JRQWSQWDxDdvnrgzuyknwtIjuYrobLh5L4Qc7l72Ewzvn2-Q56yuxO2Q4ELMdGoJoQzJJHYG-HnwMjQmozqH2btvlHxoAKzh833LhmL0TO_fEhdB5h40msHTDRi1zIbLZJobskwoF-C40bTa9P7woIjOSqHPFmTkg1fxGQdymFHO8oi0NCtEA_FFdkmFvp8nny6al6mZT2ii5JxLaNQJi_9E"

for i in range(0, 10000, 100):
    items = request(i, bearer=bearer)['items']
    songs = []

    if len(songs) == 100:
        break
    else:
        for song in items:
            songs.append(song['track']['name'])
            print(song['track']['name'])

