from re import T
from hilo import Hil

class Director:

    def __init__(self):
        self.is_playing = True
        self.start =""
        self.score = 300
        self.total_score = 0
        hil = Hil()
        self.hilo = hil
        

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """

        while self.is_playing and self.total_score >= 0:
            self.do_outputs()

    def get_inputs(self):
        """ ASK THE USER IF THE CARD IS HIGER OR LOWER"""
        roll_hilo = input('Higer or lower? [h/l] ')
        self.start = roll_hilo
    ''' if roll_hilo == "h":
            self.start = roll_hilo
        elif roll_hilo == "l":
            self.start = roll_hilo'''


    def do_updates(self):
        
        if self.start == "h":
            hilo = self.hilo
            hilo.roll_h()
            self.score = hilo.points

            

        elif self.start == "l":

            hilo = self.hilo
            hilo.roll_l()
            self.score = hilo.points

        else:
            self.is_playing = False
        
        self.total_score = self.score


    
    def do_outputs(self):

        values = ""
        val_next = ""

        hilo = self.hilo

        values = f"{hilo.value}"
        val_next = f"{hilo.next} "
        self.do_updates()

        print(f"The card is: {values}")
        self.get_inputs()

        print (f"Next Card Was: {val_next}")
        print(f"Your score is: {self.total_score}\n")
        ask = input("Play again? y/n\n")

        if ask == "y":
            self.is_playing = True
        else:
            self.is_playing = False
        
        


        #self.is_playing == (self.score > 0)
