from command import CommandParser
from desktop_handler import DesktopHandler
from speech_handler import SpeechHandler
from spotify_handler import SpotifyHandler


class Vision:

    online = False
    text_mode = True
    spot_handler = SpotifyHandler()
    desktop_handler = DesktopHandler("Programs")
    speech_handler = SpeechHandler(desktop_handler)
    command_parser = CommandParser()

    def start(self):
        self.online = True
        self.command_parser.get_command_file("commands.json")
        self.command_parser.list_commands()
        self.speech_handler.listen(self)

    def stop(self):
        self.online = False


if __name__ == "__main__":
    Vision().start()
