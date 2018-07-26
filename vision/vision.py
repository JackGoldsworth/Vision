from spotify import SpotifyHandler
from speech import SpeechHandler


class Vision:

    online = False
    spot_handler = SpotifyHandler()
    speech_handler = SpeechHandler()

    def start(self):
        self.online = True
        self.spot_handler.start()
        self.speech_handler.setup()
        self.speech_handler.listen(self)
        # self.spot_handler.play_specific_artist_song("Weekend", "Mac Miller")

    def stop(self):
        self.online = False

    def get_spotify_handler(self):
        return self.spot_handler

    def get_speech_handler(self):
        return self.speech_handler


if __name__ == "__main__":
    Vision().start()
