import speech_recognition as sr


class SpeechHandler:

    speech = None
    mic = None
    index = 0

    def __init__(self):
        self.speech = sr.Recognizer()
        self.mic = sr.Microphone()

    def listen(self, vision):
        while vision.online:
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
        if words[1] is None:
            return
        command = words[1]
        spot = vision.get_spotify_handler()
        if command == "play":
            if words.__contains__("by"):
                self.index = 0
                spot.play_specific_artist_song(self.get_all_words_until(words, "by"),
                                               self.get_all_words_until(words, "end"))
            else:
                self.index = 0
                spot.play_specific_song(self.get_all_words_until(words, "end"))
        elif command == "stop":
            vision.online = False

    def get_all_words_until(self, sentence, word):
        index = self.index
        words = list()
        print(sentence)
        sentence.pop(0)
        sentence.pop(0)
        print(sentence)
        if word != "end":
            for i, w in enumerate(sentence):
                if w != (word or "vision"):
                    words.insert(i, w)
                else:
                    index = i
                    break
            self.index = index
            print(" ".join(words))
            return" ".join(words)
        else:
            if "by" in sentence:
                print(" ".join(sentence[index + 1:]))
                return " ".join(sentence[index + 1:])
            else:
                print(" ".join(sentence))
                return " ".join(sentence)
