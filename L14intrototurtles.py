import turtle
#drawing a square
pen=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor("purple")
pen.color("green")
pen.forward(200)
pen.left(90)
pen.forward(200)
pen.left(90)
pen.forward(200)
pen.left(90)
pen.forward(200)

#circle
pen.up()
pen.goto(-100,-120)
pen.down()
pen.circle(100)

#square
pen.up()
pen.goto(-150,90)
pen.down()
for i in range(4):
   pen.forward(100)
   pen.right(90)









screen.mainloop()