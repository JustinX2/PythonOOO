"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:

    def __init__(self,filepath):
        with open(filepath) as file:
            self.words=self.parse(file)
        print(f"{len(self.words)} words read")
    
    def parse(self,file):
        return [word.strip() for word in file]
    
    def random(self):
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    def parse(self,file):
        return [word.strip() for word in file if word.strip() and not word.startswith("#")]
