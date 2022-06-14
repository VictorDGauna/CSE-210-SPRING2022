from hilo import Hil

class Director:

    def __init__(self):
        self.hilo = []
        self.is_playing = True
        self.score = 0
        self.total_score = 0
        for i in range(1):
            hil = Hil()
            self.hilo.append(hil)
        

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
        roll_hilo = input('Higer or lower? [h/l]')
        if roll_hilo == "h":
            self.is_playing = roll_hilo
        elif roll_hilo == "l":
            self.is_playing = roll_hilo


    def do_updates(self):
        
        if self.is_playing == "h":
            for i in range (len(self.hilo)):
                hilo = self.hilo[i]
                hilo.roll_h()
                self.score += hilo.points
        if self.is_playing == "l":
            for i in range (len(self.hilo)):
                hilo = self.hilo[i]
                hilo.roll_l()
                self.score += hilo.points 

        self.total_score += self.score

    
    def do_outputs(self):
        values = ""
        val_next = ""
        for i in range(len(self.hilo)):
            hilo = self.hilo[i]
            values += f"{hilo.value} "
            val_next += f"{hilo.next} "

        print(f"Your card is: {values}")
        self.get_inputs()
        print(f"Your score is: {self.total_score}")
        print (f"The next card was: {val_next}\n")
        self.is_playing == (self.score > 0)
