# Ashmeet Kaur
# CompB10 FALL2025
# recursive tree
# program aims to create a tree using recursion and draw leaves(dots) at end of each node
import turtle, random

# User-definable variables
initial_length = 100  # Initial length of the branch
angle = 65            # Angle of the branching
decrease_factor = 0.70 # Factor by which branch length decreases

def draw_branch(turtle, branch_length):
    if branch_length > 5:
        turtle.pensize(branch_length/10)
        turtle.pencolor("sienna")
        # Draw the branch
        turtle.forward(branch_length)
        # Right branch
        turtle.right(angle)
        draw_branch(turtle, branch_length * decrease_factor)
        # Left branch
        turtle.left(2 * angle)
        draw_branch(turtle, branch_length * decrease_factor)
        # Return to base position
        turtle.right(angle)
        turtle.backward(branch_length)
    else:
        colors = ["#163806", "#2A6E0A", "#6BD138", "#99D138", "#C7D138", "#3B780C"]
        randomColor = random.choice(colors)
        turtle.dot(random.randint(5, 12),randomColor)

# Set up the turtle
screen = turtle.Screen()
my_turtle = turtle.Turtle()
my_turtle.left(90)  # Point the turtle upwards
my_turtle.up()
my_turtle.backward(100)
my_turtle.down()
my_turtle.speed(100)
# Draw the fractal tree
draw_branch(my_turtle, initial_length)

# Close the window on click
screen.exitonclick()