import turtle
myturtle = turtle.Turtle()
# ##### Setup Section #######

myturtle.speed(15)
intPetalsTotal = 9
intAngle = 360 // intPetalsTotal
intPetalsDrawn = 0
intDotSize = 25
intInnerDotsize = 10
# ##### END Setup Section #######

# ##### START Loop to Draw Petals #######
while (intPetalsDrawn < intPetalsTotal):
    myturtle.fillcolor("#ff3333")
    myturtle.begin_fill()
    # Draw a circle segment with a 200 radius, but only for 40 degrees
    myturtle.circle(200, 40)
    # Draw a circle segment with a radius of 10, for 140 degrees
    myturtle.circle(10, 140)
    # Repeat the two lines above, to complete
    # 360 degrees and end up back at the start.
    myturtle.circle(200, 40)
    myturtle.circle(10, 140)
    myturtle.end_fill()
    myturtle.right(intAngle)
    intPetalsDrawn += 1
# ##### END Loop to Draw Petals #######

##### START Drawing the center of the flower #######
myturtle.forward(intDotSize)
myturtle.left(90)
myturtle.fillcolor("#000000")
myturtle.begin_fill()
myturtle.circle(intDotSize)
myturtle.end_fill()
##### END Drawing the center of the flower #######

##### START Drawing the inner center of the flower #######
myturtle.right(90) # to shift direction to x axis
myturtle.backward(intDotSize - intInnerDotsize) # to centralize the inner circle
myturtle.left(90)
myturtle.fillcolor("#ffd11a")
myturtle.begin_fill()
myturtle.circle(intInnerDotsize)
myturtle.end_fill()
##### END Drawing the inner center of the flower #######

# Finish up
screen = turtle.Screen()
screen.exitonclick()