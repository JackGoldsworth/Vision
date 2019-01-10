import speech_recognition as sr

from command.command_handler import CommandHandler


class SpeechHandler:

    speech = None
    mic = None
    command_handler = None

    def __init__(self, desktop_handler):
        self.speech = sr.Recognizer()
        self.mic = sr.Microphone()
        self.command_handler = CommandHandler(desktop_handler)

    def listen(self, vision):
        """
        Either prompts you to enter commands
        or listens to your voice or commands.

        :param vision: The core vision class
        """
        if vision.settings_handler.get_setting("Vision", "text_mode"):
            while vision.online and vision.settings_handler.get_setting("Vision", "text_mode"):
                command = input("Enter a command\n")
                command = str(command).split()
                if command[0].lower() == "vision" and len(command) > 1:
                    self.handle_commands(command, vision)
        while vision.online and not vision.settings_handler.get_setting("Vision", "text_mode"):
            try:
                with self.mic as source:
                    print("Listening")
                    audio = self.speech.listen(source, phrase_time_limit=5)
                    google = self.speech.recognize_google(audio)
                    google_str = str(google).split()
                    if google_str[0].lower() == "vision":
                        if vision.settings_handler.get_setting("Vision", "debug") is True:
                            print(google_str)
                        self.handle_commands(google_str, vision)
            except sr.UnknownValueError:
                pass

    def handle_commands(self, words, vision):
        """
        Handles which type of commands to use.

        :param words: The words typed or spoke from listen().
        :param vision: The core vision class.
        """
        try:
            words[1]
        except IndexError:
            return None
        command = words[1].lower()
        # Play Spotify Song or album
        if command == "play":
            self.command_handler.play_spotify(words, vision)
        # List commands
        elif command == "list" and len(words) > 2:
            self.command_handler.list_commands(words, vision)
        # Close Vision
        elif command == "close" and len(words) == 2:
            vision.stop()
        # Open Program
        elif command == "open":
            self.command_handler.open_program(words)
        # Close program
        elif command == "close" and len(words) == 3:
            self.command_handler.close_program(words)
        # Text Mode
        elif command == "text" and len(words) > 2:
            self.command_handler.text_mode(words, vision)
        # Program login
        elif command == "login" and len(words) > 2:
            self.command_handler.program_login(words, vision)
        # Play Next Spotify Song
        elif command == "next" and len(words) > 2:
            self.command_handler.next_song(words, vision)
        # Enter debug mode
        elif command == "debug" and len(words) > 2:
            self.command_handler.change_debug(words, vision)
        # Turns off the profanity filter
        # TODO: Volume, pause and resume song
        elif command == "profanity" and len(words) > 2:
            self.command_handler.change_profanity(words, vision)
