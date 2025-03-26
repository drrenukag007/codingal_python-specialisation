import turtle
pen=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor("black")

def drawacircle(size,color):
    pen.color(color)
    pen.circle(size)



drawacircle(68,"yellow")
drawacircle(32,"purple")
drawacircle(74,"blue")





screen.mainloop()