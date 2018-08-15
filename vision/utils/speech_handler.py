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
                    print(google)
                    self.handle_commands(google_str, vision)
                    print(google)
            except sr.UnknownValueError:
                pass

    def handle_commands(self, words, vision):
        command = words[0]
        if command == "play":
            vision.get_spotify_handler().play_specific_artist_song(self.get_all_words_until(words, "by"),
                                                                   self.get_all_words_until(words, "end"))

    def get_all_words_until(self, sentence, word):
        index = self.index
        words = list()
        if word != "end":
            for i, w in enumerate(sentence):
                if w != word:
                    words.insert(i, w)
                else:
                    index = i
                    break
            self.index = index
            print(" ".join(words[1:]))
            return " ".join(words[1:])
        else:
            print(" ".join(sentence[index + 1:]))
            return " ".join(sentence[index + 1:])
