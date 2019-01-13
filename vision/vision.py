from command import CommandParser
from handlers.desktop_handler import DesktopHandler
from handlers.search_handler import SearchHandler
from handlers.speech_handler import SpeechHandler
from handlers.spotify_handler import SpotifyHandler
from settings.settings_handler import SettingsHandler


class Vision:
    online = False
    spot_handler = SpotifyHandler()
    desktop_handler = DesktopHandler("Programs")
    speech_handler = SpeechHandler(desktop_handler)
    command_parser = CommandParser()
    settings_handler = SettingsHandler()
    search_handler = SearchHandler()

    def start(self):
        self.online = True
        self.settings_handler.load_settings("settings.json")
        self.command_parser.get_command_file("commands.json")
        self.speech_handler.listen(self)

    def stop(self):
        print("Vision shutting down...")
        self.settings_handler.save_settings()
        self.online = False


if __name__ == "__main__":
    Vision().start()
