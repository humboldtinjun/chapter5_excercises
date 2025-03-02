# what does it this do? not i converted it to turtle
import turtle


def draw(length):
    angle = 30
    factor = 0.75

    if length > 5:
        turtle.forward(length)  # Move forward
        turtle.left(angle)  # Turn left
        draw(factor * length)  # First recursive call
        turtle.right(2 * angle)  # Turn right
        draw(factor * length)  # Second recursive call
        turtle.left(angle)  # Turn left to realign
        turtle.backward(length)  # Move back to starting position


# Set up the turtle
turtle.speed(5)  # Set to the fastest speed
turtle.left(90)  # Start facing upwards
turtle.up()  # Lift pen so no line is drawn
turtle.backward(100)  # Move down to give space
turtle.down()  # Put the pen down

# Call the function
draw(150)

# Finish the drawing
turtle.done()

# the base case stops when length <= 5, it moves forward by length,
# then turns left by 50deg and calls draw() with a smallr length,
# turns right by 2*50, calls draw() for the second branch, moves
# turtle back to the right direction and goes back to the starting
# position.  It draws a tree like branch thing. the two recursive
# calls create two branches making a tree

