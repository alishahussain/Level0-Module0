import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('pink')

    # This code makes a new Turtle. Pick a new name for the turtle
    srinivas = turtle.Turtle()

    # Make your turtle's shape 'turtle', .shape('turtle')
    srinivas.shape('turtle')
    # Set your turtle's speed using .speed(2)
    srinivas.speed(50)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    srinivas.color('green')
    srinivas.pencolor('blue')
    # Move your turtle forward using .forward(100)
    # TEST    Did your turtle move forward?
    srinivas.forward(100)
    # Move your turtle left or right using .left(90) or .right(90)
    srinivas.right(90)
    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?
    for turn in range(40):
        srinivas.forward(100)
        srinivas.right(100)
    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
    srinivas.penup()
    srinivas.goto(-100,0)
    srinivas.pendown()
    # Have your turtle draw a circle using .circle(radius, steps=30)
    srinivas.color("blue")
    srinivas.begin_fill()
    srinivas.circle(50, steps=100)
    # TEST    Did your turtle draw a circle?

    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below
    srinivas.end_fill()
    # Draw 3 more shapes with different fill colors!
    srinivas.penup()
    srinivas.goto(-300,300)
    srinivas.pendown()
    srinivas.color("green")
    srinivas.begin_fill()
    for turn in range(5):
        srinivas.forward(100)
        srinivas.right(72)
    srinivas.end_fill()
    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
