from hilo import Hil

class Director:

    def __init__(self):
        self.is_playing = True
        self.score = 300
        self.total_score = 0
        hil = Hil()
        self.hilo = hil
        

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """

        while self.is_playing:
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """ ASK THE USER IF THE CARD IS HIGER OR LOWER"""
        roll_hilo = input('Higer or lower? [h/l] ')
        if roll_hilo == "h":
            self.is_playing = roll_hilo
        elif roll_hilo == "l":
            self.is_playing = roll_hilo


    def do_updates(self):
        
        if self.is_playing == "h":
            hilo = self.hilo
            hilo.roll_h()
            self.score = hilo.points
            self.total_score = self.score



        elif self.is_playing == "l":

            hilo = self.hilo
            hilo.roll_l()
            self.score = hilo.points
            self.total_score = self.score


    
    def do_outputs(self):
        values = ""
        val_next = ""

        hilo = self.hilo
        values = f"{hilo.value}"
        print(f"The card is: {values}")

        self.get_inputs()
        val_next = f"{hilo.next} "

        print (f"Next Card Was: {val_next}")
        print(f"Your score is: {self.total_score}\n")
        #self.is_playing == (self.score > 0)
