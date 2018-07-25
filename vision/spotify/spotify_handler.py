import spotipy
import spotipy.util as util
import os


class SpotifyHandler:

    token = None
    sp = None
    deviceID = None
    scope = 'user-library-read user-read-currently-playing user-modify-playback-state user-read-playback-state'

    def start(self):
        username = input("Please enter your spotify username ")
        try:
            self.token = util.prompt_for_user_token(username, self.scope)
        except AttributeError:
            os.remove(f".cache-{username}")

        if self.token:
            self.sp = spotipy.Spotify(auth=self.token)
            self.deviceID = self.sp.devices()["devices"][0]["id"]
        else:
            print("Can't get token for", username)

    def get_saved_tracks(self):
        results = self.sp.current_user_saved_tracks()
        for item in results['items']:
            track = item['track']
            print(track['name'] + ' - ' + track['artists'][0]['name'])

    def play_next_song(self):
        self.sp.next_track(self.deviceID)

    def play_specific_song(self, uri):
        album = self.sp.artist_albums("246dkjvS1zLTtiykXe5h60")["items"]
        for item in album:
            print("AlBUM: " + item["name"])


#track = self.sp.track("61jnrkPHpLumBf1kqGpRRt")
#print(track)
#self.sp.start_playback(self.deviceID, None, [track])

