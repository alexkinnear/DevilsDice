import time

import pygame
import random
from Button import Button

pygame.init()

# ------ Colors ------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_RED = (200, 0, 0)
BLUE = (0, 0, 255)
LIGHT_GREY = (211, 211, 211)

# ------ Display ------
dis_width = 800
dis_height = 800
dis = pygame.display.set_mode((dis_width, dis_height))
dis.fill(WHITE)

myTurn = True
myPts = 0
devilsPts = 0

def drawBoard(my_score, devils_score):
    # draw score increments of 10
    font = pygame.font.SysFont(None, 48)
    for i in range(1, 11):
        x = dis_width / 15
        y = dis_height - (i * (dis_height / 10))
        img = font.render(str(i * 10), True, BLACK)
        dis.blit(img, (x, y))

    # Draw user and devil text
    my_x = dis_width / 3
    devil_x = dis_width / 3 * 2
    y = dis_height - 30
    user = font.render("User", True, BLUE)
    dis.blit(user, (my_x, y))
    devil = font.render("Devil", True, DARK_RED)
    dis.blit(devil, (devil_x, y))

    # draw buttons
    roll = Button(dis, LIGHT_GREY, dis_width / 2 - 15, dis_height / 2, 100, 50, "roll")
    roll.draw()
    roll.add_text("Roll", 48, BLACK)
    pass_turn = Button(dis, LIGHT_GREY, dis_width / 2 - 15, dis_height / 2 + dis_height / 10, 100, 50, "pass")
    pass_turn.draw()
    pass_turn.add_text("Pass", 48, BLACK)

    # draw player score bars
    pygame.draw.rect(dis, BLUE, [my_x, dis_height - ((dis_height / 10) * (my_score / 10)), dis_width / 10, (dis_height / 10) * (my_score / 10) - 30])
    pygame.draw.rect(dis, DARK_RED, [devil_x, dis_height - ((dis_height / 10) * (devils_score / 10)), dis_width / 10, (dis_height / 10) * (devils_score / 10) - 30])


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    myRndPts = 0
    while myTurn:
        selection = input("Roll: 'r', Pass: 'p'")
        if selection == 'r':
            die = random.randint(1, 6)
            if die == 1:
                myTurn = False
            myRndPts += die
        elif selection == 'p':
            myPts += myRndPts
            myTurn = False
    drawBoard(myPts, devilsPts)

    devilsRndPts = 0
    while not myTurn:
        if devilsPts < myPts:
            if devilsRndPts < 30:
                roll = random.randint(1, 6)
                if roll == 1:
                    myTurn = True
                devilsRndPts += roll
            else:
                devilsPts += devilsRndPts
                myTurn = True
        else:
            if devilsPts < 21:
                roll = random.randint(1, 6)
                if roll == 1:
                    myTurn = True
                devilsRndPts += roll
            else:
                devilsPts += devilsRndPts
                myTurn = True





pygame.quit()
