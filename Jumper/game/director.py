from pyray import is_sound_playing
from game.jumper import Jumper
from game.puzzle import Puzzle
from game.terminal_service import TerminalService

class Director:
    
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        puzzle (puzzle): The game's puzzle.
        is_playing (boolean): Whether or not to keep playing.
        jumper (Jumper): The game's Jumper.
        terminal_service: For getting and displaying information on the terminal.
    """
    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """

        self.puzzle = Puzzle()
        self.is_playing = True
        self.jumper = Jumper()
        self.terminal_service = TerminalService()

    def start_game(self):
        
        while self.is_sound_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()


    def get_inputs(self):
        pass
    def do_updates(self):
        pass
    def do_outputs(self):
        pass

