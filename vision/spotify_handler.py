import os

import spotipy
import spotipy.util as util

from string_util import StringUtil


class SpotifyHandler:

    token = None
    sp = None
    deviceID = None
    vision = None
    scope = 'user-library-read user-read-currently-playing user-modify-playback-state user-read-playback-state'

    def start(self, vision):
        """
        Starts the Spotify api and makes sure
        that there is a device to append to.
        """
        self.vision = vision
        print("Please enter your Spotify username: ")
        username = input()
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
        """
        Prints a list of the users saved tracks.
        """
        results = self.sp.current_user_saved_tracks()
        for item in results['items']:
            print(item)
            track = item['track']
            print(track['name'] + ' - ' + track['artists'][0]['name'])

    def play_next_song(self):
        """
        Plays the next queue'd song.
        """
        self.sp.next_track(self.deviceID)

    def play_specific_song(self, name):
        """
        Plays a specific song by song name.

        :param name: The track name
        """
        search = self.sp.search(name)
        items = [search["tracks"]["items"][0]["uri"]]
        if search["tracks"]["items"][0]["explicit"] is self.vision.settings_handler.get_setting("Spotify",
                                                                                                "explicit_songs"):
            self.sp.start_playback(self.deviceID, None, items)

    def play_specific_artist_song(self, name, artist_name):
        """
        Plays a specific song based on artist and song name.

        :param name: Song name.
        :param artist_name: Singer/Band name.
        """
        search = self.sp.search(str(name).lower(), type='track')
        if self.vision.settings_handler.get_setting("Vision", "debug"):
            print(search)
        items = search["tracks"]["items"]
        for i, item in enumerate(items):
            artist = item["artists"]
            name = artist[0]["name"]
            if StringUtil.ccs(name, artist_name):
                items = [search["tracks"]["items"][i]["uri"]]
                if search["tracks"]["items"][i]["explicit"] is self.vision.settings_handler.get_setting("Spotify",
                                                                                                        "explicit_songs"):
                    self.sp.start_playback(self.deviceID, None, items)
                    break

    def play_specific_artist_album(self, name, artist_name):
        """
        Plays a specific album based on artist and album name.

        :param name: Album name
        :param artist_name: Singer/Band name.
        """
        search = self.sp.search(str(name).lower(), type='album')
        if self.vision.settings_handler.get_setting("Vision", "debug"):
            print(search)
        items = search["albums"]["items"]
        for i, item in enumerate(items):
            artist = item["artists"]
            name = artist[0]["name"]
            if StringUtil.ccs(name, artist_name) and search["albums"]["items"][i]["album_type"] == "album":
                # Checking song profanity
                items = search["albums"]["items"][i]["uri"]
                tracks = self.sp.album_tracks(items, 1)
                if tracks["items"][0]["explicit"] is self.vision.settings_handler.get_setting("Spotify",
                                                                                              "explicit_songs"):
                    self.sp.start_playback(self.deviceID, items)
                    break

    def pause_song(self):
        self.sp.pause_playback()

    def resume_song(self):
        self.sp.start_playback()

    def previous_song(self):
        self.sp.previous_track()

    def change_spotify_volume(self, percent):
        self.sp.volume(percent)
