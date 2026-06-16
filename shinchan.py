import turtle
import math

screen = turtle.Screen()
screen.title("Shinchan - Turtle Graphics")
screen.bgcolor("white")
screen.setup(width=800, height=700)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def draw_filled_circle(t, x, y, radius, color):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.fillcolor(color)
    t.pencolor("black")
    t.pensize(2)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_circle_outline(t, x, y, radius, pen_color="black", pen_size=2):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.pencolor(pen_color)
    t.pensize(pen_size)
    t.circle(radius)

def goto_draw(t, points, fill_color=None, pen_color="black", pen_size=2, close=True):
    t.penup()
    t.goto(points[0])
    t.pendown()
    t.pencolor(pen_color)
    t.pensize(pen_size)
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for p in points[1:]:
        t.goto(p)
    if close:
        t.goto(points[0])
    if fill_color:
        t.end_fill()

# ─── HEAD ───
draw_filled_circle(t, 0, 100, 90, "#F5C518")

# ─── EYES (whites) ───
draw_filled_circle(t, -28, 155, 20, "white")
draw_filled_circle(t,  28, 155, 20, "white")

# ─── PUPILS ───
draw_filled_circle(t, -24, 148, 10, "black")
draw_filled_circle(t,  32, 148, 10, "black")

# ─── EYE SHINE ───
draw_filled_circle(t, -20, 152, 4, "white")
draw_filled_circle(t,  36, 152, 4, "white")

# ─── EYEBROWS ───
t.penup(); t.goto(-48, 178); t.pendown()
t.pensize(4); t.pencolor("black")
t.goto(-8, 182)

t.penup(); t.goto(8, 182); t.pendown()
t.goto(48, 178)

# ─── NOSE ───
draw_filled_circle(t, 0, 128, 12, "#E8A000")

# ─── NOSTRILS ───
draw_filled_circle(t, -5, 124, 3, "black")
draw_filled_circle(t,  5, 124, 3, "black")

# ─── MOUTH (wide open grin) ───
t.penup(); t.goto(-40, 108); t.pendown()
t.pensize(3); t.pencolor("black")
t.fillcolor("#CC2200")
t.begin_fill()
t.goto(40, 108)
t.goto(50, 95)
for angle in range(0, -181, -5):
    rx = 50 * math.cos(math.radians(angle))
    ry = 18 * math.sin(math.radians(angle))
    t.goto(rx, 87 + ry)
t.goto(-50, 95)
t.goto(-40, 108)
t.end_fill()

# ─── TEETH ───
goto_draw(t, [(-30, 108), (-10, 108), (-10, 96), (-30, 96)], fill_color="white", close=True)
goto_draw(t, [(-10, 108), (10, 108), (10, 96), (-10, 96)], fill_color="white", close=True)
goto_draw(t, [(10, 108), (30, 108), (30, 96), (10, 96)], fill_color="white", close=True)

# ─── EARS ───
draw_filled_circle(t, -90, 140, 18, "#F5C518")
draw_filled_circle(t,  90, 140, 18, "#F5C518")

# ─── HAIR (two tufts) ───
goto_draw(t, [(-25, 185), (-45, 225), (-15, 200)], fill_color="black")
goto_draw(t, [(25, 185), (45, 225), (15, 200)], fill_color="black")

# ─── NECK ───
goto_draw(t, [(-20, 12), (20, 12), (25, -20), (-25, -20)], fill_color="#F5C518")

# ─── BODY (red shirt) ───
goto_draw(t,
    [(-70, -20), (70, -20), (85, -140), (60, -155),
     (0, -145), (-60, -155), (-85, -140)],
    fill_color="#CC0000")

# ─── SHIRT COLLAR ───
goto_draw(t, [(-20, -20), (0, -45), (20, -20)], fill_color="white")

# ─── YELLOW STRIPE ON SHIRT ───
goto_draw(t, [(-68, -80), (68, -80), (70, -95), (-70, -95)], fill_color="#F5C518")

# ─── LEFT ARM ───
goto_draw(t,
    [(-70, -25), (-95, -30), (-115, -90), (-90, -110), (-65, -70), (-65, -60)],
    fill_color="#CC0000")
# left hand
draw_filled_circle(t, -105, -118, 16, "#F5C518")

# ─── RIGHT ARM ───
goto_draw(t,
    [(70, -25), (95, -30), (115, -90), (90, -110), (65, -70), (65, -60)],
    fill_color="#CC0000")
# right hand
draw_filled_circle(t, 105, -118, 16, "#F5C518")

# ─── PANTS (black) ───
goto_draw(t,
    [(-85, -140), (-85, -210), (-15, -210), (-15, -155),
     (15, -155), (15, -210), (85, -210), (85, -140),
     (60, -155), (0, -145), (-60, -155)],
    fill_color="black")

# ─── SHOES ───
# left shoe
goto_draw(t, [(-85, -210), (-85, -230), (-50, -240), (-10, -235), (-10, -210)], fill_color="#222222")
# right shoe
goto_draw(t, [(85, -210), (85, -230), (50, -240), (10, -235), (10, -210)], fill_color="#222222")

# ─── ROSY CHEEKS ───
t.penup(); t.goto(-65, 133); t.pendown()
t.pencolor("#F5C518"); t.fillcolor("#FFAAAA")
t.begin_fill(); t.circle(14); t.end_fill()

t.penup(); t.goto(51, 133); t.pendown()
t.fillcolor("#FFAAAA")
t.begin_fill(); t.circle(14); t.end_fill()

turtle.done()