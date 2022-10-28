import spotipy
import spotipy.util as util

client_id = '86df2104482c438d89e25692b2dffc95'
client_secret = '2f2be1289a9d4287aa15f6b223bdd888'

scope = "playlist-read-private playlist-read-collaborative playlist-modify-private playlist-modify-public user-library-modify user-library-read"


def authorize(scope, client_id, client_secret):
    token = util.prompt_for_user_token('USERNAME_TO_AUTHORIZE',
                                        scope,
                                        client_id=client_id,
                                        client_secret=client_secret,
                                        redirect_uri='http://localhost/'
                                        )

    spotify = spotipy.Spotify(auth=token)
    return spotify
