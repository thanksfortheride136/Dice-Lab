class GoalOnes:
    used = False

    def prompt(self, dice):
        potential_score = self.score(dice)
        return f"Ones ({potential_score})"

    def score(self, dice):
        total = 0
        for die in dice:
            if die.face == 1:
                total += 1
        return total


class GoalTwos:
    used = False

    def prompt(self, dice):
        potential_score = self.score(dice)
        return f"Twos ({potential_score})"

    def score(self, dice):
        total = 0
        for die in dice:
            if die.face == 2:
                total += 2
        return total


class GoalThrees:
    used = False

    def prompt(self, dice):
        potential_score = self.score(dice)
        return f"Threes ({potential_score})"

    def score(self, dice):
        total = 0
        for die in dice:
            if die.face == 3:
                total += 3
        return total


class GoalFours:
    used = False

    def prompt(self, dice):
        potential_score = self.score(dice)
        return f"Fours ({potential_score})"

    def score(self, dice):
        total = 0
        for die in dice:
            if die.face == 4:
                total += 4
        return total


class GoalFives:
    used = False

    def prompt(self, dice):
        potential_score = self.score(dice)
        return f"Fives ({potential_score})"

    def score(self, dice):
        total = 0
        for die in dice:
            if die.face == 5:
                total += 5
        return total

class GoalSixes:
    used = False

    def prompt(self, dice):
        potential_score = self.score(dice)
        return f"Sixes ({potential_score})"

    def score(self, dice):
        total = 0
        for die in dice:
            if die.face == 6:
                total += 6
        return total


class GoalThreeOfAKind:
    used = False

    def prompt(self, dice):
        potential_score = self.score(dice)
        return f"Three of a kind ({potential_score})"

    def faces(self, dice):
        return[die.face for die in dice]
    
    def is_three_of_a_kind(self, dice):
        listOfFaces = self.faces(dice)
        listOfFaces.sort()
        if listOfFaces[0] == listOfFaces[1] and listOfFaces[0] == listOfFaces[2]:
            return True
        elif listOfFaces[1] == listOfFaces[2] and listOfFaces[1] == listOfFaces[3]:
            return True
        elif listOfFaces[2] == listOfFaces[3] and listOfFaces[2] == listOfFaces[4]:
            return True
        else:
            return False

    def score(self, dice):
        if self.is_three_of_a_kind(dice):
            total = 0
            for die in dice:
                total += die.face
            return total
        else:
            return 0

class GoalFourOfAKind:
    used = False

    def prompt(self, dice):
        potential_score = self.score(dice)
        return f"Four of a kind ({potential_score})"

    def faces(self, dice):
        return[die.face for die in dice]
    
    def is_four_of_a_kind(self, dice):
        listOfFaces = self.faces(dice)
        listOfFaces.sort()
        if listOfFaces[0] == listOfFaces[3]:
            return True
        elif listOfFaces[1] == listOfFaces[4]:
            return True
        else:
            return False

    def score(self, dice):
        if self.is_four_of_a_kind(dice):
            total = 0
            for die in dice:
                total += die.face
            return total
        else:
            return 0

class GoalFullHouse:
    used = False

    def prompt(self, dice):
        potential_score = self.score(dice)
        return f"Full house ({potential_score})"

    def faces(self, dice):
        return[die.face for die in dice]

    def is_full_house(self, dice):
        listOfFaces = self.faces(dice)
        listOfFaces.sort()
        if listOfFaces[0] == listOfFaces[1] and listOfFaces[0] == listOfFaces[2] and listOfFaces[3] == listOfFaces[4]:
            return True
        elif listOfFaces[2] == listOfFaces[3] and listOfFaces[2] == listOfFaces[4] and listOfFaces[0] == listOfFaces[1]:
            return True
        else:
            return False

    def score(self, dice):
        if self.is_full_house(dice):
            return 25
        else:
            return 0

class GoalSmallStraight:
    used = False

    def prompt(self, dice):
        potential_score = self.score(dice)
        return f"Small straight ({potential_score})"

    def faces(self, dice):
        return[die.face for die in dice]

    def is_small_straight(self, dice):
        listOfFaces = self.faces(dice)
        listOfFaces.sort()
        foundSmallStraight = False
        for i in range (2):
            for j in range(3):
                if i == 0:
                    if j != 2:
                        if listOfFaces[j] == listOfFaces[j+1] - 1:
                            continue
                        else:
                            break
                    else:
                        if listOfFaces[j] == listOfFaces[j+1] - 1:
                            foundSmallStraight = True
                else:
                    if j != 2:
                        if listOfFaces[j+1] == listOfFaces[j+2] - 1:
                            continue
                        else:
                            break
                    else:
                        if listOfFaces[j+1] == listOfFaces[j+2] - 1:
                            foundSmallStraight = True
        return foundSmallStraight

    def score(self, dice):
        if self.is_small_straight(dice):
            return 30
        else:
            return 0

class GoalLargeStraight:
    used = False

    def prompt(self, dice):
        potential_score = self.score(dice)
        return f"Large straight ({potential_score})"

    def faces(self, dice):
        return[die.face for die in dice]

    def is_large_straight(self, dice):
        listOfFaces = self.faces(dice)
        listOfFaces.sort()
        for j in range(4):
            if j != 3:
                if listOfFaces[j] == listOfFaces[j+1] - 1:
                    continue
                else:
                    return False
            else:
                if listOfFaces[j] == listOfFaces[j+1] - 1:
                    return True
    
    def score(self, dice):
        if self.is_large_straight(dice):
            return 40
        else:
            return 0

class GoalYahtzee:
    used = False

    def prompt(self, dice):
        potential_score = self.score(dice)
        return f"Five of a kind ({potential_score})"

    def faces(self, dice):
        return[die.face for die in dice]
    
    def is_five_of_a_kind(self, dice):
        listOfFaces = self.faces(dice)
        listOfFaces.sort()
        if listOfFaces[0] == listOfFaces[4]:
            return True
        else:
            return False

    def score(self, dice):
        if self.is_five_of_a_kind(dice):
            return 50
        else:
            return 0

class GoalChance:
    used = False

    def prompt(self, dice):
        potential_score = self.score(dice)
        return f"Chance ({potential_score})"

    def score(self, dice):
        total = 0
        for die in dice:
            total += die.face
        return total