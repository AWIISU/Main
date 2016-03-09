import random

def aces(dice):
    played[0] += 1
    for num in dice:
        if (num == 1):
            played[0] += 1
    return

def twos(dice):
    played[1] += 1
    for num in dice:
        if (num == 2):
            played[1] += 2
    return

def threes(dice):
    played[2] += 1
    for num in dice:
        if (num == 3):
            played[2] += 3
    return

def fours(dice):
    played[3] += 1
    for num in dice:
        if (num == 4):
            played[3] += 4
    return

def fives(dice):
    played[4] += 1
    for num in dice:
        if (num == 5):
            played[4] += 5
    return

def sixes(dice):
    played[5] += 1
    for num in dice:
        if (num == 6):
            played[5] += 6
    return

def threeofaKind(dice):
    played[6] += 1
    for num in dice:
        played[6] += num
    return

def fourofaKind(dice):
    played[7] += 1
    for num in dice:
        played[7] += num
    return

def fullHouse(dice):
    played[8] = 25
    return

def smallStraight(dice):
    played[9] = 30
    return

def largeStraight(dice):
    played[10] = 40
    return

def yahtzee(dice):
    played[11] = 50
    return

def chance(dice):
    for num in dice:
        played[12] += num
    return

def yahtzeeBonus(dice):
    yahtzeeBonusScore = 0
    if (played[13] < 300):
        yahtzeeBonusScore = 100
    return yahtzeeBonusScore

def roll():
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    die3 = random.randint(1,6)
    die4 = random.randint(1,6)
    die5 = random.randint(1,6)
    dice = [die1, die2, die3, die4, die5]
    return dice

def bestMove(dice):
    if (dice[0] == dice[1] and dice[0] == dice[2] and dice[0] == dice[3] and dice[0] == dice[4] and dice[0] == dice[5]): #Checks for yahtzee
        if(yahtzeeTracker == 0):
            yahtzeeTracker += 1
            dice[11] == 50






global player
global roll
global played
player = 1
roll = 1
played = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
global yahtzeeTracker
yahtzeeTracker = 0

#print "Dice numbers are: {}, {}, {}, {}, {}.".format(die1, die2, die3, die4, die5)



score = aces(dice)
print "Score is: {}".format(score)

