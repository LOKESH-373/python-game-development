import turtle
import math

# Setup
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Spider-Man")
screen.setup(600, 700)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def draw_circle_filled(x, y, r, color):
    t.penup()
    t.goto(x, y - r)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

def draw_ellipse(x, y, rx, ry, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.pencolor(color)
    for angle in range(360):
        rad = math.radians(angle)
        px = x + rx * math.cos(rad)
        py = y + ry * math.sin(rad)
        t.goto(px, py)
    t.end_fill()

def draw_polygon(points, color, outline="black"):
    t.penup()
    t.goto(points[0])
    t.pendown()
    t.fillcolor(color)
    t.pencolor(outline)
    t.begin_fill()
    for p in points:
        t.goto(p)
    t.goto(points[0])
    t.end_fill()

def draw_web_lines(cx, cy, radius):
    t.pencolor("#8B0000")
    t.pensize(1)
    # Radial lines
    for angle in range(0, 360, 30):
        rad = math.radians(angle)
        t.penup()
        t.goto(cx, cy)
        t.pendown()
        t.goto(cx + radius * math.cos(rad), cy + radius * math.sin(rad))
    # Concentric circles
    for r in range(20, radius + 1, 20):
        t.penup()
        t.goto(cx, cy - r)
        t.pendown()
        t.circle(r)

# ── HEAD (red base) ──────────────────────────────────────────────────────────
head_cx, head_cy, head_r = 0, 50, 110
draw_circle_filled(head_cx, head_cy, head_r, "red")

# ── WEB PATTERN on head ───────────────────────────────────────────────────────
draw_web_lines(head_cx, head_cy, head_r)

# ── BLUE MASK SIDES ──────────────────────────────────────────────────────────
# Left blue cheek
draw_ellipse(-65, 30, 50, 65, "#003399")
# Right blue cheek
draw_ellipse(65, 30, 50, 65, "#003399")

# ── FACE / SKIN AREA (lower face) ────────────────────────────────────────────
draw_ellipse(0, -10, 60, 45, "red")

# ── EYES (white lenses) ──────────────────────────────────────────────────────
# Left eye
left_eye = [(-80, 80), (-30, 100), (-20, 60), (-75, 50)]
draw_polygon(left_eye, "white", "white")

# Right eye
right_eye = [(80, 80), (30, 100), (20, 60), (75, 50)]
draw_polygon(right_eye, "white", "white")

# Eye outlines (black)
t.pensize(3)
t.pencolor("black")
for pts in [left_eye, right_eye]:
    t.penup(); t.goto(pts[0]); t.pendown()
    for p in pts: t.goto(p)
    t.goto(pts[0])

# ── BODY ─────────────────────────────────────────────────────────────────────
# Torso red
torso = [(-90, -60), (90, -60), (75, -230), (-75, -230)]
draw_polygon(torso, "red")

# Blue body sides
left_side = [(-90, -60), (-60, -60), (-70, -230), (-90, -230)]
draw_polygon(left_side, "#003399")
right_side = [(90, -60), (60, -60), (70, -230), (90, -230)]
draw_polygon(right_side, "#003399")

# Chest web
draw_web_lines(0, -130, 80)

# Chest spider symbol
t.penup(); t.goto(0, -110)
t.pendown()
t.pencolor("black"); t.fillcolor("black")
t.begin_fill()
t.circle(15)
t.end_fill()
# Spider legs (simple lines)
t.pensize(3)
for angle in [30, 60, 120, 150, 210, 240, 300, 330]:
    rad = math.radians(angle)
    t.penup(); t.goto(0, -110)
    t.pendown()
    t.goto(0 + 35 * math.cos(rad), -110 + 35 * math.sin(rad))

# ── BELT ─────────────────────────────────────────────────────────────────────
belt = [(-90, -230), (90, -230), (90, -255), (-90, -255)]
draw_polygon(belt, "#003399")
# Belt buckle
buckle = [(-18, -232), (18, -232), (18, -253), (-18, -253)]
draw_polygon(buckle, "red")

# ── LEGS ─────────────────────────────────────────────────────────────────────
# Left leg
left_leg = [(-75, -255), (-15, -255), (-25, -400), (-80, -400)]
draw_polygon(left_leg, "red")
left_leg_blue = [(-80, -255), (-75, -255), (-80, -400), (-85, -400)]
draw_polygon(left_leg_blue, "#003399")

# Right leg
right_leg = [(75, -255), (15, -255), (25, -400), (80, -400)]
draw_polygon(right_leg, "red")
right_leg_blue = [(80, -255), (75, -255), (80, -400), (85, -400)]
draw_polygon(right_leg_blue, "#003399")

# Boots
left_boot = [(-80, -400), (-25, -400), (-20, -430), (-85, -430)]
draw_polygon(left_boot, "#003399")
right_boot = [(80, -400), (25, -400), (20, -430), (85, -430)]
draw_polygon(right_boot, "#003399")

# ── ARMS ─────────────────────────────────────────────────────────────────────
# Left arm
left_arm = [(-90, -60), (-150, -130), (-145, -220), (-110, -65)]
draw_polygon(left_arm, "red")
# Right arm
right_arm = [(90, -60), (150, -130), (145, -220), (110, -65)]
draw_polygon(right_arm, "red")

# Gloves
left_glove = [(-150, -130), (-165, -200), (-145, -220), (-130, -150)]
draw_polygon(left_glove, "#003399")
right_glove = [(150, -130), (165, -200), (145, -220), (130, -150)]
draw_polygon(right_glove, "#003399")

# ── DONE ─────────────────────────────────────────────────────────────────────
t.penup()
t.goto(0, -470)
t.pencolor("black")
t.write("Spider-Man", align="center", font=("Arial", 18, "bold"))

screen.mainloop()