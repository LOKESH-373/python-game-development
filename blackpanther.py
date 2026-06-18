import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Black Panther")
screen.setup(800, 700)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def draw_filled_shape(points, color):
    t.penup()
    t.goto(points[0])
    t.pendown()
    t.fillcolor(color)
    t.pencolor(color)
    t.begin_fill()
    for p in points[1:]:
        t.goto(p)
    t.goto(points[0])
    t.end_fill()

def draw_arc(cx, cy, rx, ry, start_deg, end_deg, color, width=2):
    t.penup()
    t.pencolor(color)
    t.pensize(width)
    steps = 60
    start_rad = math.radians(start_deg)
    end_rad = math.radians(end_deg)
    angle = start_rad
    step = (end_rad - start_rad) / steps
    t.goto(cx + rx * math.cos(angle), cy + ry * math.sin(angle))
    t.pendown()
    for _ in range(steps):
        angle += step
        t.goto(cx + rx * math.cos(angle), cy + ry * math.sin(angle))
    t.penup()

def draw_filled_ellipse(cx, cy, rx, ry, color):
    points = []
    for i in range(360):
        rad = math.radians(i)
        points.append((cx + rx * math.cos(rad), cy + ry * math.sin(rad)))
    draw_filled_shape(points, color)

# ── Head / face base ──────────────────────────────────────────────────────────
# Outer head shape (dark purple-black)
head_pts = [
    (0, 240), (-90, 220), (-160, 160), (-180, 60),
    (-160, -60), (-120, -150), (-60, -200), (0, -220),
    (60, -200), (120, -150), (160, -60), (180, 60),
    (160, 160), (90, 220)
]
draw_filled_shape(head_pts, "#1a0a2e")

# Face surface (slightly lighter)
face_pts = [
    (0, 200), (-75, 185), (-140, 130), (-155, 50),
    (-135, -50), (-100, -140), (-50, -190), (0, -205),
    (50, -190), (100, -140), (135, -50), (155, 50),
    (140, 130), (75, 185)
]
draw_filled_shape(face_pts, "#12082a")

# ── Ears (panther ears — pointed) ────────────────────────────────────────────
left_ear = [(-60, 220), (-130, 300), (-170, 220), (-110, 195)]
draw_filled_shape(left_ear, "#1a0a2e")
left_ear_inner = [(-75, 215), (-128, 285), (-158, 220), (-108, 200)]
draw_filled_shape(left_ear_inner, "#3a1060")

right_ear = [(60, 220), (130, 300), (170, 220), (110, 195)]
draw_filled_shape(right_ear, "#1a0a2e")
right_ear_inner = [(75, 215), (128, 285), (158, 220), (108, 200)]
draw_filled_shape(right_ear_inner, "#3a1060")

# ── Vibranium brow/forehead stripe ───────────────────────────────────────────
brow_pts = [(-70, 120), (70, 120), (55, 100), (-55, 100)]
draw_filled_shape(brow_pts, "#7b2fff")

# ── Eyes (glowing purple) ────────────────────────────────────────────────────
# Left eye socket
left_eye_pts = [
    (-110, 90), (-60, 110), (-30, 90), (-50, 60), (-105, 55)
]
draw_filled_shape(left_eye_pts, "#3d0080")

# Left eye glow
left_glow_pts = [
    (-103, 84), (-62, 102), (-38, 84), (-56, 63), (-100, 61)
]
draw_filled_shape(left_glow_pts, "#9933ff")

# Left pupil
draw_filled_ellipse(-72, 80, 18, 10, "#200040")

# Right eye socket
right_eye_pts = [
    (110, 90), (60, 110), (30, 90), (50, 60), (105, 55)
]
draw_filled_shape(right_eye_pts, "#3d0080")

# Right eye glow
right_glow_pts = [
    (103, 84), (62, 102), (38, 84), (56, 63), (100, 61)
]
draw_filled_shape(right_glow_pts, "#9933ff")

