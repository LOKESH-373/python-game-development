import turtle
import math

screen = turtle.Screen()
screen.bgcolor("#0a0a1a")
screen.title("Naruto Uzumaki")
screen.setup(700, 800)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def goto(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def filled_circle(x, y, r, color, outline=None, pw=1):
    goto(x, y - r)
    t.fillcolor(color)
    t.pencolor(outline if outline else color)
    t.pensize(pw)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

def filled_ellipse(x, y, rx, ry, color, outline=None, steps=60, pw=1):
    t.fillcolor(color)
    t.pencolor(outline if outline else color)
    t.pensize(pw)
    t.begin_fill()
    goto(x + rx, y)
    t.pendown()
    for i in range(steps + 1):
        angle = 2 * math.pi * i / steps
        t.goto(x + rx * math.cos(angle), y + ry * math.sin(angle))
    t.end_fill()

def draw_polygon(points, fill_color, outline_color=None, size=1):
    t.fillcolor(fill_color)
    t.pencolor(outline_color if outline_color else fill_color)
    t.pensize(size)
    t.begin_fill()
    goto(points[0][0], points[0][1])
    for p in points[1:]:
        t.goto(p[0], p[1])
    t.goto(points[0][0], points[0][1])
    t.end_fill()

def arc(x, y, r, start_deg, end_deg, color, pw=2):
    t.pencolor(color)
    t.pensize(pw)
    t.penup()
    steps = abs(end_deg - start_deg)
    for i in range(steps + 1):
        angle = math.radians(start_deg + i * (end_deg - start_deg) / steps)
        px = x + r * math.cos(angle)
        py = y + r * math.sin(angle)
        if i == 0:
            t.goto(px, py)
            t.pendown()
        else:
            t.goto(px, py)
    t.penup()

# ── Colors ──
SKIN       = "#f5c8a0"
DARK_SKIN  = "#d9a070"
SHADOW     = "#c08050"
BLONDE     = "#f0c020"
DARK_BLOND = "#c8960a"
ORANGE     = "#e85500"
DARK_ORNG  = "#b03c00"
BLACK      = "#111111"
WHITE      = "#ffffff"
BLUE_EYE   = "#3a7acc"
DARK_BLUE  = "#1a4a99"
RED_MARK   = "#cc1a00"
HEADBAND   = "#2a2a6a"
METAL      = "#c8c850"
LEAF_G     = "#2a6a2a"
SCROLL_WHT = "#eeeedd"
RED_SPIRAL = "#cc2200"

# ══════════════════════════════════════════
#  BODY
# ══════════════════════════════════════════

# Torso — orange jacket
draw_polygon(
    [(-110,-300),(110,-300),(120,-130),(-120,-130)],
    ORANGE, DARK_ORNG, 2
)
# Zipper / front line
goto(0,-130); t.pencolor(DARK_ORNG); t.pensize(2); t.pendown(); t.goto(0,-300); t.penup()
# Jacket collar
draw_polygon([(-40,-130),(-10,-155),(10,-155),(40,-130),
              (30,-110),(-30,-110)], DARK_ORNG, DARK_ORNG)

# Neck
draw_polygon([(-28,-110),(28,-110),(24,-65),(-24,-65)], SKIN, DARK_SKIN)

# Shoulders
draw_polygon([(-170,-185),(-110,-130),(-120,-270),(-170,-270)], ORANGE, DARK_ORNG, 2)
draw_polygon([(170,-185),(110,-130),(120,-270),(170,-270)], ORANGE, DARK_ORNG, 2)

# Scroll on back (peeking over right shoulder)
draw_polygon([(90,-130),(140,-90),(155,-140),(105,-175)], SCROLL_WHT, "#aaaaaa", 2)
filled_ellipse(122, -110, 20, 10, SCROLL_WHT, "#aaaaaa")
# Spiral on scroll
goto(122,-108)
t.pencolor(RED_SPIRAL); t.pensize(1.5); t.pendown(); t.circle(8); t.penup()

# ══════════════════════════════════════════
#  HEAD
# ══════════════════════════════════════════

# Head base
filled_ellipse(0, 100, 100, 115, SKIN, DARK_SKIN, pw=2)

# ── Blonde spiky hair ──
spikes = [
    # top spikes
    [(-95,130),(-130,270),(-55,160)],
    [(-60,160),(-80,290),(-10,175)],
    [(-20,175),(0,300),(20,175)],
    [(10,175),(80,290),(60,160)],
    [(55,160),(130,270),(95,130)],
    # side spikes
    [(-100,100),(-160,220),(-90,150)],
    [(100,100),(160,220),(90,150)],
    # lower side
    [(-100,60),(-155,140),(-98,110)],
    [(100,60),(155,140),(98,110)],
]
for sp in spikes:
    draw_polygon(sp, BLONDE, DARK_BLOND, 1)

# Hair crown (covers top of head)
draw_polygon(
    [(-100,110),(-85,170),(-40,210),(0,220),(40,210),(85,170),(100,110),
     (75,70),(0,50),(-75,70)],
    BLONDE, DARK_BLOND, 1
)

# Hair fringe over forehead (below headband)
draw_polygon([(-70,55),(-85,30),(-60,20),(-20,40),(0,45)], BLONDE, DARK_BLOND)
draw_polygon([(70,55),(85,30),(60,20),(20,40),(0,45)], BLONDE, DARK_BLOND)

# ── Konoha Headband ──
draw_polygon([(-105,75),(105,75),(105,38),(-105,38)], HEADBAND, BLACK, 2)
# Metal plate
draw_polygon([(-65,73),(65,73),(65,40),(-65,40)], METAL, "#999922", 2)
# Leaf symbol
t.pencolor(LEAF_G); t.pensize(1.5)
goto(0,52); t.pendown(); t.circle(10); t.penup()
goto(-10,60); t.pendown(); t.goto(0,73); t.penup()
goto(10,60); t.pendown(); t.goto(0,73); t.penup()
goto(0,52); t.pendown(); t.goto(0,45); t.penup()

# ── Ears ──
filled_ellipse(-103, 30, 15, 22, SKIN, DARK_SKIN)
filled_ellipse( 103, 30, 15, 22, SKIN, DARK_SKIN)

# ── Eyes ──
# Left eye
filled_ellipse(-40, 15, 22, 16, WHITE, BLACK, pw=2)
filled_circle(-40, 12, 11, BLUE_EYE, DARK_BLUE)
filled_circle(-40, 12,  6, BLACK)
filled_circle(-36, 16,  3, WHITE)   # shine
# Upper eyelid
arc(-40, 12, 16, 10, 170, BLACK, 2)

# Right eye
filled_ellipse(40, 15, 22, 16, WHITE, BLACK, pw=2)
filled_circle(40, 12, 11, BLUE_EYE, DARK_BLUE)
filled_circle(40, 12,  6, BLACK)
filled_circle(44, 16,  3, WHITE)    # shine
arc(40, 12, 16, 10, 170, BLACK, 2)

# ── Eyebrows ──
t.pencolor(DARK_BLOND); t.pensize(4)
goto(-60, 36); t.pendown(); t.goto(-20, 40); t.penup()
goto( 20, 40); t.pendown(); t.goto( 60, 36); t.penup()

# ── Nose ──
t.pencolor(SHADOW); t.pensize(2)
goto(-6, -5); t.pendown(); t.goto(-3,-15); t.goto(3,-15); t.goto(6,-5); t.penup()

# ── Smile / mouth ──
arc(0, -30, 18, 200, 340, SHADOW, 2)

# ══════════════════════════════════════════
#  WHISKER MARKS (3 per cheek)
# ══════════════════════════════════════════
whisker_sets = [
    # left cheek  (x1,y1,x2,y2)
    [(-90,  5, -45,  8)],
    [(-92,  -5, -46,  0)],
    [(-88, -15, -45, -8)],
    # right cheek
    [(45,  8,  90,  5)],
    [(46,  0,  92, -5)],
    [(45, -8,  88,-15)],
]
t.pencolor(RED_MARK); t.pensize(2.5)
for ws in whisker_sets:
    x1,y1,x2,y2 = ws[0]
    goto(x1,y1); t.pendown(); t.goto(x2,y2); t.penup()

# ══════════════════════════════════════════
#  LABELS
# ══════════════════════════════════════════
goto(0, -330)
t.pencolor("#ffcc00")
t.write("Naruto Uzumaki", align="center", font=("Arial", 20, "bold"))
goto(0, -360)
t.pencolor("#ff6600")
t.write("Believe it!  🍥  Future Hokage", align="center", font=("Arial", 12, "normal"))

screen.mainloop()