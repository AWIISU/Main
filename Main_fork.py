import random
#import cv2
#import numpy as np
DICE_SIZE = 16
BLUR_FACTOR = 5
RED_LOW_THRESHOLD = 209
MIN_PIP_AREA = 10

# first functions for use in calculating score, each one called changes the list item that the score is tallied to


def aces(cubes):
    played[0] = 0
    for num in cubes:
        if num == 1:
            played[0] += 1
    if player == 0:
        played0[0] = played[0]

    else:
        played1[0] = played[0]
    return played[0]


def twos(cubes):
    played[1] = 0
    for num in cubes:
        if num == 2:
            played[1] += 2
    if player == 0:
        played0[1] = played[1]
    else:
        played1[1] = played[1]
    return played[1]


def threes(cubes):
    played[2] = 0
    for num in cubes:
        if num == 3:
            played[2] += 3
    if player == 0:
        played0[2] = played[2]
    else:
        played1[2] = played[2]
    return played[2]


def fours(cubes):
    played[3] = 0
    for num in cubes:
        if num == 4:
            played[3] += 4
    if player == 0:
        played0[3] = played[3]
    else:
        played1[3] = played[3]
    return played[3]


def fives(cubes):
    played[4] = 0
    for num in cubes:
        if num == 5:
            played[4] += 5
    if player == 0:
        played0[4] = played[4]
    else:
        played1[4] = played[4]
    return played[4]


def sixes(cubes):
    played[5] = 0
    for num in cubes:
        if num == 6:
            played[5] += 6
    if player == 0:
        played0[5] = played[5]
    else:
        played1[5] = played[5]
    return played[5]


def threeofakind(cubes):
    played[6] = 5
    #if cubes[0] == cubes[1] == cubes[2] or cubes[1] == cubes[2] == cubes[3] or cubes[2] == cubes[3] == cubes[4]:
    for num in cubes:
        played[6] += num
    if player == 0:
        played0[6] = played[6]
    else:
        played1[6] = played[6]
    return played[6]


def fourofakind(cubes):
    played[7] = 0
    if cubes[0] == cubes[1] == cubes[2] == cubes[3] or cubes[1] == cubes[2] == cubes[3] == cubes[4]:
        for num in cubes:
            played[7] += num
    if player == 0:
        played0[7] = played[7]
    else:
        played1[7] = played[7]
    return played[7]


def fullhouse(cubes):
    played[8] = 0
    if (cubes[0] == cubes[1] == cubes[2] and cubes[3] == cubes[4]) or (cubes[0] == cubes[1] and cubes[2] == cubes[3] == cubes[4]):
        played[8] = 25
    if player == 0:
        played0[8] = played[8]
    else:
        played1[8] = played[8]
    return played[8]


def smallstraight(cubes):
    played[9] = 0
    if (cubes[0] == cubes[1] - 1 == cubes[2] - 2 == cubes[3] - 3) or (cubes[1] == cubes[2] - 1 == cubes[3] - 2 == cubes[4] - 3):
        played[9] = 30
    if player == 0:
        played0[9] = played[9]
    else:
        played1[9] = played[9]
    return played[9]


def largestraight(cubes):
    played[10] = 0
    if cubes[0] == cubes[1] - 1 == cubes[2] - 2 == cubes[3] - 3 == cubes[4] - 4:
        played[10] = 40
    if player == 0:
        played0[10] = played[10]
    else:
        played1[10] = played[10]
    return played[10]


def yahtzee(cubes):
    played[11] = 0
    if cubes[0] == cubes[1] == cubes[2] == cubes[3] == cubes[4]:
        played[11] = 50
    if player == 0:
        played0[11] = played[11]
    else:
        played1[11] = played[11]
    return played[11]


def chance(cubes):
    for num in cubes:
        played[12] += num
    if player == 0:
        played0[12] = played[12]
    else:
        played1[12] = played[12]
    return played[12]


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
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    die3 = random.randint(1, 6)
    die4 = random.randint(1, 6)
    die5 = random.randint(1, 6)
    dice = [die1, die2, die3, die4, die5]
    dice.sort()
    print "it works"
    return dice

