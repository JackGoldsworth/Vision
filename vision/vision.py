from spotify import SpotifyHandler
from speech import SpeechHandler


class Vision:
    online = False
    spot_handler = SpotifyHandler()
    speech_handler = SpeechHandler()

    def start(self):
        self.online = True
        self.spot_handler.start()
        self.spot_handler.play_specific_song("Why")
        #self.speech_handler.setup()

    def stop(self):
        self.online = False


if __name__ == "__main__":
    Vision().start()
