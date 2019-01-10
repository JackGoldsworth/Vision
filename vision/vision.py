from command import CommandParser
from desktop_handler import DesktopHandler
from speech_handler import SpeechHandler
from spotify_handler import SpotifyHandler


class Vision:

    online = False
    text_mode = False
    debug_mode = False
    spot_handler = SpotifyHandler()
    desktop_handler = DesktopHandler("Programs")
    speech_handler = SpeechHandler(desktop_handler)
    command_parser = CommandParser()

    def start(self):
        self.online = True
        self.spot_handler.start(self)
        self.command_parser.get_command_file("commands.json")
        self.speech_handler.listen(self)

    def stop(self):
        self.online = False


if __name__ == "__main__":
    Vision().start()
