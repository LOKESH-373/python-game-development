import turtle
import math

screen = turtle.Screen()
screen.bgcolor("#1a1a2e")
screen.title("Kakashi Hatake")
screen.setup(700, 750)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def goto(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def filled_circle(x, y, r, color, outline=None):
    goto(x, y - r)
    t.fillcolor(color)
    t.pencolor(outline if outline else color)
    t.pensize(2 if outline else 1)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

def filled_ellipse(x, y, rx, ry, color, outline=None, steps=60):
    t.fillcolor(color)
    t.pencolor(outline if outline else color)
    t.pensize(2 if outline else 1)
    t.begin_fill()
    goto(x + rx, y)
    t.pendown()
    for i in range(steps + 1):
        angle = 2 * math.pi * i / steps
        px = x + rx * math.cos(angle)
        py = y + ry * math.sin(angle)
        t.goto(px, py)
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

SKIN = "#f5c5a3"
DARK_SKIN = "#e0a882"
SILVER = "#c8c8d4"
DARK_SILVER = "#8888a0"
BLACK = "#1a1a1a"
MASK_WHITE = "#dde8f0"
MASK_OUTLINE = "#aabbcc"
RED_EYE = "#cc2200"
DARK_RED = "#881100"
LEAF_GREEN = "#3a7a3a"
LEAF_METAL = "#c0c070"
NAVY = "#1a1a50"
DARK_NAVY = "#0d0d30"
JOUNIN_BLUE = "#2244aa"
ORANGE = "#dd6600"

# ── Neck ──
draw_polygon([(-35, -130), (35, -130), (30, -70), (-30, -70)], SKIN, DARK_SKIN)

# ── Shoulders / Jounin vest ──
draw_polygon([(-150, -280), (150, -280), (130, -130), (-130, -130)], JOUNIN_BLUE, DARK_NAVY, 2)
draw_polygon([(-50, -130), (50, -130), (45, -180), (-45, -180)], NAVY, DARK_NAVY, 2)
# Vest pockets
draw_polygon([(-110, -200), (-60, -200), (-60, -250), (-110, -250)], DARK_NAVY, BLACK, 1)
draw_polygon([(60, -200), (110, -200), (110, -250), (60, -250)], DARK_NAVY, BLACK, 1)

# ── Head (face base) ──
filled_ellipse(0, 80, 95, 110, SKIN, DARK_SKIN)

# ── Spiky silver hair ──
hair_spikes = [
    [(-90, 120), (-50, 220), (-20, 130)],
    [(-60, 140), (-30, 250), (0, 150)],
    [(-30, 150), (10, 260), (30, 155)],
    [(0, 155), (45, 255), (60, 150)],
    [(30, 150), (75, 235), (90, 130)],
    [(60, 140), (105, 210), (100, 110)],
    # back/left spikes
    [(-95, 100), (-140, 210), (-80, 130)],
    [(-100, 70), (-155, 160), (-90, 100)],
]
for spike in hair_spikes:
    draw_polygon(spike, SILVER, DARK_SILVER, 1)

# Hair base (covers top of head)
draw_polygon(
    [(-95, 100), (-90, 150), (-50, 190), (0, 200), (50, 190), (90, 150), (95, 100),
     (70, 60), (0, 40), (-70, 60)],
    SILVER, DARK_SILVER, 1
)

# ── Konoha headband ──
draw_polygon([(-100, 90), (100, 90), (100, 50), (-100, 50)], DARK_NAVY, BLACK, 2)
# Metal plate
draw_polygon([(-60, 88), (60, 88), (60, 52), (-60, 52)], LEAF_METAL, "#a0a050", 2)
# Leaf symbol on plate
goto(0, 70)
t.pencolor(LEAF_GREEN)
t.pensize(2)
t.pendown()
# Leaf swirl (simplified circle + lines)
t.penup(); t.goto(0, 62); t.pendown()
t.pencolor(DARK_NAVY)
t.pensize(1.5)
t.circle(10)
goto(-8, 70); t.goto(0, 85)
goto(8, 70); t.goto(0, 85)
goto(0, 60); t.goto(0, 55)

# ── Left eye (covered by headband — just below) ──
# Left eye (normal black eye visible slightly under band)
filled_ellipse(-38, 25, 18, 14, "#ffffff", BLACK, 40)
filled_circle(-38, 22, 9, "#3a2a1a")
filled_circle(-38, 22, 5, BLACK)
# Eye shine
filled_circle(-34, 26, 2, "#ffffff")

# ── Right eye — SHARINGAN (revealed) ──
# White sclera
filled_ellipse(38, 25, 20, 15, "#ffffff", BLACK, 40)
# Red iris
filled_circle(38, 22, 13, RED_EYE, DARK_RED)
# Black pupil
filled_circle(38, 22, 5, BLACK)
# Three tomoe (magatama) around pupil
for angle_deg in [90, 210, 330]:
    angle = math.radians(angle_deg)
    tx = 38 + 8 * math.cos(angle)
    ty = 22 + 8 * math.sin(angle)
    filled_circle(int(tx), int(ty), 3, BLACK)
# Sharingan ring
goto(38, 22 - 12)
t.pencolor(DARK_RED)
t.pensize(1)
t.pendown()
t.circle(12)

# ── Nose (subtle) ──
goto(-8, 0)
t.pencolor(DARK_SKIN)
t.pensize(2)
t.pendown()
t.goto(-5, -10)
t.goto(0, -8)

# ── Mask (covers lower half of face) ──
draw_polygon(
    [(-90, 20), (90, 20), (85, -100), (60, -120), (0, -130), (-60, -120), (-85, -100)],
    MASK_WHITE, MASK_OUTLINE, 2
)
# Mask fold lines (subtle)
goto(-60, 10)
t.pencolor(MASK_OUTLINE); t.pensize(1); t.pendown(); t.goto(-55, -60)
goto(60, 10)
t.pendown(); t.goto(55, -60)

# ── Ears ──
filled_ellipse(-97, 30, 14, 20, SKIN, DARK_SKIN)
filled_ellipse(97, 30, 14, 20, SKIN, DARK_SKIN)

# ── Label ──
goto(0, -310)
t.pencolor("#ffffff")
t.pensize(1)
t.write("Kakashi Hatake", align="center", font=("Arial", 18, "bold"))

goto(0, -340)
t.pencolor("#8888aa")
t.write("Copy Ninja | Sixth Hokage", align="center", font=("Arial", 11, "normal"))

screen.mainloop()