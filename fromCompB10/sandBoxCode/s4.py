#Ashmeet Kaur
# CompB10

import turtle
myTurtle = turtle.Turtle()

intLen = 100                # measures length of each side
intSides = 8                # number of sides
intAngle = 360 / intSides   # angle formed by 2 sides

# following works to fill in a shape made using for loop
turtle.begin_fill()
for x in range(intSides):
    turtle.forward(intLen)
    turtle.right(intAngle)
turtle.end_fill()

screen = turtle.Screen()
screen.exitonclick()