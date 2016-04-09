import random

# first functions for use in calculating score, each one called changes the list item that the score is tallied to


def aces():
    played[0] = 0
    for num in dice:
        if num == 1:
            played[0] += 1
    if player == 1:
        played0[0] = played[0]
    else:
        played1[0] = played[0]
    return


def twos():
    played[1] = 0
    for num in dice:
        if num == 2:
            played[1] += 2
    if player == 1:
        played0[1] = played[1]
    else:
        played1[1] = played[1]
    return


def threes():
    played[2] = 0
    for num in dice:
        if num == 3:
            played[2] += 3
    if player == 1:
        played0[2] = played[2]
    else:
        played1[2] = played[2]
    return


def fours():
    played[3] = 0
    for num in dice:
        if num == 4:
            played[3] += 4
    if player == 1:
        played0[3] = played[3]
    else:
        played1[3] = played[3]
    return


def fives():
    played[4] = 0
    for num in dice:
        if num == 5:
            played[4] += 5
    if player == 1:
        played0[4] = played[4]
    else:
        played1[4] = played[4]
    return


def sixes():
    played[5] = 0
    for num in dice:
        if num == 6:
            played[5] += 6
    if player == 1:
        played0[5] = played[5]
    else:
        played1[5] = played[5]
    return


def threeofakind():
    played[6] = 0
    if dice[0] == dice[1] == dice[2] or dice[1] == dice[2] == dice[3] or dice[2] == dice[3] == dice[4]:
        for num in dice:
            played[6] += num
    if player == 1:
        played0[6] = played[6]
    else:
        played1[6] = played[6]
    return


def fourofakind():
    played[7] = 0
    if dice[0] == dice[1] == dice[2] == dice[3] or dice[1] == dice[2] == dice[3] == dice[4]:
        for num in dice:
            played[7] += num
    if player == 1:
        played0[7] = played[7]
    else:
        played1[7] = played[7]
    return


def fullhouse():
    played[8] = 0
    if (dice[0] == dice[1] == dice[2] and dice[3] == dice[4]) or (dice[0] == dice[1] and dice[2] == dice[3] == dice[4]):
        played[8] = 25
    if player == 1:
        played0[8] = played[8]
    else:
        played1[8] = played[8]
    return


def smallstraight():
    played[9] = 0
    if (dice[0] == dice[1] - 1 == dice[2] - 2 == dice[3] - 3) or (dice[1] == dice[2] - 1 == dice[3] - 2 == dice[4] - 3):
        played[9] = 30
    if player == 1:
        played0[9] = played[9]
    else:
        played1[9] = played[9]
    return


def largestraight():
    played[10] = 0
    if dice[0] == dice[1] - 1 == dice[2] - 2 == dice[3] - 3 == dice[4] - 4:
        played[10] = 40
    if player == 1:
        played0[10] = played[10]
    else:
        played1[10] = played[10]
    return


def yahtzee():
    played[11] = 0
    if dice[0] == dice[1] == dice[2] == dice[3] == dice[4]:
        played[11] = 50
    if player == 1:
        played0[11] = played[11]
    else:
        played1[11] = played[11]
    return


def chance():
    for num in dice:
        played[12] += num
    if player == 1:
        played0[12] = played[12]
    else:
        played1[12] = played[12]
    return


def yahtzeebonus():
    yahtzeebonusscore = 0
    if played0[13] < 300 and player == 0:
        yahtzeebonusscore = 100
        played[13] += yahtzeebonusscore
    if played1[13] < 300 and player == 1:
        yahtzeebonusscore = 100
        played1[13] += yahtzeebonusscore
    return


def roll():
    if whichRoll[0] == 0:
        die1 = random.randint(1, 6)
    if whichRoll[1] == 0:
        die2 = random.randint(1, 6)
    if whichRoll[2] == 0:
        die3 = random.randint(1, 6)
    if whichRoll[3] == 0:
        die4 = random.randint(1, 6)
    if whichRoll[4] == 0:
        die5 = random.randint(1, 6)
    dice = [die1, die2, die3, die4, die5]
    dice.sort()
    return dice


"""def playagainstbot():  # all of the code for playing against a bot
    while isDone[0] == False and isDone[1] == False:

        if isDone[0] == False and isDone[1] == True:
            player = 0
        elif isDone[0] == True and isDone[1] == False:
            player = 1
        if player == 0:  # If human's turn
            1 == 1  # placeholder
            player += 1
        elif player == 1:  # If bot's turn
            while rollNum < 3:
                whichRoll = [0, 0, 0, 0, 0]
                # TODO math calculations
                roll()

            # TODO
            player -= 1
    return"""


def checkisdone():  # Checks if the players are done
    if player == 0:
        for num in played0:
            if num == -1:
                return
        else:
            isDone[0] = True
    else:
        for num in played1:
            if num == -1:
                return
        else:
            isDone[1] = True


