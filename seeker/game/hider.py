import random

class Hider:
    """The Hider represents a random integer from 1-1000.  
    Hider is hiding from the Seeker, the user who is trying
    to find the Hider.

    The responsibility of Hider is to fix a position and track
    its distance from the guesses of the Seeker.
    
    Attributes:
        _position (int) = the location of Hider
        _distance [int] = the distance of the guess of the
            seeker"""
    
    def __init__(self):
        """Constructs a new position for Hider.

        Arguments: 
            Hider(self) = an instance of hider"""
        self._position = random.randint(1,1000)
        self._distance = [0, 0]

    def hint(self):
        """Finds the proximity of a guess from and returns
        a hint to the Seeker."""
        hint = "(^.^)You are frozen!"
        if self._distance[-1] == 0:
            hint = "(;.;) You found me!"
        elif self._distance[-1] > self._distance[-2]:
            hint = "(^.^) You're getting COLDER!"
        elif self._distance[-1] < self._distance:
            hint = "(>.<) You're getting WARMER!"
        return hint

    def is_found(self):
        """If the guess of the Seeker is the location of the Hider is the same
        returns True.  If not, returns False"""
        return (self._distance[-1] == 0)

    def position_seeker(self, seeker):
        distance = (self.guess - seeker.get_location())