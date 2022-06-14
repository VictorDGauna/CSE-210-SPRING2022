import random

class Hil:
    def __init__(self):
        self.play = True
        self.value = 0
        self.next = 0
        self.points = 0

    def roll_h(self):
        self.value = random.randint(1,13)
        self.next = random.randint(1,13)
        if self.value < self.next:
            self.points += 100
        else:
            self.points -= 75
    def roll_l(self):
        self.value = random.randint(1,13)
        self.next = random.randint(1,13)
        if self.value > self.next:
            self.points += 100
        else:
            self.points -= 75
    

        