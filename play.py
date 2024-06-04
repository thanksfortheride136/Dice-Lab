from yahtzee import Yachtzee
from yahtzee_goals import (
    GoalOnes, 
    GoalTwos, 
    GoalThrees,
    GoalFours,
    GoalFives,
    GoalSixes,
    GoalThreeOfAKind,
    GoalFourOfAKind,
    GoalFullHouse,
    GoalSmallStraight,
    GoalLargeStraight,
    GoalYahtzee,
    GoalChance
)

goals = [
    GoalOnes(), 
    GoalTwos(),
    GoalThrees(),
    GoalFours(),
    GoalFives(),
    GoalSixes(),
    GoalThreeOfAKind(),
    GoalFourOfAKind(),
    GoalFullHouse(),
    GoalSmallStraight(),
    GoalLargeStraight(),
    GoalYahtzee(),
    GoalChance()
]

game = Yachtzee(goals)
game.play()
