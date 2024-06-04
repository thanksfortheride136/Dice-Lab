# die.py
# ------
# By MWC Contributors
# Implments a Die class.

from random import randint

class Die:
    def __init__(self):
        self.roll()

    def __str__(self):
        return str(self.face)

    def roll(self):
        self.face = randint(1, 6)
        return self.face
