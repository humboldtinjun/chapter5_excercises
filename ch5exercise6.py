# the koch curve
# it breaks the line into 4 parts, turns left 60, right 120 the left 60
# it repeats this until the line is too short
import turtle
def koch(x):
    if x < 5: #base case, if too small draw a straight line
        turtle.forward(x)
    else:
        koch(x/3) # first segment
        turtle.left(60)
        koch(x / 3)
        turtle.right(120)
        koch(x / 3)
        turtle.left(60)
        koch(x / 3)

turtle.speed(3)
turtle.up() #lift the pen
turtle.goto(-200, 0) #starting point
turtle.down() #put the pen down

koch(100)

turtle.exitonclick()

### the function repeatedly divides the line into smaller parts,
### making a fractal shape and the base case stops it form infinite
### loops