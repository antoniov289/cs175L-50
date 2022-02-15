#Antonio Vinagre
#CS 175L-50
#stopsign.py

import math
import turtle

#named constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
LENGTH2 = 90
ANGLE = 45
TEXT_X = -65
TEXT_Y = -30

turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)

s = LENGTH
x = s / math.sqrt(2)
diameter = s + (2 * x)

s2 = LENGTH
2
x2 = s2 / math.sqrt(2)
diameter2 = s2 + (2 * x2)

turtle.hideturtle()
turtle.penup()
turtle.goto(-1*LENGTH/2, diameter/2)
turtle.pendown()

turtle.pen(pencolor = "red", pensize = 5, fillcolor="white")

turtle.begin_fill()
for x in range(8):
    turtle.forward(LENGTH)
    turtle.right(ANGLE)
turtle.end_fill()

turtle.penup()
turtle.goto(-1*(LENGTH2)/2, ((diameter2)/2)-12)
turtle.pendown()
turtle.pen(pencolor = "black", pensize = 1, fillcolor="red")

turtle.begin_fill()
for x in range(8):
    turtle.forward(LENGTH2)
    turtle.right(ANGLE)
turtle.end_fill()

turtle.pen(pencolor="white")
turtle.penup()
turtle.goto(TEXT_X, TEXT_Y)
turtle.pendown()
turtle.write("STOP", font = ("Ariel", 50, "bold"))
