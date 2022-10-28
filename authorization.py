import spotipy
import spotipy.util as util

def authorize(scope, client_id, client_secret):
    token = util.prompt_for_user_token('nacho',
                                        scope,
                                        client_id=client_id,
                                        client_secret=client_secret,
                                        redirect_uri='http://localhost:8080'
                                        )

    spotify = spotipy.Spotify(auth=token)
    return spotify
