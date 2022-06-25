import random
from typing import overload
from display import Display
list_words = ["LITERALLY","IRONIC","IRREGARDLESS","WHOM",
        "COLONEL","NONPLUSSED","DISINTERESTED",
        "ENORMITY","LIEUTENANT","UNABASHED"]

class Jumper:
    
    def __init__(self):

       
        self.word_choosed = random.choice(list_words)

        self.guess = ""
        self.line = list(len(self.word_choosed)*'_')
        self.heart = 4
        self.win = False
        self.over = False

    def letter_check(self, letter,word_choosed):

        for i in range(0, len(self.word_choosed)):
            letter = self.word_choosed[i]
            if self.guess == letter:
                self.line[i] = self.guess
        if '_' not in self.line:
            return True
        else:
            return False

    def lives(self):

        print (Display[4-self.heart])
        print(self.line)

    def process(self):
        while self.win == False and self.heart > 0:
            self.lives()
            self.guess = (input('guess letter [a-z]: ')).upper()

            if self.guess == self.word_choosed:
                self.win = True
                self.line = self.word_choosed
            if len(self.guess) == 1 and self.guess in self.word_choosed:
                self.win = self.letter_check(self.guess, self.word_choosed)
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
            

            



       
