from utils import SpotifyHandler, SpeechHandler, DesktopHandler


class Vision:

    online = False
    text_mode = True
    spot_handler = SpotifyHandler()
    desktop_handler = DesktopHandler("Programs")
    speech_handler = SpeechHandler(desktop_handler)

    def start(self):
        self.online = True
        self.speech_handler.listen(self)

    def stop(self):
        self.online = False

    def get_spotify_handler(self):
        return self.spot_handler

    def get_speech_handler(self):
        return self.speech_handler

    def get_desktop_handler(self):
        return self.desktop_handler


if __name__ == "__main__":
    Vision().start()