'''def getdice():
    loopCount = 0
    def resizeRect(rect, sizeFactor):
        return (rect[0], (rect[1][0] + sizeFactor,rect[1][1] + sizeFactor), rect[2])
    img = cv2.imread("dice2.png")
    blurred = cv2.medianBlur(img,BLUR_FACTOR)
    blue = cv2.split(blurred)[0]
    green = cv2.split(blurred)[1]
    red = cv2.split(blurred)[2]
    diceblocks = cv2.threshold(red, RED_LOW_THRESHOLD, 255, 1)
    invdiceblocks = 255 - diceblocks[1]
    pyramids = cv2.distanceTransform(invdiceblocks, 2, 3)
    cv2.normalize(pyramids, pyramids, 0, 1.2, cv2.NORM_MINMAX)
    markers = cv2.threshold(pyramids, 0.8, 1, 0)[1]
    bwImg = cv2.convertScaleAbs(markers * 255)
    _, pyramids, hierarchy = cv2.findContours(bwImg.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    print str(len(pyramids)) + " dice."
    for pyramid in pyramids:
        rect = cv2.minAreaRect(pyramid)
        rect = resizeRect(rect, DICE_SIZE)
        floatBox = cv2.boxPoints(rect)
        intBox = np.int0(floatBox)
        bwImg = cv2.drawContours(bwImg,[intBox],0,(255,0,0),-1)
        pts1 = floatBox
        a,b,c,d = cv2.boundingRect(intBox)
        pts2 = np.float32([[a,b],[a+c,b],[a,b+d],[a+c,b+d]])
        M = cv2.getPerspectiveTransform(pts1,pts2)
        dst = cv2.warpPerspective(bwImg,M,pts2.shape)
    _, contours, hierarchy = cv2.findContours(bwImg.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    pips = 255 - cv2.threshold(cv2.cvtColor(blurred, cv2.COLOR_RGB2GRAY), 200, 255, 1)[1]
    onlypips = cv2.bitwise_and(bwImg,pips)
    dice = cv2.cvtColor(onlypips, cv2.COLOR_GRAY2RGB)
    dice_results = [0,0,0,0,0]
    wrongdice = 0
    for contour in contours:
        pips = 0
        rect = cv2.minAreaRect(contour)
        floatBox = cv2.boxPoints(rect)
        intBox = np.int0(floatBox)
        a,b,c,d = cv2.boundingRect(intBox)
        subimage = onlypips[b:b+d,a:a+c]
        _,pip_contours, subhierarchy = cv2.findContours(subimage.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for pip in pip_contours:
            if cv2.contourArea(pip) >= MIN_PIP_AREA:
                pips = pips + 1
        if pips > 6 or pips == 0:
            wrongdice = wrongdice + 1
            print pips
        else:
            dice_results[loopCount] = pips
            cv2.putText(dice,str(pips),(a,b-5),0,1,(0,0,255))
            loopCount += 1
    dice_results.sort()
    print dice_results
    print str(wrongdice) + " erroneous objects found."
    cv2.drawContours(dice,contours,-1,(255,255,0),1)
    cv2.imshow('Dice', dice)
    cv2.imshow('Original',img)
    def doCallbackTest(value):
        tmpImg = red.copy()
        newImg = 255 - cv2.threshold(tmpImg, value, 255, 1)[1] #cv2.threshold(src, thresh, maxval, type
        cv2.imshow('Dice',newImg)
    lowThreshold = 1
    max_lowThreshold = 255
    cv2.waitKey(0)
    cv2.destroyAllWindows()'''


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
    i = 0
    if player == 0:
        for num in played0:
            if num == -1 and i < 12:
                return
            i += 1
        isDone[0] = True
        return
    else:
        for num in played1:
            if num == -1 and i < 12:
                return
            i += 1
        isDone[1] = True
        return


def playagainsthuman():  # code for two humans

    global player  # which player is up and playing
    player = 0
    global played
    played = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    global played0  # the list that tracks each score in each category
    played0 = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    global played1
    played1 = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    global dice
    dice = [0, 0, 0, 0, 0]
    global rollNum
    rollNum = 1  # current roll of the current player, from 1-3
    # list played tracks both the score kept in the respective slot, unused slots are set to -1, 14 items total
    global yahtzeeTracker  # tracks if yahtzee was used or not for totaling the bonus
    yahtzeeTracker = [0, 0]
    global gameMode  # Keeps track of game mode selected (1 = Bot, 2 = friend, 3 = best move)
    gameMode = 0
    global isDone  # Is the game over?
    isDone = [False, False]
    # global whichRoll
    # whichRoll = [0, 0, 0, 0, 0]   Which dice should be rolled?
    global whichScoring
    whichScoring = -1  # Which function should be used? (aces, twos, threes, etc.)
    global scoringList

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