def playagainsthuman():  # code for two humans
    while isDone[0] == False and isDone[1] == False:
        if isDone[0] == False and isDone[1] == True:
            player = 0
        elif isDone[0] == True and isDone[1] == False:
            player = 1
        if player == 0:
            roll()
            if whichScoring == 0 and played0[0] == -1:
                aces()
            if whichScoring == 1 and played0[1] == -1:
                twos()
            if whichScoring == 2 and played0[2] == -1:
                threes()
            if whichScoring == 3 and played0[3] == -1:
                fours()
            if whichScoring == 4 and played0[4] == -1:
                fives()
            if whichScoring == 5 and played0[5] == -1:
                sixes()
            if whichScoring == 6 and played0[6] == -1:
                threeofakind()
            if whichScoring == 7 and played0[7] == -1:
                fourofakind()
            if whichScoring == 8 and played0[8] == -1:
                fullhouse()
            if whichScoring == 9 and played0[9] == -1:
                smallstraight()
            if whichScoring == 10 and played0[10] == -1:
                largestraight()
            if whichScoring == 11 and played0[11] == -1:
                yahtzee()
            if whichScoring == 12 and played0[12] == -1:
                chance()
            if whichScoring == 13 and played0[13] == -1:
                yahtzeebonus()

            checkisdone()

            if isDone[1] == False:
                player = 1
        if player == 1:
            roll()
            if whichScoring == 0 and played1[0] == -1:
                aces()
            if whichScoring == 1 and played1[1] == -1:
                twos()
            if whichScoring == 2 and played1[2] == -1:
                threes()
            if whichScoring == 3 and played1[3] == -1:
                fours()
            if whichScoring == 4 and played1[4] == -1:
                fives()
            if whichScoring == 5 and played1[5] == -1:
                sixes()
            if whichScoring == 6 and played1[6] == -1:
                threeofakind()
            if whichScoring == 7 and played1[7] == -1:
                fourofakind()
            if whichScoring == 8 and played1[8] == -1:
                fullhouse()
            if whichScoring == 9 and played1[9] == -1:
                smallstraight()
            if whichScoring == 10 and played1[10] == -1:
                largestraight()
            if whichScoring == 11 and played1[11] == -1:
                yahtzee()
            if whichScoring == 12 and played1[12] == -1:
                chance()
            if whichScoring == 13 and played1[13] == -1:
                yahtzeebonus()

            checkisdone()

            player = 0
    return


def bestplays():  # code for best move mode
    while isDone[0] == False:
        # run the dice rolling code here
        if dice[0] == dice[1] == dice[2] == dice[3] == dice[4]:
            yahtzee()
        elif (dice[0] == dice[1] - 1 == dice[2] - 2 == dice[3] - 3 == dice[4] - 4) and played0[10] != -1:
            largestraight()
        elif (dice[0] == dice[1] - 1 == dice[2] - 2 == dice[3] - 3) or (dice[1] == dice[2] - 1 == dice[3] - 2 == dice[4] - 3) and played0[9] != -1:
            smallstraight()
        elif (dice[0] == dice[1] == dice[2] and dice[3] == dice[4]) or (dice[0] == dice[1] and dice[2] == dice[3] == dice[4]) and played0[8] != -1:
            fullhouse()
        elif (dice[0] == dice[1] == dice[2] == dice[3] or dice[1] == dice[2] == dice[3] == dice[4]) and played0[7] != -1:
            fourofakind()
        elif (dice[0] == dice[1] == dice[2] or dice[1] == dice[2] == dice[3] or dice[2] == dice[3] == dice[4]) and played0[6] != -1:
            threeofakind()
        numdice = [0, 0, 0, 0, 0, 0]
        for num in dice:
            numdice[num - 1] += 1

        checkisdone()
    return


global player   # which player is up and playing
player = 0
global played
played = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
global played0   # the list that tracks each score in each category
played0 = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
global played1
played1 = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
global dice
global rollNum
rollNum = 1        # current roll of the current player, from 1-3
# list played tracks both the score kept in the respective slot, unused slots are set to -1, 14 items total
global yahtzeeTracker  # tracks if yahtzee was used or not for totaling the bonus
yahtzeeTracker = [0,0]
global gameMode  # Keeps track of game mode selected (1 = Bot, 2 = friend, 3 = best move)
gameMode = 0
global isDone  # Is the game over?
isDone = [False, False]
global whichRoll
whichRoll = [0, 0, 0, 0, 0]  # Which dice should be rolled?
global whichScoring
whichScoring = -1  # Which function should be used? (aces, twos, threes, etc.)
global scoringList


dice = roll()
aces()
print "dice are: {}".format(dice)
print "aces score would be: {}".format(played[0])
threes()
print"threes score would be: {}".format(played[2])


score = 0
# finally adds the list items together to get the final score.
for x in played0:
    if x == -1:
        x = 0
    score += x
# print "Score for player 1 is: {}".format(score)

for x in played1:
    if x == -1:
        x = 0
    score += x
# print "Score for player 2 is: {}".format(score)
