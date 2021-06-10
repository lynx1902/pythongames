import pygame                                                                    #using Pygame to design GUI
import numpy as np                                                               #using Numpy to draw the grid
import sys                                                                       #using sys to exit the window
import math                                                                      #using math to perform mathematical task
pygame.init()                                                                    #Initialising Pygame


player1=input("Enter the name of Player 1:\n")                                     #Name of First player                
player2=input("Enter the name of Player 2:\n")                                     #Name of second player

rowno=int(input("Enter the number of rows (1 to 7):\n"))                          #Numbers of rows can be given till 7
colno=int(input("Enter the number of columns (1 to 7):\n"))                       #Numbers of columns can be given till 7


#pygame
sqa=100                                                                           
rad=int(sqa/2-5)                                                                 #radius of circle

#Colors
black=(0,0,0)
red=(255,0,0)
yellow=(255,255,0)


def gameboard():                                                                 #Function to create a board using numpy 
    playboard=np.zeros((rowno,colno))
    return playboard

def putpiece(playboard,row,select,piece):                                        #Function to drop a piece inside a board
    playboard[row][select]=piece

def availableloc(playboard,select):                                              #Function to check whether the location on board is filled or not
    return playboard[rowno-1][select]==0


def opennextrow(playboard,select):                                              #Function to open a new row 
    for r in range(rowno):
        if playboard[r][select]==0:
            return r

def flipboard(playboard):                                                        #Function to flip the board as the pieces should occupy the lower rows
   print(np.flip(playboard,0))                                                   #Rotation the board


def checkwin(playboard,piece):                                                   #Checking the winning conditions
    for c in range(colno-3):
        for r in range(rowno):
            if playboard[r][c]==piece and playboard[r][c+1]==piece and playboard[r][c+2]==piece and playboard[r][c+3]==piece:
                return True

    for c in range(colno-3):
        for r in range(rowno):
            if playboard[r][c]==piece and playboard[r+1][c]==piece and playboard[r+2][c]==piece and playboard[r+3][c]==piece:
                return True
    for c in range(colno-3):
        for r in range(rowno-3):
            if playboard[r][c]==piece and playboard[r+1][c+1]==piece and playboard[r+2][c+2]==piece and playboard[r+3][c+3]==piece:
                return True

    for c in range(colno-3):
        for r in range(3,rowno):
            if playboard[r][c]==piece and playboard[r-1][c+1]==piece and playboard[r-2][c+2]==piece and playboard[r-3][c+3]==piece:
                return True


 #Pygame               
def drawplayboard(playboard):                                                       #using pygame to draw the board
    for c in range(colno):
        for r in range(rowno):
            pygame.draw.rect(gamewindow,(0,0,255),(c*sqa,r*sqa+sqa,sqa,sqa))        #To draw a blue rectangle
            pygame.draw.circle(gamewindow,black,(int(c*sqa+sqa/2),int(r*sqa+sqa+sqa/2)),rad)        #To draw circles all over the board of equal diameter
            

    for c in range(colno):
        for r in range(rowno):
            if playboard[r][c]==1:
                    pygame.draw.circle(gamewindow,red,(int(c*sqa+sqa/2),screenh-int(r*sqa+sqa/2)),rad)
            elif playboard[r][c]==2:
                    pygame.draw.circle(gamewindow,yellow,(int(c*sqa+sqa/2),screenh-int(r*sqa+sqa/2)),rad)    
    pygame.display.update()                                                                             

playboard=gameboard()               
flipboard(playboard)
sqa=100
rad=int(sqa/2-5)


tofplayer=0                                                                    #TO ensure the alternate moves of Player1 and Player2
running=True                                                                   #Game running condition

screenw=colno*sqa                                                              #Screen width
screenh=(rowno+1)*sqa                                                          #Screen height

gamewindow=pygame.display.set_mode((screenw,screenh))                          #Initializing Game window
pygame.display.set_caption('Connect 4 Team:-404')                              #Caption on the window

drawplayboard(playboard)                                    
pygame.display.update()                                                        #Updating the display
font=pygame.font.SysFont("monospace",25)                                       #Selecting font to display on screen

while running:                                                                 #running=True


    for event in pygame.event.get():                                           #To set events such as exit,play etc
        if event.type==pygame.QUIT:
            sys.exit()                                                         #To exit the game
        

        if event.type==pygame.MOUSEMOTION:                                     #To hover the piece over the black window
            pygame.draw.rect(gamewindow,black,(0,0,screenw,sqa))               #To draw a black scrren the blue window
            xcor=event.pos[0]                                                  #To hold pieces
            if tofplayer==0:                                                   
                pygame.draw.circle(gamewindow,red,(xcor,int(sqa/2)),rad)       #To draw a circle on a board of red color
            else:
                pygame.draw.circle(gamewindow,yellow,(xcor,int(sqa/2)),rad)    #To draw a circle on a board of yellow color

        pygame.display.update()                                                #To update the display

        if event.type==pygame.MOUSEBUTTONDOWN:                                  #If mouse button is released
            pygame.draw.rect(gamewindow,black,(0,0,screenw,sqa))
            if tofplayer==0:
                xcor=event.pos[0]
                select=int(math.floor(xcor/sqa))                                #to select the column

                # select=int(input("Player 1 can select from (0,6)"))
                # print(select)


                if availableloc(playboard,select):                              #To check whether the selected location is empty or not
                    row=opennextrow(playboard, select)
                    putpiece(playboard,row,select,1)                            

                    if checkwin(playboard,1):                                   #TO check the winning condition
                        screentext=font.render(f"Congratulations {player1} ! you won",1,red)        #If player ! wins
                        gamewindow.blit(screentext,(20,30))                     #To display the text on screen

                        print("Player 1 wins")
						
                        running=False                                           #To exit the game loop ,if player 1 wins
                    




            else:                                                                   #Condition for 2nd player
                xcor=event.pos[0]
                select=int(math.floor(xcor/sqa))                                    #To select the column

                # select=int(input("Player 2 can select from (0,6)"))
                print(select)

                if availableloc(playboard,select):
                    row=opennextrow(playboard, select)
                    putpiece(playboard,row,select,2)

                    if checkwin(playboard,2):
                        screentext=font.render(f"Congratulations {player2} ! you won",1,yellow)
                        gamewindow.blit(screentext,(20,20))
						
                        
                        running=False
                    
            flipboard(playboard)                        #Calling flipboard function
            drawplayboard(playboard)                    #calling draw board function
            tofplayer+=1                                #Alternating player's turn
            tofplayer=tofplayer%2
            
            if not running:                             #If the game is not running
                pygame.time.wait(5000)                  #It will display the game window for 5 seconds after the game over 








            

            
