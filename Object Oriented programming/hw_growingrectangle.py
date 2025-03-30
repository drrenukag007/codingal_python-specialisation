import pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
screen.fill("white")
#pygame.display.update()

class myRectangle():
    def __init__(self, color, pos, width, height):
        self.color = color
        self.pos = pos
        self.width = width
        self.height = height
        self.scrn = screen

    def draw(self):
        pygame.draw.rect(self.scrn, self.color, (*self.pos, self.width, self.height))

    def grow(self, x, y):
        self.width += x
        self.height += y
        pygame.draw.rect(self.scrn, self.color, (*self.pos, self.width, self.height))

r = myRectangle("blue", (100, 100), 100, 50)


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill("white")
            r.draw()
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            screen.fill("white")
            r.grow(4,2)
            pygame.display.update()
        elif event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            r2 = myRectangle("red", pos,10,5)               
            r2.draw()
            pygame.display.update()
        if event.type == pygame.QUIT:
            run = False
          
    