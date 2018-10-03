import speech_recognition as sr


class SpeechHandler:

    speech = None
    mic = None
    desktop_handler = None
    index = 0

    def __init__(self, desktop_handler):
        self.speech = sr.Recognizer()
        self.mic = sr.Microphone()
        self.desktop_handler = desktop_handler

    def listen(self, vision):
        """
        Either prompts you to enter commands
        or listens to your voice or commands.

        :param vision: The core vision class
        """
        if vision.text_mode:
            while vision.online and vision.text_mode:
                command = input("Enter a command\n")
                command = str(command).split()
                if command[0].lower() == "vision" and len(command) > 1:
                    self.handle_commands(command, vision)
        while vision.online and not vision.text_mode:
            try:
                with self.mic as source:
                    print("Listening")
                    audio = self.speech.listen(source, phrase_time_limit=10)
                    google = self.speech.recognize_google(audio)
                    google_str = str(google).split()
                    if google_str[0].lower() == "vision":
                        self.handle_commands(google_str, vision)
            except sr.UnknownValueError:
                pass

    def handle_commands(self, words, vision):
        """
        Handles the parsing of commands from the commands.json.

        :param words: The words typed or spoke from listen().
        :param vision: The core vision class.
        """
        if words[1] is None:
            return
        commands = vision.command_parser.commands
        parser = commands["parser"]
        for i, command in enumerate(commands, 0):
            command_str = str(command_str).split()
            for j in len(command_str):
                if words[j] == command_str[j]:
                    return  # Finish Later




    @staticmethod
    def get_all_words_until(sentence, words):
        """
        Gets all the words until certain other words.

        :param sentence: The split list of words from listen()
        :param words: Words to stop at, '?' means the end of the sentence.
        """
        sentence.pop(0)
        sentence.pop(0)
        word_dict = dict()
        index = 0
        for i, w in enumerate(words):
            if w != "?":
                index = sentence.index(words[i])
                word_dict[i] = sentence[:index]
            else:
                if len(words) == 1:
                    word_dict[i] = sentence[index:]
                else:
                    word_dict[i] = sentence[index + 1:]
        return word_dict

    # def handle_commands(self, words, vision):
    #     if words[1] is None:
    #         return
    #     command = words[1]
    #     spot = vision.get_spotify_handler()
    #     if command == "play":
    #         if "by" in words:
    #             self.index = 0
    #             final = self.get_all_words_until(words, ["by", "?"])
    #             spot.play_specific_artist_song(" ".join(final[0]), " ".join(final[1]))
    #         else:
    #             self.index = 0
    #             spot.play_specific_song(self.get_all_words_until(words, "?"))
    #     elif command == "stop" or command == "close" and len(words) == 2:
    #         vision.online = False
    #     elif command == "open":
    #         self.desktop_handler.open_program(words[2])
    #     elif command == "close" and len(words) == 3:
    #         self.desktop_handler.close_program(words[2])
    #     elif command == "text" and len(words) > 2:
    #         option = words[2].lower()
    #         if option == "on":
    #             vision.text_mode = True
    #         elif option == "off":
    #             vision.text_mode = False
    #     elif command == "login" and len(words) > 2:
    #         program_login = words[2].lower()
    #         if program_login == "spotify":
    #             vision.get_spotify_handler().start()