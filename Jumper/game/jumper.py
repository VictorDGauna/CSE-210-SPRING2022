import random
from display import Display
from terminal_service import TerminalService
list_words = ["LITERALLY","IRONIC","IRREGARDLESS","WHOM",
        "COLONEL","NONPLUSSED","DISINTERESTED",
        "ENORMITY","LIEUTENANT","UNABASHED"]
        ## here create a dictionary with the words to choose

class Jumper:
    #this class make the work most important because take the information
    #from the player and show the picture from the display file
    def __init__(self):

       
        self.word_choosed = random.choice(list_words)
        
        self._guess = ""
        self._line = list(len(self.word_choosed)*'_')
        self.heart = 4
        self.win = False
        self.over = False

    def letter_check(self, letter,word_choosed):

        for i in range(0, len(self.word_choosed)):
            letter = self.word_choosed[i]
            if self._guess == letter:
                self._line[i] = self._guess
        if '_' not in self._line:
            return True
        else:
            return False

    def lives(self):

        print (Display[4-self.heart])
        print(self._line)

    def process(self):
        while self.win == False and self.heart > 0:
            self.lives()
            self._guess = (input('guess letter [a-z]: ')).upper()

            if self._guess == self.word_choosed:
                self.win = True
                self._line = self.word_choosed
            if len(self._guess) == 1 and self._guess in self.word_choosed:
                self.win = self.letter_check(self._guess, self.word_choosed)
                print('Good Work!!')
            
            else:
                print ("Sorry, You Lose\n")
                self.heart -= 1

                            
            if self.win == True:
                print (f" You Guessed {self.word_choosed}\n")

            if self.heart == 0:

                print(Display[4])
                print("Tray a New Game")
                print('The secret word was:',self.word_choosed)
            

            



       
