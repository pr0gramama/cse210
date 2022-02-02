from game.hider import Hider
from game.seeker import Seeker

class Director:
    """Directs the play of the game.  Responsibility is to keep track of 
    game play sequence
    
    Attributes:
        Hider = the random number representing the location of the Hider.
        Seeker = the user's guess as to the location of the Hider.
        is_playing = while the game is playing, continue the director.
    """

    
    
    def __init__(self):
        """Constructs a new instance of Director."""

        self.hider = Hider()
        self.is_playing = True
        self.seeker = Seeker()

    def start_game(self):
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.display_outputs()

    def get_inputs(self):
        """Gets a number guess from Seeker
        """
        new_guess = input("Enter a location (1-1000): ")
        self.seeker.move_guess(new_guess)

    def do_updates(self):
        """Tracks Seeker's new guess"""
        self.hider.track_seeker(self._seeker)

    def display_outputs(self):
        hint = self._hider.hint()
        self.display_text(hint)
        if self.hider.is_found():
            self.is_playing = False