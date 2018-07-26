from spotify import SpotifyHandler
from speech import SpeechHandler


class Vision:
    online = False
    spot_handler = SpotifyHandler()
    speech_handler = SpeechHandler()

    def start(self):
        self.online = True
        self.spot_handler.start()
        self.spot_handler.get_saved_tracks()
        self.spot_handler.play_specific_song("Over Now")

    def stop(self):
        self.online = False


if __name__ == "__main__":
    Vision().start()
