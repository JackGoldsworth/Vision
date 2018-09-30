import speech_recognition as sr


class SpeechHandler:

    speech = None
    mic = None
    desktop_handler = None

    def __init__(self, desktop_handler):
        self.speech = sr.Recognizer()
        self.mic = sr.Microphone()
        self.desktop_handler = desktop_handler

    def listen(self, vision):
        if vision.text_mode:
            while vision.online:
                command = input("Enter a command\n")
                command = str(command).split()
                if command[0].lower() == "vision" and command[1] is not None:
                    self.handle_commands(command, vision)
        while vision.online and not vision.text_mode:
            try:
                with self.mic as source:
                    print("Listening")
                    audio = self.speech.listen(source, phrase_time_limit=10)
                    google = self.speech.recognize_google(audio)
                    google_str = str(google).split()
                    if google_str[0].lower() == "vision":
                        print(google_str)
                        self.handle_commands(google_str, vision)
            except sr.UnknownValueError:
                pass

    def handle_commands(self, words, vision):
        if words[1] is None:
            return
        command = words[1]
        spot = vision.get_spotify_handler()
        if command == "play":
            if "by" in words:
                final = self.get_all_words_until(words, ["by", "?"])
                song = " ".join(final[0])
                artist = " ".join(final[1])
                spot.play_specific_artist_song(song, artist)
                print(song, artist)
            else:
                spot.play_specific_song(self.get_all_words_until(words, "end"))
        elif command == "stop" or command == "close":
            vision.online = False
        elif command == "open":
            self.desktop_handler.open_program(words[2])
        elif command == "close" and words[2] is not None:
            self.desktop_handler.close_program(words[2])
        elif command == "text" and words[2] is not None:
            option = words[2].lower()
            if option == "true":
                vision.text_mode = True
            elif option == "false":
                vision.text_mode = False

    @staticmethod
    def get_all_words_until(sentence, words):
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
