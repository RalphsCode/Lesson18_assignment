"""Word Finder: finds random words from a dictionary."""
from random import randint

class WordFinder:
    """Gets words from the passed in file,
    and puts those words in a list. 
    Prints out how many words were found in the list.
    Picks a random word from that list of words.
    
    Machine for finding random words from dictionary.
    
    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """

    def __init__(self, file):
        self.file = file
        self.words = []
        self.open_word_file() 
        self.output_str()

    def open_word_file(self):
        """Method to open the file contining the words, 
        and puts the words in a list"""
        with open(self.file, 'r') as word_file:
            for word in word_file:
                if not word.strip() or word[0] == '#':
                    pass
                else:
                    self.words.append(word.strip())

    def __repr__(self):
        """Shows a descriptive represetation of this class."""
        return (f'Class that gets the words from the file: ', {self.file}, ' and has a method to return a random word from the file.' )

    def output_str(self):
        """Prints out the number of words in the list of words"""
        print(len(self.words), 'words read')

    def random(self):
        """Returns one random word from the list of words"""
        random_word_location = randint(0, len(self.words)-1)
        output = self.words[random_word_location].strip()
        return output

# Developer tests:
# t = WordFinder('simple.txt')
# for x in range(5):
#     print(t.random())

class SpecialWordFinder(WordFinder):
    """function that accepts word files containing blank lines and '#' at start of line.
    Prints the number of words found in the file.
    
    >>> swf = SpecialWordFinder("simple.txt")
    3 words read

    >>> swf.random() in ["cat", "dog", "porcupine"]
    True

    >>> swf.random() in ["cat", "dog", "porcupine"]
    True

    >>> swf.random() in ["cat", "dog", "porcupine"]
    True
    """
    def __init__(self, file):
        super().__init__(file)

    def __repr__(self):
        """function to better describe the function"""
        return f'Function to take a list of words from a file. Has a method to select a random word from the passed in file. Can accept a file with blank lines, and lines that start with "#" - both of which are ignored.'
    
# Developer tests:
# s = SpecialWordFinder('simple.txt')
# for x in range(5):
#     print(s.random())
# print(s)