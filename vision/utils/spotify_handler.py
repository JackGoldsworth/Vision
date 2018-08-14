import os

import spotipy
import spotipy.util as util


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
            print(item)
            track = item['track']
            print(track['name'] + ' - ' + track['artists'][0]['name'])

    def play_next_song(self):
        self.sp.next_track(self.deviceID)

    def play_specific_song(self, name):
        search = self.sp.search(name)
        items = [search["tracks"]["items"][0]["uri"]]
        self.sp.start_playback(self.deviceID, None, items)

    def play_specific_artist_song(self, name, artist_name):
        search = self.sp.search(name)
        items = search["tracks"]["items"]
        for i, item in enumerate(items):
            artist = item["artists"]
            name = artist[0]["name"]
            if name == artist_name:
                items = [search["tracks"]["items"][i]["uri"]]
                self.sp.start_playback(self.deviceID, None, items)