def bestplays(cube):  # code for best move mode
        # run the dice rolling code here
        numdice = [0, 0, 0, 0, 0, 0]
        for num in cube:
            numdice[num - 1] += 1
        if cube[0] == cube[1] == cube[2] == cube[3] == cube[4] and played0[11] == -1:
            return "yahtzee"
        elif (cube[0] == cube[1] - 1 == cube[2] - 2 == cube[3] - 3 == cube[4] - 4) and played0[10] == -1:
            return "large straight"
        elif (cube[0] == cube[1] - 1 == cube[2] - 2 == cube[3] - 3) or (cube[1] == cube[2] - 1 == cube[3] - 2 == cube[4] - 3) and played0[9] == -1:
            return "small straight"
        elif (cube[0] == cube[1] == cube[2] and cube[3] == cube[4]) or (cube[0] == cube[1] and cube[2] == cube[3] == cube[4]) and played0[8] == -1:
            return "full house"
        elif (cube[0] == cube[1] == cube[2] == cube[3] or cube[1] == cube[2] == cube[3] == cube[4]) and played0[7] == -1:
            return "four of a kind"
        elif (cube[0] == cube[1] == cube[2] or cube[1] == cube[2] == cube[3] or cube[2] == cube[3] == cube[4]) and played0[6] == -1:
            return "three of a kind"
        elif numdice[0] > 2 and played0[0] == -1:
            return "aces"
        elif numdice[1] > 2 and played0[1] == -1:
            return "twos"
        elif numdice[2] > 2 and played0[2] == -1:
            return "threes"
        elif numdice[3] > 2 and played0[3] == -1:
            return "fours"
        elif numdice[4] > 2 and played0[4] == -1:
            return "fives"
        elif numdice[5] > 2 and played0[5] == -1:
            return "sixes"
        elif played0[12] == -1:
            return "chance"
        elif played0[0] == -1 and numdice[0] > 0:
            return "aces"
        elif played0[1] == -1 and numdice[1] > 0:
            return "twos"
        elif played0[2] == -1 and numdice[2] > 0:
            return "threes"
        elif played0[3] == -1 and numdice[3] > 0:
            return "fours"
        elif played0[4] == -1 and numdice[4] > 0:
            return "fives"
        elif played0[5] == -1 and numdice[5] > 0:
            return "sixes"
        elif played0[0] == -1:
            return "aces"
        elif played0[1] == -1:
            return "twos"
        elif played0[2] == -1:
            return "threes"
        elif played0[3] == -1:
            return "fours"
        elif played0[4] == -1:
            return "fives"
        elif played0[5] == -1:
            return "sixes"
        elif played0[6] == -1:
           return "three of a kind"
        elif played0[7] == -1:
            return "four of a kind"
        elif played0[8] == -1:
            return "full house"
        elif played0[9] == -1:
            return "small straight"
        elif played0[10] == -1:
            return "large straight"
        return "yahtzee"


global player   # which player is up and playing
player = 0
global played
played = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
global played0   # the list that tracks each score in each category
played0 = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
global played1
played1 = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
global dice
dice = [0, 0, 0, 0, 0]
global rollNum
rollNum = 1        # current roll of the current player, from 1-3
# list played tracks both the score kept in the respective slot, unused slots are set to -1, 14 items total
global yahtzeeTracker  # tracks if yahtzee was used or not for totaling the bonus
yahtzeeTracker = [0,0]
global gameMode  # Keeps track of game mode selected (1 = Bot, 2 = friend, 3 = best move)
gameMode = 0
global isDone  # Is the game over?
isDone = [False, False]
# global whichRoll
# whichRoll = [0, 0, 0, 0, 0]   Which dice should be rolled?
global whichScoring
whichScoring = -1  # Which function should be used? (aces, twos, threes, etc.)
global scoringList


"""dice = [1, 1, 1, 1, 1]
bestplays(dice)
checkisdone()
print "dice are: {}".format(dice)
print "aces score would be: {}".format(played0[0])
print"threes score would be: {}".format(played0[2])
print"three of a kind score would be: {}".format(played0[6])
print"Yahtzee score would be: {}".format(played0[11])
print"Is he done? {}".format(isDone[0])"""

#dice = roll()
#print"Dice are: {}".format(dice)



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
