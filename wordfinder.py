import random


class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    # init

    def __init__(self, filepath):
        """ Construct word finder with input of file. Prints words read """
        self.filepath = filepath
        self.words = []
        self.get_words(self.get_lines())
        print(f"{self.count_words()} words read")

    def __repr__(self):
        return f"<Word file's file is {self.filepath}>"

    def getLines(self):
        """Open the file passed in. Return a list of lines that are not empty"""
        file = open(self.filepath)
        #TODO: readlines()
        readText = file.read().splitlines()
        textNoEmptyLine = [line for line in readText if line != ""]
        text.close()
        return textNoEmptyLine

    def getWords(self, listLines):
        """Input a list of lines and return a list of words"""
        for line in listLines:
            listOfWords = line.split(" ")
            self.words.extend(listOfWords)

    def countWords(self):
        """Return the number of words in list"""
        return len(self.words)

    def random(self):
        """Call choice from "random" library. Return a word from list of words"""
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """Special Word Finder: Reads files and ignore comment lines"""

    # def __init__(self, file):
    # """Create a special word finder with an input of file and disregards any empty or comment lines"""
    # self.file = file
    # self.words = []
    # self.getWords(self.filterList(self.getLines()))
    # print(f"{self.countWords()} words read")

    def getLines(self, lines):
        return [line for line in lines if line[0] != "#"]


# original findWords
    # def findWords(self):
    #     words = []
    #     text = open(self.file)
    #     for line in text:
    #         print(line, "line")
    #         withoutNewLine = line.split()
    #         for word in withoutNewLine:
    #             words.append(word)
    #     return words