# Right pupil
draw_filled_ellipse(72, 80, 18, 10, "#200040")

# ── Nose bridge ──────────────────────────────────────────────────────────────
nose_bridge = [(-15, 55), (15, 55), (20, -20), (0, -10), (-20, -20)]
draw_filled_shape(nose_bridge, "#0f0620")

# Nose
nose_pts = [(-30, -20), (30, -20), (35, -50), (15, -60),
            (0, -55), (-15, -60), (-35, -50)]
draw_filled_shape(nose_pts, "#1a0a2e")

# Nostrils
draw_filled_ellipse(-20, -45, 10, 7, "#0a0315")
draw_filled_ellipse(20, -45, 10, 7, "#0a0315")

# ── Mouth / snarl ────────────────────────────────────────────────────────────
# Lips
upper_lip = [(-45, -80), (45, -80), (35, -95), (15, -100),
             (0, -97), (-15, -100), (-35, -95)]
draw_filled_shape(upper_lip, "#2a0a50")

lower_lip = [(-45, -80), (45, -80), (40, -120), (20, -135),
             (0, -138), (-20, -135), (-40, -120)]
draw_filled_shape(lower_lip, "#1a0535")

# Teeth (snarling)
teeth = [(-35, -83), (-10, -83), (-10, -112), (-35, -108)]
draw_filled_shape(teeth, "#e8e0f0")
teeth2 = [(-8, -83), (8, -83), (8, -115), (-8, -115)]
draw_filled_shape(teeth2, "#e8e0f0")
teeth3 = [(10, -83), (35, -83), (35, -108), (10, -112)]
draw_filled_shape(teeth3, "#e8e0f0")

# Canine fangs
fang_l = [(-40, -83), (-25, -83), (-28, -128), (-44, -122)]
draw_filled_shape(fang_l, "#f0eaff")
fang_r = [(40, -83), (25, -83), (28, -128), (44, -122)]
draw_filled_shape(fang_r, "#f0eaff")

# ── Chin detail ──────────────────────────────────────────────────────────────
chin_stripe = [(-20, -150), (20, -150), (15, -175), (-15, -175)]
draw_filled_shape(chin_stripe, "#7b2fff")

# ── Vibranium necklace/collar ─────────────────────────────────────────────────
collar_pts = [
    (-160, -60), (-140, -170), (-80, -215), (0, -230),
    (80, -215), (140, -170), (160, -60),
    (130, -55), (80, -195), (0, -208),
    (-80, -195), (-130, -55)
]
draw_filled_shape(collar_pts, "#3a0a7a")

# Collar gems
for x in [-90, -45, 0, 45, 90]:
    gem_y = -220 + abs(x) * 0.3
    draw_filled_ellipse(x, gem_y, 8, 6, "#9933ff")
    draw_filled_ellipse(x, gem_y, 4, 3, "#cc88ff")

# ── Facial markings (Wakandan patterns) ──────────────────────────────────────
# Left cheek marks
for i, (x, y) in enumerate([(-120, 30), (-130, 10), (-125, -10)]):
    mark = [(x-12, y+4), (x+12, y+4), (x+10, y-4), (x-10, y-4)]
    draw_filled_shape(mark, "#5500bb")

# Right cheek marks
for i, (x, y) in enumerate([(120, 30), (130, 10), (125, -10)]):
    mark = [(x-12, y+4), (x+12, y+4), (x+10, y-4), (x-10, y-4)]
    draw_filled_shape(mark, "#5500bb")

# ── Forehead vibranium symbol (panther claw mark) ────────────────────────────
for dx in [-20, -6, 8]:
    claw = [(dx, 160), (dx+5, 160), (dx+8, 130), (dx+3, 130)]
    draw_filled_shape(claw, "#aa55ff")

