class StringUtil:

    @staticmethod
    def get_all_words_until(sentence, words, indices_popped=2):
        """
        Gets all the words until certain other words.

        :param sentence: The split list of words from listen()
        :param words: Words to stop at, '?' means the end of the sentence.
        :param indices_popped: How many words should you pop from the stack.
        """
        for i in range(indices_popped):
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

    @staticmethod
    def ccs(string1, string2):
        """
        Compare case sensitive strings.
        :param string1: First string
        :param string2: Second string
        :return: True or false if equal
        """
        if string1.lower() == string2.lower():
            return True
        else:
            return False
