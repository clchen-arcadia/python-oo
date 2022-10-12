import random

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, filepath):
        """ Construct word finder with input filepath. Prints words read """
        self.filepath = filepath
        self.words = []
        self.get_words(self.get_lines())
        print(f"{self.count_words()} words read")

    def __repr__(self):
        return f"<Word file's file is {self.filepath}>"

    def get_lines(self):
        """Open the file passed in. Return a list of lines that are not empty"""
        file = open(self.filepath)

        # NOTE some previously tested code. Deprecated
        # output_lines = []
        # for line_test in file:
        #     output_lines.append(line_test)

        lines = file.readlines()
        text_cleaned = [line[:-1] for line in lines if line[:-1] != ""]

        file.close()
        return text_cleaned

    def get_words(self, list_lines):
        """Input a list of lines and return a list of words"""
        for line in list_lines:
            words_list = line.split(" ")
            self.words.extend(words_list)

    def count_words(self):
        """Return the number of words in list"""
        return len(self.words)

    def random(self):
        """Return a random word from list of words"""
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """Special Word Finder: Reads files and ignore comment lines"""

    def __init__(self, filepath):
        """Create a special word finder with an input of file and disregards any empty or comment lines"""
        super().__init__(filepath)

    def get_lines(self):
        """Calls super method of the same name and filters and returns it"""
        parent_list = super().get_lines()
        return [line for line in parent_list if line[0] != "#"]




# original findWords Code, deprecated
#
    # def findWords(self):
    #     words = []
    #     text = open(self.file)
    #     for line in text:
    #         print(line, "line")
    #         withoutNewLine = line.split()
    #         for word in withoutNewLine:
    #             words.append(word)
    #     return words
