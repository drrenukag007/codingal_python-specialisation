
import pygame
import random
import sys
pygame.init()
screen_width=500
screen_height=500
window=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Pygame circles usimg mouse events")
window.fill("lightpink") #adds background color

#display one circle (window)
x=random.randint(60,500)
y=random.randint(60,500)
#pygame.draw.circle(window,"darkred",(255,255),60,5)3
#pygame.draw.circle(window,"darkred",(x,y),40,10)


class Circle():
    def __init__(self,color,position,radius,width):
        self.color=color
        self.position=position
        self.radius=radius
        self.width=width

    def draw(self):
        pygame.draw.circle(window,self.color,self.position,self.radius,self.width)

    def grow(self,x):
        self.radius=self.radius+x
        pygame.draw.circle(window,self.color,self.position,self.radius,self.width)




redCircle=Circle("red",(200,200),30,3)
orangeCirlce=Circle("orange",(255,255),30,6)
blueCirlce=Circle("blue",(300,300),30,9)






  #TEMPLATE - THIS CODE HAS TO BE HERE
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            orangeCirlce.draw()
            redCircle.draw()
            blueCirlce.draw()
            pygame.display.update()

        elif event.type==pygame.MOUSEBUTTONUP:
            orangeCirlce.grow(3)
            redCircle.grow(6)
            blueCirlce.grow(9)
            pygame.display.update()

        elif event.type==pygame.MOUSEMOTION:
            pos=pygame.mouse.get_pos()
            white=Circle("white",pos,6,1)
            white.draw()



    pygame.display.update() #PUT INSIDE WHILE LOOP FOR MORE EFFICIENT!!!
