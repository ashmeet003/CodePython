#Ashmeet Kaur
# CompB10 Fall 2025
# the program intends to use modules to call function from
# picasso file and implement in s11 file
import picasso as p
import turtle

t = turtle.Turtle()
p.draw_nose(t)
p.moveTurtle(t,-50,50)
p.draw_left_eye(t)
p.moveTurtle(t,100,0)
p.draw_right_eye(t)

# pen lift -> draw mouth
p.moveTurtle(t,-40,-100)
p.draw_mouth(t)

# pen lift -> draw left ear
p.moveTurtle(t,-120,60)
p.draw_left_ear(t)

# pen lift -> draw right ear
p.moveTurtle(t,200,10)
p.draw_right_ear(t)

# pen lift -> draw hair
p.moveTurtle(t,-220,60)
p.draw_hair(t)

turtle.done()