# ── Glow outline around eyes ─────────────────────────────────────────────────
t.pensize(2)
draw_arc(-70, 80, 45, 25, 150, 30, "#cc66ff", 2)
draw_arc(70, 80, 45, 25, 30, 150, "#cc66ff", 2)

screen.mainloop()
import turtle
import math

screen = turtle.Screen()
screen.bgcolor("#0a0a0a")
screen.title("Black Panther - Black Edition")
screen.setup(800, 700)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def draw_filled_shape(points, color):
    t.penup()
    t.goto(points[0])
    t.pendown()
    t.fillcolor(color)
    t.pencolor(color)
    t.begin_fill()
    for p in points[1:]:
        t.goto(p)
    t.goto(points[0])
    t.end_fill()

def draw_arc(cx, cy, rx, ry, start_deg, end_deg, color, width=2):
    t.penup()
    t.pencolor(color)
    t.pensize(width)
    steps = 60
    start_rad = math.radians(start_deg)
    end_rad = math.radians(end_deg)
    angle = start_rad
    step = (end_rad - start_rad) / steps
    t.goto(cx + rx * math.cos(angle), cy + ry * math.sin(angle))
    t.pendown()
    for _ in range(steps):
        angle += step
        t.goto(cx + rx * math.cos(angle), cy + ry * math.sin(angle))
    t.penup()

def draw_filled_ellipse(cx, cy, rx, ry, color):
    points = []
    for i in range(360):
        rad = math.radians(i)
        points.append((cx + rx * math.cos(rad), cy + ry * math.sin(rad)))
    draw_filled_shape(points, color)

# ── Head / face base ──────────────────────────────────────────────────────────
head_pts = [
    (0, 240), (-90, 220), (-160, 160), (-180, 60),
    (-160, -60), (-120, -150), (-60, -200), (0, -220),
    (60, -200), (120, -150), (160, -60), (180, 60),
    (160, 160), (90, 220)
]
draw_filled_shape(head_pts, "#111111")

face_pts = [
    (0, 200), (-75, 185), (-140, 130), (-155, 50),
    (-135, -50), (-100, -140), (-50, -190), (0, -205),
    (50, -190), (100, -140), (135, -50), (155, 50),
    (140, 130), (75, 185)
]
draw_filled_shape(face_pts, "#0d0d0d")

# ── Ears ─────────────────────────────────────────────────────────────────────
left_ear = [(-60, 220), (-130, 300), (-170, 220), (-110, 195)]
draw_filled_shape(left_ear, "#111111")
left_ear_inner = [(-75, 215), (-128, 285), (-158, 220), (-108, 200)]
draw_filled_shape(left_ear_inner, "#222222")

right_ear = [(60, 220), (130, 300), (170, 220), (110, 195)]
draw_filled_shape(right_ear, "#111111")
right_ear_inner = [(75, 215), (128, 285), (158, 220), (108, 200)]
draw_filled_shape(right_ear_inner, "#222222")

# ── Silver brow stripe ───────────────────────────────────────────────────────
brow_pts = [(-70, 120), (70, 120), (55, 100), (-55, 100)]
draw_filled_shape(brow_pts, "#aaaaaa")

# ── Eyes (silver-white glow) ─────────────────────────────────────────────────
left_eye_pts = [(-110, 90), (-60, 110), (-30, 90), (-50, 60), (-105, 55)]
draw_filled_shape(left_eye_pts, "#333333")

left_glow_pts = [(-103, 84), (-62, 102), (-38, 84), (-56, 63), (-100, 61)]
draw_filled_shape(left_glow_pts, "#cccccc")

draw_filled_ellipse(-72, 80, 18, 10, "#111111")

right_eye_pts = [(110, 90), (60, 110), (30, 90), (50, 60), (105, 55)]
draw_filled_shape(right_eye_pts, "#333333")

right_glow_pts = [(103, 84), (62, 102), (38, 84), (56, 63), (100, 61)]
draw_filled_shape(right_glow_pts, "#cccccc")

