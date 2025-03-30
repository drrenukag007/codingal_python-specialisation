import pygame
import sys
pygame.init()
WIDTH=500
HEIGHT=500
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.update()
pygame.display.set_caption("Pygame Rectangles")

#rectangle
#pygame.draw.rect(screen,"red",(50,200,300,200)) #filled rectangle
#pygame.draw.rect(screen,"blue",(0,0,300,200),5,15,50,60,40) #width + border radius included
#bottom right, top left, top right , bottom left = ORDER FOR BORDER RADIUS IF DONE SEPERATELY

class Rectangle():
    def __init__(self,color,dimensions,width,radius):
        self.color=color
        self.dimensions=dimensions
        self.width=width
        self.radius=radius

    def display(self):
        pygame.draw.rect(screen,self.color,self.dimensions,self.width,self.radius)

whiteRect=Rectangle('white',(0,0,20,15),2,5)
greyRect=Rectangle('grey',(20,20,40,35),4,10)
pinkRect=Rectangle('pink',(40,40,80,75),6,15)
yellowRect=Rectangle('yellow',(60,60,120,115),8,20)
orangeRect=Rectangle('orange',(80,80,160,155),10,25)
redRect=Rectangle('red',(100,100,200,195),12,30)
purpleRect=Rectangle('purple',(120,120,240,235),14,35)
blueRect=Rectangle('blue',(140,140,280,275),16,40)
greenRect=Rectangle('green',(160,160,320,315),18,45)
brownRect=Rectangle('brown',(180,180,360,355),20,50)
whiteRect.display()
greyRect.display()
pinkRect.display()
yellowRect.display()
orangeRect.display()
redRect.display()
purpleRect.display()
blueRect.display()
greenRect.display()
brownRect.display()
pygame.display.update()





pygame.display.update() #everything displayed in layers, always perform update function to draw

#cumpulsory code for every game
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
