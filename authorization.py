import spotipy
import spotipy.util as util

client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'

scope = "playlist-read-private playlist-read-collaborative playlist-modify-private playlist-modify-public user-library-modify user-library-read ugc-image-upload user-read-playback-state user-modify-playback-state user-read-currently-playing app-remote-control streaming user-follow-modify user-follow-read user-read-playback-position user-top-read user-read-recently-played user-read-email user-read-private"


def authorize():
    token = util.prompt_for_user_token('YOUR_USERNAME',
                                       scope,
                                       client_id=client_id,
                                       client_secret=client_secret,
                                       redirect_uri='http://localhost:8080'
                                       )

    spotify = spotipy.Spotify(auth=token)
    return spotify
