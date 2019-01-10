from command import CommandParser
from desktop_handler import DesktopHandler
from settings.settings_handler import SettingsHandler
from speech_handler import SpeechHandler
from spotify_handler import SpotifyHandler


class Vision:
    online = False
    spot_handler = SpotifyHandler()
    desktop_handler = DesktopHandler("Programs")
    speech_handler = SpeechHandler(desktop_handler)
    command_parser = CommandParser()
    settings_handler = SettingsHandler()

    def start(self):
        self.online = True
        self.settings_handler.load_settings("settings.json")
        self.command_parser.get_command_file("commands.json")
        self.speech_handler.listen(self)

    def stop(self):
        self.online = False
        self.settings_handler.save_settings()


if __name__ == "__main__":
    Vision().start()
