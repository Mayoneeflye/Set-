#Set
#Cynthia Deng and Kevin Wang

#June 4,2017
#ICS3U1 - 02
#Submitted to Mr. Cope

#Set is a game that requires players to make sets with the cards on the board
#Input: Player uses their mouse to select cards they believe belong in a set
#Output: Visuals; menu, instructions, cards, scores, timer

import pygame
from pygame.locals import *
pygame.init()
import time
import CardList
import random
pygame.font.init()

def randomize_create_cards():
    global sample
    sample = random.sample(range(0, 81), 12)

    image1 = pygame.image.load(CardList.cardsList[sample[0]][0])
    image1 = pygame.transform.scale(image1, (60, 84))
    image2 = pygame.image.load(CardList.cardsList[sample[1]][0])
    image2 = pygame.transform.scale(image2, (60, 84))
    image3 = pygame.image.load(CardList.cardsList[sample[2]][0])
    image3 = pygame.transform.scale(image3, (60, 84))
    image4 = pygame.image.load(CardList.cardsList[sample[3]][0])
    image4 = pygame.transform.scale(image4, (60, 84))
    image5 = pygame.image.load(CardList.cardsList[sample[4]][0])
    image5 = pygame.transform.scale(image5, (60, 84))
    image6 = pygame.image.load(CardList.cardsList[sample[5]][0])
    image6 = pygame.transform.scale(image6, (60, 84))
    image7 = pygame.image.load(CardList.cardsList[sample[6]][0])
    image7 = pygame.transform.scale(image7, (60, 84))
    image8 = pygame.image.load(CardList.cardsList[sample[7]][0])
    image8 = pygame.transform.scale(image8, (60, 84))
    image9 = pygame.image.load(CardList.cardsList[sample[8]][0])
    image9 = pygame.transform.scale(image9, (60, 84))
    image10 = pygame.image.load(CardList.cardsList[sample[9]][0])
    image10 = pygame.transform.scale(image10, (60, 84))
    image11 = pygame.image.load(CardList.cardsList[sample[10]][0])
    image11 = pygame.transform.scale(image11, (60, 84))
    image12 = pygame.image.load(CardList.cardsList[sample[11]][0])
    image12 = pygame.transform.scale(image12, (60, 84))

    return (image1, image2, image3, image4, image5, image6, image7, image8, image9, image10, image11, image12)


size = (720,720)                                #set size of window screen
size2 = (300,300)                               #set size of background behind the cards
screen = pygame.display.set_mode(size)          #create screen
pygame.display.set_caption("Set!")              #set caption (title of the game)
background = pygame.Surface(size).convert()     #create background
background.fill((100,100,100))                  #fill background with color

cover = pygame.Surface((60,84))
cover.set_alpha(50)
cover.fill((0,0,0))
card1 = randomize_create_cards()

newSetImage = pygame.image.load("Images/New Set.png")
menuImage = pygame.image.load("Images/Menu.png")
instructionButtonImage = pygame.image.load("Images/Instructions Button.png")
playButtonImage = pygame.image.load("Images/Play Button.png")

#create cards
c1 = card1[0]
c2 = card1[1]
c3 = card1[2]
c4 = card1[3]
c5 = card1[4]
c6 = card1[5]
c7 = card1[6]
c8 = card1[7]
c9 = card1[8]
c10 = card1[9]
c11 = card1[10]
c12 = card1[11]

pygame.display.update()

game = False    #False = menu, True = Game

t1 = time.time()    #set current time

selected = 0   #set move count

#boolean for if cards have been clicked (if they have been clicked on by player)
c1c = False
c2c = False
c3c = False
c4c = False
c5c = False
c6c = False
c7c = False
c8c = False
c9c = False
c10c = False
c11c = False
c12c = False

#
c1s = False
c2s = False
c3s = False
c4s = False
c5s = False
c6s = False
c7s = False
c8s = False
c9s = False
c10s = False
c11s = False
c12s = False

#list for selected cards
selection = []

#score for player
score = 0

#loop condition
running = True  #main game loop condition

clock = pygame.time.Clock()

