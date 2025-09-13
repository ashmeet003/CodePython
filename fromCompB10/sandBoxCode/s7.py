# Ashmeet Kaur
# COMP B10
# Infinite Snowflakes
# The program intends to create a snowflake pattern and fill it one of the listed colors
# The program uses function to create one petal at a time.

import random
import turtle

myturtle = turtle.Turtle()
screen = turtle.Screen()
arColors = ["#A282D9", "#885FCE", "#5A31A0", "#371E63", "#1F1137"] # use of hex codes
xpixels = screen.window_width()//2
ypixels = screen.window_height()//2
myturtle.speed(150)

def makeArm(intScale):          # creates petal like formation
    myturtle.circle(intScale*50, 40)
    myturtle.left(120)
    myturtle.circle(intScale*50, 40)

while True:
    xColor = random.choice(arColors)            # chooses a random color from list
    myturtle.pencolor(xColor)
    myturtle.fillcolor(xColor)

    myturtle.penup()                            # places turtle at random location
    xloc = random.randint(-1*xpixels,xpixels)
    yloc = random.randint(-1*ypixels,ypixels)
    myturtle.goto(xloc,yloc)
    myturtle.pendown()

    intScale2 = random.randint(1,10)/5    # scale = length of a petal
    myturtle.begin_fill()
    for x in range(9):                          # creates 9 petals
        makeArm(intScale2)
    myturtle.end_fill()