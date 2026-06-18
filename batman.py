import turtle

def draw_batman_logo():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Batman Logo")
    screen.setup(800, 600)

    t = turtle.Turtle()
    t.speed(0)
    t.color("yellow")
    t.pensize(2)

    # --- Draw main ellipse (body of logo) ---
    t.penup()
    t.goto(0, -60)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(90, 360)
    t.end_fill()

    # --- Draw black bat shape on top ---
    t.penup()
    t.goto(0, -60)
    t.pendown()
    t.color("black")
    t.fillcolor("black")
    t.begin_fill()

    # Left wing
    t.goto(-30, 0)
    t.goto(-80, 60)
    t.goto(-120, 90)
    t.goto(-160, 70)
    t.goto(-130, 30)
    t.goto(-90, 10)
    t.goto(-60, -20)

    # Bottom left curve (body)
    t.goto(-40, -55)
    t.goto(-20, -70)

    # Center dip
    t.goto(0, -50)
    t.goto(20, -70)
    t.goto(40, -55)

    # Bottom right
    t.goto(60, -20)
    t.goto(90, 10)
    t.goto(130, 30)
    t.goto(160, 70)
    t.goto(120, 90)
    t.goto(80, 60)
    t.goto(30, 0)

    # Right wing tip and back to center
    t.goto(0, -60)

    t.end_fill()

    # --- Bat ears (pointed triangles at top of wings) ---
    t.penup()
    t.goto(-80, 60)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.goto(-120, 110)
    t.goto(-100, 60)
    t.end_fill()

    t.penup()
    t.goto(80, 60)
    t.pendown()
    t.begin_fill()
    t.goto(120, 110)
    t.goto(100, 60)
    t.end_fill()

    # --- Bat head (center raised bump) ---
    t.penup()
    t.goto(-30, 20)
    t.pendown()
    t.begin_fill()
    t.goto(-15, 50)
    t.goto(0, 60)
    t.goto(15, 50)
    t.goto(30, 20)
    t.goto(0, 10)
    t.goto(-30, 20)
    t.end_fill()

    t.hideturtle()
    screen.mainloop()

draw_batman_logo()