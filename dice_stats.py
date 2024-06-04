from die import Die
from tqdm import tqdm
from collections import Counter

class FiveDice:
    def __init__(self):
        self.dice = [Die() for number in range(5)]

    def roll(self):
        for die in self.dice:
            die.roll()
        return self.faces()

    def faces(self):
        return [die.face for die in self.dice]

    def all_ones(self):
        for face in self.faces():
            if face != 1:
                return False
        return True

    def is_three_of_a_kind(self):
        listOfFaces = self.faces()
        listOfFaces.sort()
        if listOfFaces[0] == listOfFaces[1] and listOfFaces[0] == listOfFaces[2]:
            return True
        elif listOfFaces[1] == listOfFaces[2] and listOfFaces[1] == listOfFaces[3]:
            return True
        elif listOfFaces[2] == listOfFaces[3] and listOfFaces[2] == listOfFaces[4]:
            return True
        else:
            return False

    def is_four_of_a_kind(self):
        listOfFaces = self.faces()
        listOfFaces.sort()
        if listOfFaces[0] == listOfFaces[3]:
            return True
        elif listOfFaces[1] == listOfFaces[4]:
            return True
        else:
            return False

dice = FiveDice()
successes = 0
trials = 1000000
for trial in tqdm(range(trials)):
    dice.roll()
    if dice.is_three_of_a_kind():
        successes += 1

print(successes/trials)


