import spotipy
import spotipy.util as util


class SpotifyHandler:

    token = None
    scope = 'user-library-read'

    def start(self):
        username = input("Please enter your spotify username")
        self.token = util.prompt_for_user_token(username, self.scope)
        if self.token:
            sp = spotipy.Spotify(auth=self.token)
            results = sp.current_user_saved_tracks()
            for item in results['items']:
                track = item['track']
                print(track['name'] + ' - ' + track['artists'][0]['name'])
        else:
            print("Can't get token for", username)
