import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
screen.fill("white")

class Rectangle():
    def __init__(self, color, pos, width, height):
        self.rect_color = color
        self.pos = pos
        self.width = width
        self.height = height
        self.rect_surface = screen

    def draw(self):
        pygame.draw.rect(self.rect_surface, self.rect_color, (self.pos[0], self.pos[1], self.width, self.height))

    def grow(self, x, y):
        self.width += x
        self.height += y
        self.draw()

r = Rectangle("green", (100, 100), 100, 50)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill("white")
            r.draw()

        elif event.type == pygame.MOUSEBUTTONUP:
            screen.fill("white")
            r.grow(4, 2)

        elif event.type == pygame.MOUSEMOTION:
            screen.fill("white")  # Clear the screen to avoid leaving trails
            r.draw()  # Redraw the original rectangle
            pos = pygame.mouse.get_pos()
            r2 = Rectangle("red", (pos[0], pos[1]), 10, 5)
            r2.draw()

    pygame.display.update()

pygame.quit()
