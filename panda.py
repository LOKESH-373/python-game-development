import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Turtle Panda")

# Create the turtle
panda = turtle.Turtle()
panda.speed(5)

# Function to draw a circle
def draw_circle(color, x, y, radius):
    panda.penup()
    panda.goto(x, y - radius)
    panda.pendown()
    panda.fillcolor(color)
    panda.begin_fill()
    panda.circle(radius)
    panda.end_fill()

# Panda face
draw_circle("black", 0, -50, 100)   # head
draw_circle("white", 0, -50, 90)    # face

# Panda ears
draw_circle("black", -70, 100, 40)
draw_circle("black", 70, 100, 40)

# Panda eyes
draw_circle("black", -40, 40, 30)
draw_circle("black", 40, 40, 30)
draw_circle("white", -40, 40, 15)
draw_circle("white", 40, 40, 15)

# Panda nose
draw_circle("black", 0, -20, 15)

# Panda mouth
panda.penup()
panda.goto(-20, -40)
panda.pendown()
panda.setheading(-60)
panda.circle(20, 120)

# Hide turtle
panda.hideturtle()

# Keep window open
turtle.done()
