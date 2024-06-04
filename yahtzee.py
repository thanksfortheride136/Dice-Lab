from die import Die

class Yachtzee:
    """A command-line Yahtzee game.
    This version of Yahtzee is initialized with a list of goals.
    """

    """runs when the object is instantiated, sets attributes for score, goals and dice. Dice is creating a dice roll 5 times
    """
    def __init__(self, goals):
        self.score = 0
        self.goals = goals
        self.dice = [Die() for num in range(5)]

        
    """prints a welcome message and uses a while loop to say if the goal is 0, then run the play_round() method. then print your final score out.
    """
    def play(self):
        print("Welcome to Yachtzee!")
        while self.count_unused_goals() > 0:
            self.play_round()
        print(f"Your final score was {self.score}")

        
    """its prints =*80 then it sets rolls to 3. Then it shows how many rolls you have left. it shows how many rolls you ahve left after thdice roles. adds to the score
    """
    def play_round(self):
        print("=" * 80)
        self.rolls_left = 3
        for die in self.dice:
            die.roll()
        self.show_status()
        goal = self.choose_goal()
        goal.used = True
        self.score += goal.score(self.dice)

    """Used to show score, rolls left and dice in the game.
    """
    def show_status(self):
        dice = ', '.join([str(die) for die in self.dice])
        print(f"Score: {self.score}. Rolls left: {self.rolls_left}. Dice: {dice}.")

    """Used to show score, rolls left and dice in the game.
    """
    def choose_goal(self):
        options = []
        unused_goals = self.get_unused_goals()
        for goal in unused_goals:
            option = goal.prompt(self.dice)
            options.append(option)
        if self.rolls_left > 0:
            options.append("Re-roll")
        choice = self.get_choice(options)
        if options[choice] == "Re-roll":
            self.reroll()
            self.show_status()
            return self.choose_goal()
        else:
            return unused_goals[choice]
        
    """
    Displays options amd prompts user to make choice. If input is valid return the choice.
    """
    def get_choice(self, options):
        print("What would you like to do?")
        for i, option in enumerate(options):
            print(f"{i}. {option}")
        choice = input("> ")
        while not self.option_choice_is_valid(choice, options):
            print("Sorry, that's not a valid choice.")
            choice = input("> ")
        return int(choice)

    """
    Chekcs if the users chouice is valid, returns true or false.
    """
    def option_choice_is_valid(self, choice, options):
        if not choice.isdigit():
            return False
        if int(choice) < 0:
            return False
        if int(choice) >= len(options):
            return False
        return True

    """
    counts unused goals
    """
    def count_unused_goals(self):
        return len(self.get_unused_goals())

    """
    iterates through sel.goals and ammends unused goals list with unused goals.
    """
    def get_unused_goals(self):
        unused_goals = []
        for goal in self.goals:
            if not goal.used:
                unused_goals.append(goal)
        return unused_goals

    """
    rerolls dice, decreased amount of rolls
    """
    def reroll(self):
        self.rolls_left -= 1
        choices = self.get_reroll_choices()
        dice_to_reroll = self.get_dice_to_reroll(choices)
        for die in dice_to_reroll:
            die.roll()

    """
    Determiens whcih dice should be rerolled
    """
    def get_dice_to_reroll(self, choice_ints):
        dice_to_reroll = []
        for die in self.dice:
            if die.face in choice_ints:
                choice_ints.remove(die.face)
                dice_to_reroll.append(die)
        return dice_to_reroll

    """
    Prompts to enter which dice to re-roll
    """
    def get_reroll_choices(self):
        print("Which dice do you want to re-roll?")
        choices = input("> ")
        while not self.reroll_choices_are_valid(choices):
            print("Please enter the numbers on dice you want to re-roll.")
            choices = input("> ")
        choice_ints = [int(digit) for digit in choices]
        return choice_ints
        
    """
    Validates choices for reroll
    """
    def reroll_choices_are_valid(self, choices_str):
        if not choices_str.isdigit():
            return False
        choice_ints = [int(digit) for digit in choices_str]
        for die in self.dice:
            if die.face in choice_ints:
                choice_ints.remove(die.face)
        return len(choice_ints) == 0
