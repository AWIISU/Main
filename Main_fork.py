import random

#first functions for use in calculating score, each one called changes the list item that the score is tallied to

def aces(dice):
    for num in dice:
        if (num == 1):
            played[0] += 1
    if(player == 1):
        played0[0] = played[0]
    else:
        played1[0] = played[0]
    return


def twos(dice):
    for num in dice:
        if (num == 2):
            played[1] += 2
    return


def threes(dice):
    for num in dice:
        if (num == 3):
            played[2] += 3
    return


def fours(dice):
    for num in dice:
        if (num == 4):
            played[3] += 4
    return


def fives(dice):
    for num in dice:
        if (num == 5):
            played[4] += 5
    return


def sixes(dice):
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
    if(whichRoll[0] == 0):
        die1 = random.randint(1, 6)
    if(whichRoll[1] == 0):
        die2 = random.randint(1, 6)
    if(whichRoll[2] == 0):
        die3 = random.randint(1, 6)
    if(whichRoll[3] == 0):
        die4 = random.randint(1, 6)
    if(whichRoll[4] == 0):
        die5 = random.randint(1, 6)
    dice = [die1, die2, die3, die4, die5]
    return dice



def bestMove(dice):
    if (dice[0] == dice[1] and dice[0] == dice[2] and dice[0] == dice[3] and dice[0] == dice[4] and dice[0] == dice[
        5]) and (yahtzeeTracker == 0):  # Checks for yahtzee
        yahtzeeTracker += 1
        played[11] == 50
        #TODO like all of it

def playAgainstBot(): # all of the code for playing against a bot
    while(isDone[0] == False and isDone[1] == False):

        if(isDone[0] == False and isDone[1] == True):
            player = 0
        elif(isDone[0] == True and isDone[1] == False):
            player = 1
        if(player == 0): # If human's turn
            1 == 1 #placeholder
            player += 1
        elif(player == 1): # If bot's turn
            while(rollNum < 3):
                whichRoll = [0, 0, 0, 0, 0]
                #TODO math calculations
                roll()

            #TODO
            player -= 1
    return

def playAgainstHuman(): #  code for two humans

    return

def bestPlays(): # code for best move mode

    return


global player   #which player is up and playing
global played
global played0   #the list that tracks each score in each category
global played1
player = 0
global rollNum
rollNum = 1        #current roll of the current player, from 1-3
#list played tracks both the score kept in the respective slot, unused slots are set to -1, 14 items total
played = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
played0 = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
played1 = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
global yahtzeeTracker #tracks if yahtzee was used or not for totaling the bonus
yahtzeeTracker = [0,0]
global gameMode #Keeps track of game mode selected (1 = Bot, 2 = friend, 3 = best move)
gameMode = 0
global isDone # Is the game over?
isDone = [False,False]
global whichRoll
whichRoll = [0,0,0,0,0]


dice = roll()
aces(dice)
print "dice are: {}".format(dice)
print "aces score would be: {}".format(played[0])
threes(dice)
print"threes score would be: {}".format(played[2])



score = 0
#finally adds the list items together to get the final score.
for x in played0:
    if (x == -1):
        x = 0
    score += x
#print "Score for player 1 is: {}".format(score)

for x in played1:
    if (x == -1):
        x = 0
    score += x
#print "Score for player 2 is: {}".format(score)

