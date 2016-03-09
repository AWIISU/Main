import random

def aces(dice):
    acesScore = 0
    for num in dice:
        if (num == 1):
            acesScore += 1
    return acesScore

def twos(dice):
    twosScore = 0
    for num in dice:
        if (num == 2):
            twosScore += 2
    return twosScore

def threes(dice):
    threesScore = 0
    for num in dice:
        if (num == 3):
            threesScore += 3
    return threesScore

def fours(dice):
    foursScore = 0
    for num in dice:
        if (num == 4):
            foursScore += 4
    return foursScore

def fives(dice):
    fivesScore = 0
    for num in dice:
        if (num == 5):
            fivesScore += 5
    return fivesScore

def sixes(dice):
    sixesScore = 0
    for num in dice:
        if (num == 6):
            sixesScore += 6
    return sixesScore

def threeofaKind(dice):
    kind3Score = 0
    for num in dice:
        kind3Score += num
    return kind3Score

def fourofaKind(dice):
    kind4Score = 0
    for num in dice:
        kind4Score += num
    return kind4Score

def fullHouse(dice):
    houseScore = 25
    return houseScore

def smallStraight(dice):
    smStraightScore = 30
    return smStraightScore

def largeStraight(dice):
    lgStraightScore = 40
    return lgStraightScore

def yahtzee(dice, yahtzeeTracker):
    if(yahtzeeTracker > 0):
        yahtzeeScore = 100
    else:
        yahtzeeScore = 50
    return yahtzeeScore

def chance(dice):
    chanceScore = 0
    for num in dice:
        chanceScore += num
    return chanceScore


    


die1 = random.randint(1,6)
die2 = random.randint(1,6)
die3 = random.randint(1,6)
die4 = random.randint(1,6)
die5 = random.randint(1,6)

yahtzeeTracker = 0

print "Dice numbers are: {}, {}, {}, {}, {}.".format(die1, die2, die3, die4, die5)

dice = [die1, die2, die3, die4, die5]

score = aces(dice)
print "Score is: {}".format(score)

