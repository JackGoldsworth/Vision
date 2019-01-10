from string_util import StringUtil


class CommandHandler:
    desktop_handler = None

    def __init__(self, desktop_handler):
        self.desktop_handler = desktop_handler

    def change_spotify_volume(self, words, vision):
        if StringUtil.ccs(words[3], "zero"):
            percent = 0
        else:
            percent = int(words[3])
        vision.spot_handler.change_spotify_volume(percent)

    def next_song(self, words, vision):
        if words[2].lower() == "song":
            vision.spot_handler.play_next_song()

    def pause_song(self, words, vision):
        if words[2].lower() == "song":
            vision.spot_handler.pause_song()

    def resume_song(self, words, vision):
        if words[2].lower() == "song":
            vision.spot_handler.resume_song()

    def previous_song(self, words, vision):
        if words[2].lower() == "song":
            vision.spot_handler.previous_song()

    def play_spotify(self, words, vision):
        spot = vision.spot_handler
        if words[2].lower() == "album":
            if "by" in words:
                final = StringUtil.get_all_words_until(words, ["by", "?"], 3)
                spot.play_specific_artist_album(" ".join(final[0]), " ".join(final[1]))
        else:
            if "by" in words:
                final = StringUtil.get_all_words_until(words, ["by", "?"])
                spot.play_specific_artist_song(" ".join(final[0]), " ".join(final[1]))
            else:
                spot.play_specific_song(StringUtil.get_all_words_until(words, "?"))

    def close_program(self, words):
        self.desktop_handler.close_program(words[2])

    def open_program(self, words):
        self.desktop_handler.open_program(words[2])

    def program_login(self, words, vision):
        program_login = words[2].lower()
        if program_login == "spotify":
            vision.spot_handler.start(vision)

    def text_mode(self, words, vision):
        option = words[2].lower()
        if option == "on":
            vision.settings_handler.change_settings("Vision", "text_mode", True)
        elif option == "off":
            vision.settings_handler.change_settings("Vision", "text_mode", False)

    def change_profanity(self, words, vision):
        if words[2].lower() == "on":
            vision.settings_handler.change_settings("Spotify", "explicit_songs", True)
        elif words[2].lower() == "off":
            vision.settings_handler.change_settings("Spotify", "explicit_songs", False)

    def change_debug(self, words, vision):
        if words[2].lower() == "on":
            vision.settings_handler.change_settings("Vision", "debug", True)
        elif words[2].lower() == "off":
            vision.settings_handler.change_settings("Vision", "debug", False)

    def list_commands(self, words, vision):
        option = words[2]
        if option == "commands":
            vision.command_parser.list_commands()
