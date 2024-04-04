import random

class WordFinder:
    """Word Finder: finds random words from a dictionary.

    >>> wf = WordFinder("words.txt)
    235885 words read

    >>> wf.num_words
    235886

    >>> wf.random() in wf.words
    True
    
    """
    def __init__(self, file):
        """
        Initilize WordFinder object.

        Args:
            file (str) is the path to the file containing words
        """
        self.file = file
        self.words = self.read_words()
        self.num_words = len(self.words)
        print(f'{self.num_words} words read')

    def read_words(self):
        """
        Read words from the file

        Returns:
            List of words read from the file
        """
        with open(self.file, 'r') as f:
            return f.read().split()

    def random(self):
        """
        Get a random word from the list of words.

        Returns:
            str of a randomly selected word
        """
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """Finds random word from a dictionary excluding blank spaces and comments
    
    >>> sf = SpecialWordFinder("special_words.txt")
    3 words read

    >>> sf.num_words
    3

    >>> sf.random() in sf.words
    True

    """
    def read_words(self):
        """
        Read words from the file excluding blank spaces and commented out words.

        Returns:
            List of only accepted words
        """
        words = super().read_words()
        return [word for word in words if word.strip() and not word.startswith('#')]

    