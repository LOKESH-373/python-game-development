import turtle

screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Cartoon Character")

pen = turtle.Turtle()
pen.speed(5)

def draw_circle(color, x, y, radius):
    pen.penup()
    pen.goto(x, y - radius)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

# Head
draw_circle("peachpuff", 0, 50, 80)

# Eyes
draw_circle("white", -30, 80, 20)
draw_circle("white", 30, 80, 20)
draw_circle("black", -30, 80, 10)
draw_circle("black", 30, 80, 10)

# Smile
pen.penup()
pen.goto(-40, 40)
pen.pendown()
pen.setheading(-60)
pen.circle(40, 120)

# Body
draw_circle("orange", 0, -120, 100)

# Belt
draw_circle("brown", 0, -120, 20)

pen.hideturtle()
turtle.done()