draw_filled_ellipse(72, 80, 18, 10, "#111111")

# ── Nose bridge ──────────────────────────────────────────────────────────────
nose_bridge = [(-15, 55), (15, 55), (20, -20), (0, -10), (-20, -20)]
draw_filled_shape(nose_bridge, "#080808")

nose_pts = [(-30, -20), (30, -20), (35, -50), (15, -60),
            (0, -55), (-15, -60), (-35, -50)]
draw_filled_shape(nose_pts, "#111111")

draw_filled_ellipse(-20, -45, 10, 7, "#050505")
draw_filled_ellipse(20, -45, 10, 7, "#050505")

# ── Mouth / snarl ────────────────────────────────────────────────────────────
upper_lip = [(-45, -80), (45, -80), (35, -95), (15, -100),
             (0, -97), (-15, -100), (-35, -95)]
draw_filled_shape(upper_lip, "#1a1a1a")

lower_lip = [(-45, -80), (45, -80), (40, -120), (20, -135),
             (0, -138), (-20, -135), (-40, -120)]
draw_filled_shape(lower_lip, "#141414")

# Teeth
teeth1 = [(-35, -83), (-10, -83), (-10, -112), (-35, -108)]
draw_filled_shape(teeth1, "#e0e0e0")
teeth2 = [(-8, -83), (8, -83), (8, -115), (-8, -115)]
draw_filled_shape(teeth2, "#e8e8e8")
teeth3 = [(10, -83), (35, -83), (35, -108), (10, -112)]
draw_filled_shape(teeth3, "#e0e0e0")

# Fangs
fang_l = [(-40, -83), (-25, -83), (-28, -128), (-44, -122)]
draw_filled_shape(fang_l, "#f5f5f5")
fang_r = [(40, -83), (25, -83), (28, -128), (44, -122)]
draw_filled_shape(fang_r, "#f5f5f5")

# ── Chin stripe ──────────────────────────────────────────────────────────────
chin_stripe = [(-20, -150), (20, -150), (15, -175), (-15, -175)]
draw_filled_shape(chin_stripe, "#aaaaaa")

# ── Collar ───────────────────────────────────────────────────────────────────
collar_pts = [
    (-160, -60), (-140, -170), (-80, -215), (0, -230),
    (80, -215), (140, -170), (160, -60),
    (130, -55), (80, -195), (0, -208),
    (-80, -195), (-130, -55)
]
draw_filled_shape(collar_pts, "#1c1c1c")

# Collar gems (silver)
for x in [-90, -45, 0, 45, 90]:
    gem_y = -220 + abs(x) * 0.3
    draw_filled_ellipse(x, gem_y, 8, 6, "#888888")
    draw_filled_ellipse(x, gem_y, 4, 3, "#dddddd")

# ── Cheek markings (dark silver) ─────────────────────────────────────────────
for (x, y) in [(-120, 30), (-130, 10), (-125, -10)]:
    mark = [(x-12, y+4), (x+12, y+4), (x+10, y-4), (x-10, y-4)]
    draw_filled_shape(mark, "#555555")

for (x, y) in [(120, 30), (130, 10), (125, -10)]:
    mark = [(x-12, y+4), (x+12, y+4), (x+10, y-4), (x-10, y-4)]
    draw_filled_shape(mark, "#555555")

# ── Forehead claw marks ───────────────────────────────────────────────────────
for dx in [-20, -6, 8]:
    claw = [(dx, 160), (dx+5, 160), (dx+8, 130), (dx+3, 130)]
    draw_filled_shape(claw, "#888888")

# ── Eye glow outline ─────────────────────────────────────────────────────────
t.pensize(2)
draw_arc(-70, 80, 45, 25, 150, 30, "#aaaaaa", 2)
draw_arc(70, 80, 45, 25, 30, 150, "#aaaaaa", 2)

screen.mainloop()