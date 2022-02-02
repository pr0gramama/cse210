import random

class Seeker():
    """The user finding the seeker.  The responsibility of the Seeker is to
    track distance between the users guess and the distance to the Hider.
    
    Attributes:
        guess (int): the guessed postion of the Seeker from 1 to 1000.
    """
    def __init__(self):
        """Gets the guess of the Seeker and returns the number of the guessed
        postion."""
        self.guess = 0

    def get_guess(self):
        """Takes the number of the guess and returns it"""
        number = self.guess
        return number

    def change_guess(self, guess):
        """Changes the new guess to a new position."""
        self.guess = guess