while running:

    clock.tick(30)

    if game == False:   #if menu, set time, allows the game to reset basically
        t1 = time.time()

    if game == True:    #if in game mode:

        #show the time until game over
        gray_a = pygame.Surface((160,40)).convert()
        gray_a.fill((220, 220, 220))
        myfont = pygame.font.SysFont('Comic Sans MS', 20)
        timer = myfont.render("time: {} s".format(round(300 - (time.time() - t1)),2),1,(0,0,0))
        screen.blit(gray_a, (0,0))

        screen.blit(timer,(0, 0))

        #score board
        score_board = myfont.render("score: {}".format(score),1,(0,0,0))
        screen.blit(gray_a, (0,40))

        screen.blit(score_board,(0, 40))

        #exit to main menu
        exit_sign = myfont.render("Main Menu".format(score),1,(0,0,0))
        screen.blit(gray_a, (720-160,0))

        screen.blit(exit_sign,(720-160, 0))

        pygame.display.update()

    if game == False:   #if menu, blit screen white background
        background = pygame.Surface(size)
        background = background.convert()
        background.fill((255,255,255))
        screen.blit(background,(0,0))
        screen.blit(menuImage, (230, 150))
        screen.blit(instructionButtonImage, (278, 320))
        screen.blit(playButtonImage, (278, 390))
        pygame.display.update()

    if not time.time() - t1 < 300:                              #when time reaches 300s (5 minutes), update caption and set menu
        myfont = pygame.font.SysFont('Comic Sans MS', 40)       #set font for game over
        go_sign = myfont.render("Game Over",1,(0,0,0))          #create game over text
        myfont = pygame.font.SysFont('Comic Sans MS',20)        #font for "click anywhere to continue" text
        clik_cont = myfont.render("Click anywhere to continue",1,(0,0,0))

        #blit background, game over sign, scoreboard, and "click anywhere to continue sign"
        screen.blit(background,(0,0))
        screen.blit(go_sign,(280,180))
        screen.blit(score_board,(330,360))
        screen.blit(clik_cont, (240,480))
        pygame.display.update() #show it all

        game = 4    #set game = 4 for mini event loop

        while game == 4:
            for ev in pygame.event.get():
                if ev.type == QUIT: #if player wants to exit, exit program
                    game = False
                    running = False

                if ev.type == MOUSEBUTTONDOWN:  #if player left clicks anywhere in the game window, proceed to main menu
                    if ev.button == 1:
                        game = False

        #reset game
        
        #reset cards
        card1 = randomize_create_cards()
        c1 = card1[0]
        c2 = card1[1]
        c3 = card1[2]
        c4 = card1[3]
        c5 = card1[4]
        c6 = card1[5]
        c7 = card1[6]
        c8 = card1[7]
        c9 = card1[8]
        c10 = card1[9]
        c11 = card1[10]
        c12 = card1[11]
        
        #reset card appearences
        screen.blit(c1, (210,210))      #draw new card
        screen.blit(c2, (285,210))      #draw new card
        screen.blit(c3, (360,210))      #draw new card
        screen.blit(c4, (435,210))      #draw new card
        screen.blit(c5, (210,310))      #draw new card
        screen.blit(c6, (285,310))      #draw new card
        screen.blit(c7, (360,310))      #draw new card
        screen.blit(c8, (435,310))      #draw new card
        screen.blit(c9, (210,410))      #draw new card
        screen.blit(c10, (285,410))     #draw new card
        screen.blit(c11, (360,410))     #draw new card
        screen.blit(c12, (435,410))     #draw new card

        #reset selected cards to 0
        selected = 0
        
        #reset all cards to not-clicked mode
        c1c = False
        c2c = False
        c3c = False
        c4c = False
        c5c = False
        c6c = False
        c7c = False
        c8c = False
        c9c = False
        c10c = False
        c11c = False
        c12c = False
        
        #empty the list containing selected cards
        selection = []
        
        c1s = False
        c2s = False
        c3s = False
        c4s = False
        c5s = False
        c6s = False
        c7s = False
        c8s = False
        c9s = False
        c10s = False
        c11s = False
        c12s = False
        
        #reset player score
        score = 0
    
    if selected == 3:   #if 3 cards have been selected
        selected = 0
        if c1c == True:     #appends a card and it's corresponding "values" to selection list
            c1c = False     #if the card was chosen as one of the 3 cards
            c1s = True      #This repeats for the following 11 cards as well
            selection.append(CardList.cardsList[sample[0]]) 
        if c2c == True:
            c2c = False
            c2s = True
            selection.append(CardList.cardsList[sample[1]])
        if c3c == True:
            c3c = False
            c3s = True
            selection.append(CardList.cardsList[sample[2]])
        if c4c == True:
            c4c = False
            c4s = True
            selection.append(CardList.cardsList[sample[3]])
        if c5c == True:
            c5c = False
            c5s = True
            selection.append(CardList.cardsList[sample[4]])
        if c6c == True:
            c6c = False
            c6s = True
            selection.append(CardList.cardsList[sample[5]])
        if c7c == True:
            c7c = False
            c7s = True
            selection.append(CardList.cardsList[sample[6]])
        if c8c == True:
            c8c = False
            c8s = True
            selection.append(CardList.cardsList[sample[7]])
        if c9c == True:
            c9c = False
            c9s = True
            selection.append(CardList.cardsList[sample[8]])
        if c10c == True:
            c10c = False
            c10s = True
            selection.append(CardList.cardsList[sample[9]])
        if c11c == True:
            c11c = False
            c11s = True
            selection.append(CardList.cardsList[sample[10]])
        if c12c == True:
            c12c = False
            c12s = True
            selection.append(CardList.cardsList[sample[11]])

        #the bottom segnment of code checks for whether or not the selected cards are a set
        #it takes the first values which is number, compares all of them, and if they're all the same, or all different,
        #then it does the same for colour, filling, and shape.
        #following the rules of set, these values have to be either all the same or all different
        #if that condition is met, it is a set and the cards are blitted over with new cards
        if (selection[0][1] != selection[1][1] != selection[2][1] and selection[0][2] != selection[1][2] != selection[2][2] \
           and selection[0][3] != selection[1][3] != selection[2][3] and selection[0][4] != selection[1][4] != selection[2][4])\
           or (selection[0][1] == selection[1][1] == selection[2][1] and selection[0][2] == selection[1][2] == selection[2][2] \
           and selection[0][3] == selection[1][3] == selection[2][3] and selection[0][4] != selection[1][4] != selection[2][4])\
           or (selection[0][1] == selection[1][1] == selection[2][1] and selection[0][2] == selection[1][2] == selection[2][2] \
           and selection[0][3] != selection[1][3] != selection[2][3] and selection[0][4] == selection[1][4] == selection[2][4])\
           or (selection[0][1] == selection[1][1] == selection[2][1] and selection[0][2] != selection[1][2] != selection[2][2] \
           and selection[0][3] == selection[1][3] == selection[2][3] and selection[0][4] == selection[1][4] == selection[2][4])\
           or (selection[0][1] != selection[1][1] != selection[2][1] and selection[0][2] == selection[1][2] == selection[2][2] \
           and selection[0][3] == selection[1][3] == selection[2][3] and selection[0][4] == selection[1][4] == selection[2][4])\
           or (selection[0][1] != selection[1][1] != selection[2][1] and selection[0][2] == selection[1][2] == selection[2][2] \
           and selection[0][3] == selection[1][3] == selection[2][3] and selection[0][4] != selection[1][4] != selection[2][4])\
           or (selection[0][1] != selection[1][1] != selection[2][1] and selection[0][2] == selection[1][2] == selection[2][2] \
           and selection[0][3] != selection[1][3] != selection[2][3] and selection[0][4] == selection[1][4] == selection[2][4])\
           or (selection[0][1] != selection[1][1] != selection[2][1] and selection[0][2] != selection[1][2] != selection[2][2] \
           and selection[0][3] == selection[1][3] == selection[2][3] and selection[0][4] == selection[1][4] == selection[2][4])\
           or (selection[0][1] == selection[1][1] == selection[2][1] and selection[0][2] != selection[1][2] != selection[2][2] \
           and selection[0][3] != selection[1][3] != selection[2][3] and selection[0][4] == selection[1][4] == selection[2][4])\
           or (selection[0][1] == selection[1][1] == selection[2][1] and selection[0][2] != selection[1][2] != selection[2][2] \
           and selection[0][3] == selection[1][3] == selection[2][3] and selection[0][4] != selection[1][4] != selection[2][4])\
           or (selection[0][1] == selection[1][1] == selection[2][1] and selection[0][2] == selection[1][2] == selection[2][2] \
           and selection[0][3] != selection[1][3] != selection[2][3] and selection[0][4] != selection[1][4] != selection[2][4])\
           or (selection[0][1] == selection[1][1] == selection[2][1] and selection[0][2] != selection[1][2] != selection[2][2] \
           and selection[0][3] != selection[1][3] != selection[2][3] and selection[0][4] != selection[1][4] != selection[2][4])\
           or (selection[0][1] != selection[1][1] != selection[2][1] and selection[0][2] == selection[1][2] == selection[2][2] \
           and selection[0][3] != selection[1][3] != selection[2][3] and selection[0][4] != selection[1][4] != selection[2][4])\
           or (selection[0][1] != selection[1][1] != selection[2][1] and selection[0][2] != selection[1][2] != selection[2][2] \
           and selection[0][3] == selection[1][3] == selection[2][3] and selection[0][4] != selection[1][4] != selection[2][4])\
           or (selection[0][1] != selection[1][1] != selection[2][1] and selection[0][2] != selection[1][2] != selection[2][2] \
           and selection[0][3] != selection[1][3] != selection[2][3] and selection[0][4] == selection[1][4] == selection[2][4])\
           or (selection[0][1] == selection[1][1] == selection[2][1] and selection[0][2] == selection[1][2] == selection[2][2] \
           and selection[0][3] == selection[1][3] == selection[2][3] and selection[0][4] == selection[1][4] == selection[2][4]):
            score += 1
            if c1s == True:
                sample[0] = random.randrange(81)                                #the global variable sample, a list, has it's first value changed
                image1 = pygame.image.load(CardList.cardsList[sample[0]][0])    #so that c1 can change while leaving the other cards the same
                image1 = pygame.transform.scale(image1, (60, 84))               #the new card is then blitted into the space
                c1 = image1                                                     #repeats for the next 11 cards
                screen.blit(c1, (210,210))
            if c2s == True:
                sample[1] = random.randrange(81)
                image2 = pygame.image.load(CardList.cardsList[sample[1]][0])
                image2 = pygame.transform.scale(image2, (60, 84))
                c2 = image2
                screen.blit(c2, (285,210))
            if c3s == True:
                sample[2] = random.randrange(81)
                image3 = pygame.image.load(CardList.cardsList[sample[2]][0])
                image3 = pygame.transform.scale(image3, (60, 84))
                c3 = image3
                screen.blit(c3, (360,210))
            if c4s == True:
                sample[3] = random.randrange(81)
                image4 = pygame.image.load(CardList.cardsList[sample[3]][0])
                image4 = pygame.transform.scale(image4, (60, 84))
                c4 = image4
                screen.blit(c4, (435,210))
            if c5s == True:
                sample[4] = random.randrange(81)
                image5 = pygame.image.load(CardList.cardsList[sample[4]][0])
                image5 = pygame.transform.scale(image5, (60, 84))
                c5 = image5
                screen.blit(c5, (210, 310))
            if c6s == True:
                sample[5] = random.randrange(81)
                image6 = pygame.image.load(CardList.cardsList[sample[5]][0])
                image6 = pygame.transform.scale(image6, (60, 84))
                c6 = image6
                screen.blit(c6, (285,310))
            if c7s == True:
                sample[6] = random.randrange(81)
                image7 = pygame.image.load(CardList.cardsList[sample[6]][0])
                image7 = pygame.transform.scale(image7, (60, 84))
                c7 = image7
                screen.blit(c7, (360,310))
            if c8s == True:
                sample[7] = random.randrange(81)
                image8 = pygame.image.load(CardList.cardsList[sample[7]][0])
                image8 = pygame.transform.scale(image8, (60, 84))
                c8 = image8
                screen.blit(c8, (435,310))
            if c9s == True:
                sample[8] = random.randrange(81)
                image9 = pygame.image.load(CardList.cardsList[sample[8]][0])
                image9 = pygame.transform.scale(image9, (60, 84))
                c9 = image9
                screen.blit(c9, (210,410))
            if c10s == True:
                sample[9] = random.randrange(81)
                image10 = pygame.image.load(CardList.cardsList[sample[9]][0])
                image10 = pygame.transform.scale(image10, (60, 84))
                c10 = image10
                screen.blit(c10, (285,410))
            if c11s == True:
                sample[10] = random.randrange(81)
                image11 = pygame.image.load(CardList.cardsList[sample[10]][0])
                image11 = pygame.transform.scale(image11, (60, 84))
                c11 = image11
                screen.blit(c11, (360,410))
            if c12s == True:
                sample[11] = random.randrange(81)
                image12 = pygame.image.load(CardList.cardsList[sample[11]][0])
                image12 = pygame.transform.scale(image12, (60, 84))
                c12 = image12
                screen.blit(c12, (435,410))
        else:
            screen.blit(c1, (210,210))      #draw new card
            screen.blit(c2, (285,210))      #draw new card
            screen.blit(c3, (360,210))      #draw new card
            screen.blit(c4, (435,210))      #draw new card
            screen.blit(c5, (210,310))      #draw new card
            screen.blit(c6, (285,310))      #draw new card
            screen.blit(c7, (360,310))      #draw new card
            screen.blit(c8, (435,310))      #draw new card
            screen.blit(c9, (210,410))      #draw new card
            screen.blit(c10, (285,410))     #draw new card
            screen.blit(c11, (360,410))     #draw new card
            screen.blit(c12, (435,410))     #draw new card

        selection = []
        c1s = False
        c2s = False
        c3s = False
        c4s = False
        c5s = False
        c6s = False
        c7s = False
        c8s = False
        c9s = False
        c10s = False
        c11s = False
        c12s = False
        pygame.display.update()

    for ev in pygame.event.get():

        if ev.type == QUIT: #if user exits, exit game
            running = False

        elif ev.type == MOUSEBUTTONDOWN:    #if mouse input
            x = ev.pos[0]                   #x position of mouse action
            y = ev.pos[1]                   #y position of mouse action

            if game == False:       #in menu mode
                if ev.button == 1:                                  #if left click:
                    if 278 <= x <= 405 and 390 <= y <= 437:         #   on the "play" button
                        background.fill((255,255,255))              #fill background white
                        screen.blit(background,(0,0))               #blit background
                        table = pygame.Surface(size2).convert()     #create black background for cards
                        table.fill((0, 0, 0))
                        screen.blit(table, (202, 202))
                        screen.blit(newSetImage, (289,530))

                        screen.blit(c1, (210,210))      #draw new card
                        screen.blit(c2, (285,210))      #draw new card
                        screen.blit(c3, (360,210))      #draw new card
                        screen.blit(c4, (435,210))      #draw new card
                        screen.blit(c5, (210,310))      #draw new card
                        screen.blit(c6, (285,310))      #draw new card
                        screen.blit(c7, (360,310))      #draw new card
                        screen.blit(c8, (435,310))      #draw new card
                        screen.blit(c9, (210,410))      #draw new card
                        screen.blit(c10, (285,410))     #draw new card
                        screen.blit(c11, (360,410))     #draw new card
                        screen.blit(c12, (435,410))     #draw new card

                        pygame.display.update()

                        #set beginning game time
                        t1 = time.time()
                        game = True #

                    elif 278 <= x <= 403 and 320 <= y <= 366:   #if instructions button is clicked
                        game = 3                                #set game = 3 for instructions page
                        screen.blit(background,(0,0))
                        
                        #font
                        myfont = pygame.font.SysFont('Comic Sans MS', 20)
                        
                        #instructions
                        label0 = myfont.render("Instructions:", 1, (0,0,0))
                        label1 = myfont.render("SET is a card game that has a total of 81 cards.", 1, (0,0,0))
                        label1_5 = myfont.render("Each card has four attributes:", 1, (0,0,0))
                        label2 = myfont.render("colour(red,blue,green), number(1,2,3),", 1,(0,0,0))
                        label2_25 = myfont.render("shape(diamond,rounded,squiggle),", 1, (0,0,0))
                        label2_5 = myfont.render("and shading(open,striped,solid).", 1, (0,0,0))
                        label3 = myfont.render("The dealer starts the game off by dealing 12 cards (3x4).", 1, (0,0,0))
                        label4 = myfont.render("When the player sees a set, he/she will click on the cards of that set.",1,(0,0,0))
                        label5 = myfont.render("1. All cards have the same number OR different numbers", 1, (0,0,0))
                        label6 = myfont.render("2. All cards have the same color OR different colours", 1, (0,0,0))
                        label7 = myfont.render("3. All cards have the same shape OR different shape", 1, (0,0,0))
                        label8 = myfont.render("4. All cards have the same shading OR different shading", 1, (0,0,0))
                        
                        #blitting instructions
                        screen.blit(label0,(0,0))
                        screen.blit(label1, (0,50))
                        screen.blit(label1_5,(0,100))
                        screen.blit(label2, (0,150))
                        screen.blit(label2_25, (0,200))
                        screen.blit(label2_5, (0,250))
                        screen.blit(label3, (0,350))
                        screen.blit(label4, (0,400))
                        screen.blit(label5, (0,450))
                        screen.blit(label6, (0,500))
                        screen.blit(label7, (0,550))
                        screen.blit(label8, (0,600))
                        
                        #show it all
                        pygame.display.update()

            elif game == 3:                             #if in instructions page
                if ev.button == 1:                      #and left click
                    if 0 <= x <= 720 and 0 <= y <= 720: #return to main menu
                        game = False

            elif game == True:                        #if in game mode
                if ev.button == 1:                  #if left click

                    if 210 <= x <= 275 and 210 <= y <= 301: #if clicked in this area
                        if c1c == False:                    #if c1c is False
                            screen.blit(cover, (210,210))   #a transparent cover is blitted onto the area so it can be seen as if the card is selected
                            pygame.display.update()
                            selected += 1
                            c1c = True
                        elif c1c == True:                   #if c1c is True
                            screen.blit(c1, (210,210))      #the the original card is blitted over so it seems as thought it's unselected
                            pygame.display.update()         #selected then decreases in value so it shows that one less card is selected
                            selected -= 1                   #repeat for the next 11 cards
                            c1c = False

                    elif 285 <= x <= 350 and 210 <= y <= 301:
                        if c2c == False:
                            screen.blit(cover, (285,210))
                            pygame.display.update()
                            selected += 1
                            c2c = True
                        elif c2c == True:
                            screen.blit(c2, (285,210))
                            pygame.display.update()
                            selected -= 1
                            c2c = False

                    elif 360 <= x <= 425 and 210 <= y <= 301:
                        if c3c == False:
                            screen.blit(cover, (360,210))
                            pygame.display.update()
                            selected += 1
                            c3c = True
                        elif c3c == True:
                            screen.blit(c3, (360,210))
                            pygame.display.update()
                            selected -= 1
                            c3c = False

                    elif 435 <= x <= 500 and 210 <= y <= 301:
                        if c4c == False:
                            screen.blit(cover, (435,210))
                            pygame.display.update()
                            selected += 1
                            c4c = True
                        elif c4c == True:
                            screen.blit(c4, (435,210))
                            pygame.display.update()
                            selected -= 1
                            c4c = False

                    elif 210 <= x <= 275 and 310 <= y <= 401:
                        screen.blit(cover, (210,310))
                        pygame.display.update()
                        if c5c == False:
                            selected += 1
                            c5c = True
                        elif c5c == True:
                            screen.blit(c5, (210,310))
                            pygame.display.update()
                            selected -= 1
                            c5c = False

                    elif 285 <= x <= 350 and 310 <= y <= 401:
                        screen.blit(cover, (285,310))
                        pygame.display.update()
                        if c6c == False:
                            selected += 1
                            c6c = True
                        elif c6c == True:
                            screen.blit(c6, (285,310))
                            pygame.display.update()
                            selected -= 1
                            c6c = False

                    elif 360 <= x <= 425 and 310 <= y <= 401:
                        screen.blit(cover, (360,310))
                        pygame.display.update()
                        if c7c == False:
                            selected += 1
                            c7c = True
                        elif c7c == True:
                            screen.blit(c7, (360,310))
                            pygame.display.update()
                            selected -= 1
                            c7c = False

                    elif 435 <= x <= 500 and 310 <= y <= 401:
                        screen.blit(cover, (435,310))
                        pygame.display.update()
                        if c8c == False:
                            selected += 1
                            c8c = True
                        elif c8c == True:
                            screen.blit(c8, (435,310))
                            pygame.display.update()
                            selected -= 1
                            c8c = False

                    elif 210 <= x <= 275 and 410 <= y <= 501:
                        screen.blit(cover, (210,410))
                        pygame.display.update()
                        if c9c == False:
                            selected += 1
                            c9c = True
                        elif c9c == True:
                            screen.blit(c9, (210,410))
                            pygame.display.update()
                            selected -= 1
                            c9c = False

                    elif 285 <= x <= 350 and 410 <= y <= 501:
                        screen.blit(cover, (285,410))
                        pygame.display.update()
                        if c10c == False:
                            selected += 1
                            c10c = True
                        elif c10c == True:
                            screen.blit(c10, (285,410))
                            pygame.display.update()
                            selected -= 1
                            c10c = False

                    elif 360 <= x <= 425 and 410 <= y <= 501:
                        screen.blit(cover, (360,410))
                        pygame.display.update()
                        if c11c == False:
                            selected += 1
                            c11c = True
                        elif c11c == True:
                            screen.blit(c11, (360,410))
                            pygame.display.update()
                            selected -= 1
                            c11c = False

                    elif 435 <= x <= 500 and 410 <= y <= 501:
                        screen.blit(cover, (435,410))
                        pygame.display.update()
                        if c12c == False:
                            selected += 1
                            c12c = True
                        elif c12c == True:
                            screen.blit(c12, (435,410))
                            pygame.display.update()
                            selected -= 1
                            c12c = False

                    elif 289 <= x <= 432 and 530 <= y <= 585: #if user clicks on "new set" button
                        #resets all the cards on the board
                        card1 = randomize_create_cards()
                        c1 = card1[0]
                        c2 = card1[1]
                        c3 = card1[2]
                        c4 = card1[3]
                        c5 = card1[4]
                        c6 = card1[5]
                        c7 = card1[6]
                        c8 = card1[7]
                        c9 = card1[8]
                        c10 = card1[9]
                        c11 = card1[10]
                        c12 = card1[11]

                        screen.blit(c1, (210,210))      #draw new card
                        screen.blit(c2, (285,210))      #draw new card
                        screen.blit(c3, (360,210))      #draw new card
                        screen.blit(c4, (435,210))      #draw new card
                        screen.blit(c5, (210,310))      #draw new card
                        screen.blit(c6, (285,310))      #draw new card
                        screen.blit(c7, (360,310))      #draw new card
                        screen.blit(c8, (435,310))      #draw new card
                        screen.blit(c9, (210,410))      #draw new card
                        screen.blit(c10, (285,410))     #draw new card
                        screen.blit(c11, (360,410))     #draw new card
                        screen.blit(c12, (435,410))     #draw new card
                        pygame.display.update()

                    elif 560 <= x <= 720 and 0 <= y <= 40:  #if user clicks on exit
                        game = False                        #exits game loop as now game is False and returns to the menu
                        
                        #resets the game
                        card1 = randomize_create_cards()
                        c1 = card1[0]
                        c2 = card1[1]
                        c3 = card1[2]
                        c4 = card1[3]
                        c5 = card1[4]
                        c6 = card1[5]
                        c7 = card1[6]
                        c8 = card1[7]
                        c9 = card1[8]
                        c10 = card1[9]
                        c11 = card1[10]
                        c12 = card1[11]

                        screen.blit(c1, (210,210))      #draw new card
                        screen.blit(c2, (285,210))      #draw new card
                        screen.blit(c3, (360,210))      #draw new card
                        screen.blit(c4, (435,210))      #draw new card
                        screen.blit(c5, (210,310))      #draw new card
                        screen.blit(c6, (285,310))      #draw new card
                        screen.blit(c7, (360,310))      #draw new card
                        screen.blit(c8, (435,310))      #draw new card
                        screen.blit(c9, (210,410))      #draw new card
                        screen.blit(c10, (285,410))     #draw new card
                        screen.blit(c11, (360,410))     #draw new card
                        screen.blit(c12, (435,410))     #draw new card

                        selected = 0
                        c1c = False
                        c2c = False
                        c3c = False
                        c4c = False
                        c5c = False
                        c6c = False
                        c7c = False
                        c8c = False
                        c9c = False
                        c10c = False
                        c11c = False
                        c12c = False

                        selection = []
                        c1s = False
                        c2s = False
                        c3s = False
                        c4s = False
                        c5s = False
                        c6s = False
                        c7s = False
                        c8s = False
                        c9s = False
                        c10s = False
                        c11s = False
                        c12s = False

                        score = 0

pygame.display.flip()   #update everything
pygame.display.quit()

