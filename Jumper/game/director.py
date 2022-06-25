from jumper import Jumper, list_words
from terminal_service import TerminalService

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

        self.is_playing = True
        self.jumper = Jumper()
        self.disp = list_words
        self.terminal_service = TerminalService()

    def start_game(self):
        
        while self.is_playing:
            self.get_inputs()
            self.do_updates()


    def get_inputs(self):
        self.disp

    def do_updates(self):
        self.jumper.process()
    

