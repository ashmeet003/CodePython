import random

def moveTurtle(t, x, y):

    t.penup()
    current_x, current_y = t.position()
    t.goto(current_x + x, current_y + y)
    t.pendown()

def draw_left_eye(t):
    style = random.choice([1, 2, 3])

    if style == 1:
        t.circle(10)  # Simple circle
    elif style == 2:
        t.fillcolor('black')
        t.begin_fill()
        t.circle(10)
        t.end_fill()
    elif style == 3:
        for _ in range(6):  # Star-like eye
            t.forward(10)
            t.backward(10)
            t.left(60)
    t.hideturtle()


def draw_right_eye(t):
    style = random.choice([1, 2, 3])

    if style == 1:
        t.circle(10)  # Simple circle
    elif style == 2:
        t.fillcolor('blue')
        t.begin_fill()
        t.circle(10)
        t.end_fill()
    elif style == 3:
        t.dot(20, 'green')  # Large dot
    t.hideturtle()


def draw_nose(t):
    style = random.choice([1, 2, 3])

    if style == 1:
        t.right(90)
        t.forward(20)
        t.right(135)
        t.forward(28)
    elif style == 2:
        t.left(45)
        t.forward(30)
        t.right(90)
        t.forward(15)
    elif style == 3:
        t.left(90)
        t.forward(20)
        t.circle(10, 180)
    t.hideturtle()


def draw_mouth(t):
    style = random.choice([1, 2, 3])

    if style == 1:
        t.circle(20, 90)  # Partial circle for a smile
    elif style == 2:
        t.right(90)
        t.forward(30)
        t.left(180)
        t.forward(60)
    elif style == 3:
        t.circle(20, -90)  # Frown
    t.hideturtle()


def draw_left_ear(t):
    style = random.choice([1, 2])

    if style == 1:
        t.circle(10, 180)  # Semi-circle
    elif style == 2:
        t.left(90)
        t.forward(20)
        t.right(180)
        t.forward(40)
    t.hideturtle()


def draw_right_ear(t):
    style = random.choice([1, 2])

    if style == 1:
        t.circle(-10, 180)  # Semi-circle mirrored
    elif style == 2:
        t.right(90)
        t.forward(20)
        t.left(180)
        t.forward(40)
    t.hideturtle()

def draw_hair(t):
    style = random.choice([1, 2])
    t.setheading(0)
    if style == 1:
        t.right(60)
        for i in range(10):
            t.forward(25)
            t.left(120)
            t.forward(25)
            t.right(120)
    if style == 2:
        for i in range(25):
            t.right(30)
            t.circle(-20, 100)
            moveTurtle(t, 2, 30)
            t.setheading(0)
    t.hideturtle()


