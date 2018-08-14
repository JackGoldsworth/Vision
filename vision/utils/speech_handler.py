import speech_recognition as sr


class SpeechHandler:

    speech = None
    mic = None

    def __init__(self):
        self.speech = sr.Recognizer()
        self.mic = sr.Microphone()

    def listen(self, vision):
        while vision.online:
            try:
                with self.mic as source:
                    print("Listening")
                    audio = self.speech.listen(source, phrase_time_limit=10)
                    sphinx = self.speech.recognize_sphinx(audio)
                    sphinx_str = str(sphinx).partition(" ")
                    print(sphinx)
                    if sphinx_str[0] == "play":
                        vision.get_spotify_handler().play_specific_artist_song("Weekend", "Mac Miller")
                        print(sphinx)
            except sr.UnknownValueError:
                pass
