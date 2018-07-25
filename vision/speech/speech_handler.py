import os
from pocketsphinx import LiveSpeech, get_model_path


class SpeechHandler:

    speech = None
    model_path = get_model_path()

    def setup(self):
        self.speech = LiveSpeech(
            verbose=False,
            sampling_rate=16000,
            buffer_size=2048,
            no_search=False,
            full_utt=False,
            hmm=os.path.join(self.model_path, 'en-us'),
            lm=os.path.join(self.model_path, 'en-us.lm.bin'),
            dic=os.path.join(self.model_path, 'cmudict-en-us.dict')
        )
        for phrase in self.speech:
            print(phrase.hypothesis())
