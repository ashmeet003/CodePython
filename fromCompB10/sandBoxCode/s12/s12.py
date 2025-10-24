import turtle

def execute_turtle_commands(filename):
    t = turtle.Turtle()
    screen = turtle.Screen()

    try:
        with open(filename, 'r') as file:
            for line in file:
                # Split each line into command and value
                parts = line.strip().split()
                command = parts[0]
                value = int(parts[1])

                # Execute the command
                if command == "fd":
                    t.forward(value)
                elif command == "rt":
                    t.right(value)
                elif command == "lt":
                    t.left(value)
                elif command == "circle":
                    t.circle(value)
                else:
                    print(f"Unknown command: {command}")
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

    # Click on screen to close the window
    screen.exitonclick()

# Example usage
execute_turtle_commands("triangle.txt")