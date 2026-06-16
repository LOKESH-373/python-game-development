import turtle
import math

# Setup
screen = turtle.Screen()
screen.bgcolor("#FFB6C1")
screen.title("Barbie Girl")
screen.setup(600, 750)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def draw_filled_circle(x, y, r, fill, outline=""):
    t.penup(); t.goto(x, y - r); t.pendown()
    t.fillcolor(fill)
    t.pencolor(outline if outline else fill)
    t.pensize(2)
    t.begin_fill(); t.circle(r); t.end_fill()

def draw_ellipse(x, y, rx, ry, fill, outline=""):
    t.penup(); t.goto(x + rx, y); t.pendown()
    t.fillcolor(fill)
    t.pencolor(outline if outline else fill)
    t.pensize(1)
    t.begin_fill()
    for angle in range(361):
        rad = math.radians(angle)
        t.goto(x + rx * math.cos(rad), y + ry * math.sin(rad))
    t.end_fill()

def draw_polygon(points, fill, outline="", size=1):
    t.penup(); t.goto(points[0]); t.pendown()
    t.fillcolor(fill)
    t.pencolor(outline if outline else fill)
    t.pensize(size)
    t.begin_fill()
    for p in points: t.goto(p)
    t.goto(points[0])
    t.end_fill()

def draw_arc(x, y, r, start, end, color, size=2):
    t.penup()
    t.goto(x + r * math.cos(math.radians(start)),
           y + r * math.sin(math.radians(start)))
    t.pendown()
    t.pencolor(color); t.pensize(size)
    for a in range(start, end):
        rad = math.radians(a)
        t.goto(x + r * math.cos(rad), y + r * math.sin(rad))

# ── HAIR (back layer) ─────────────────────────────────────────────────────────
hair_back = [(-70, 200), (70, 200), (85, 130), (90, 30),
             (75, -80), (55, -130), (-55, -130), (-75, -80),
             (-90, 30), (-85, 130)]
draw_polygon(hair_back, "#FFD700", "#DAA520", 2)

# ── NECK ──────────────────────────────────────────────────────────────────────
draw_polygon([(-18, 110), (18, 110), (15, 140), (-15, 140)],
             "#FFDAB9", "#F4C2A1", 1)

# ── HEAD ──────────────────────────────────────────────────────────────────────
draw_filled_circle(0, 150, 80, "#FFDAB9", "#F4C2A1")

# ── HAIR (front top) ──────────────────────────────────────────────────────────
hair_top = [(-70, 200), (70, 200), (60, 230), (30, 245),
            (0, 248), (-30, 245), (-60, 230)]
draw_polygon(hair_top, "#FFD700", "#DAA520", 2)

# Side hair strands left
for i, (sx, sy, ex, ey) in enumerate([
    (-65, 190, -80, 100), (-72, 170, -88, 80), (-60, 150, -78, 60)]):
    t.penup(); t.goto(sx, sy); t.pendown()
    t.pencolor("#DAA520"); t.pensize(8)
    t.goto(ex, ey)

# Side hair strands right
for sx, sy, ex, ey in [
    (65, 190, 80, 100), (72, 170, 88, 80), (60, 150, 78, 60)]:
    t.penup(); t.goto(sx, sy); t.pendown()
    t.pencolor("#DAA520"); t.pensize(8)
    t.goto(ex, ey)

# ── EYES ──────────────────────────────────────────────────────────────────────
# Eye whites
draw_ellipse(-28, 158, 18, 13, "white", "#CCCCCC")
draw_ellipse(28, 158, 18, 13, "white", "#CCCCCC")

# Irises
draw_filled_circle(-28, 152, 10, "#4FC3F7", "#0288D1")
draw_filled_circle(28, 152, 10, "#4FC3F7", "#0288D1")

# Pupils
draw_filled_circle(-28, 152, 5, "#1A1A2E")
draw_filled_circle(28, 152, 5, "#1A1A2E")

# Eye shine
draw_filled_circle(-25, 155, 2, "white")
draw_filled_circle(31, 155, 2, "white")

# Eyelashes upper
for dx in [-38, -30, -22, -14]:
    t.penup(); t.goto(dx, 168); t.pendown()
    t.pencolor("#1A1A2E"); t.pensize(2)
    t.goto(dx - 2, 176)
for dx in [38, 30, 22, 14]:
    t.penup(); t.goto(dx, 168); t.pendown()
    t.goto(dx + 2, 176)

# Eyebrows
draw_arc(-28, 175, 16, 20, 160, "#8B6914", 3)
draw_arc(28, 175, 16, 20, 160, "#8B6914", 3)

# ── NOSE ──────────────────────────────────────────────────────────────────────
t.penup(); t.goto(-5, 138); t.pendown()
t.pencolor("#F4A58A"); t.pensize(2)
t.goto(0, 133); t.goto(5, 138)

# ── LIPS ──────────────────────────────────────────────────────────────────────
# Upper lip
upper_lip = [(-22, 123), (-10, 128), (0, 126), (10, 128), (22, 123),
             (10, 120), (0, 122), (-10, 120)]
draw_polygon(upper_lip, "#FF1493", "#C2185B", 1)
# Lower lip
lower_lip = [(-20, 123), (20, 123), (15, 113), (0, 110), (-15, 113)]
draw_polygon(lower_lip, "#FF69B4", "#C2185B", 1)
# Lip shine
draw_ellipse(-8, 118, 5, 3, "#FFB6C1")

# ── CHEEKS (blush) ────────────────────────────────────────────────────────────
draw_ellipse(-52, 145, 18, 10, "#FFB6C1")
draw_ellipse(52, 145, 18, 10, "#FFB6C1")

# ── EARS ──────────────────────────────────────────────────────────────────────
draw_ellipse(-80, 155, 10, 13, "#FFDAB9", "#F4C2A1")
draw_ellipse(80, 155, 10, 13, "#FFDAB9", "#F4C2A1")
# Earrings
draw_filled_circle(-80, 140, 5, "#FF69B4", "#FF1493")
draw_filled_circle(80, 140, 5, "#FF69B4", "#FF1493")

# ── SHOULDERS / BODY BASE ─────────────────────────────────────────────────────
# Shoulders
draw_ellipse(-60, 100, 35, 18, "#FFDAB9", "#F4C2A1")
draw_ellipse(60, 100, 35, 18, "#FFDAB9", "#F4C2A1")

# ── DRESS TOP (bodice) ────────────────────────────────────────────────────────
bodice = [(-55, 108), (55, 108), (65, 20), (50, -20),
          (-50, -20), (-65, 20)]
draw_polygon(bodice, "#FF1493", "#C2185B", 2)

# Dress sparkles
for sx, sy in [(0, 70), (-25, 50), (25, 50), (-10, 20), (10, 20),
               (-30, 85), (30, 85)]:
    t.penup(); t.goto(sx, sy); t.pendown()
    t.pencolor("white"); t.pensize(1)
    for a in range(0, 360, 45):
        t.goto(sx, sy)
        t.goto(sx + 5 * math.cos(math.radians(a)),
               sy + 5 * math.sin(math.radians(a)))

# Neckline decoration
neckline = [(-30, 108), (30, 108), (20, 95), (0, 90), (-20, 95)]
draw_polygon(neckline, "#FF69B4", "#FF1493", 1)

# ── DRESS SKIRT ───────────────────────────────────────────────────────────────
skirt = [(-65, 20), (65, 20), (100, -80), (90, -180),
         (60, -230), (0, -245), (-60, -230),
         (-90, -180), (-100, -80)]
draw_polygon(skirt, "#FF69B4", "#FF1493", 2)

# Skirt layers / ruffles
ruffle1 = [(-80, -60), (80, -60), (95, -110), (-95, -110)]
draw_polygon(ruffle1, "#FFB6C1", "#FF69B4", 1)
ruffle2 = [(-88, -120), (88, -120), (92, -170), (-92, -170)]
draw_polygon(ruffle2, "#FF1493", "#C2185B", 1)
ruffle3 = [(-90, -175), (90, -175), (80, -220), (-80, -220)]
draw_polygon(ruffle3, "#FFB6C1", "#FF69B4", 1)

# ── BELT ──────────────────────────────────────────────────────────────────────
belt = [(-65, 20), (65, 20), (62, 5), (-62, 5)]
draw_polygon(belt, "#C2185B", "#880E4F", 2)
draw_filled_circle(0, 12, 8, "#FFD700", "#DAA520")

# ── ARMS ──────────────────────────────────────────────────────────────────────
# Left arm
left_arm = [(-55, 100), (-75, 105), (-110, 30), (-90, 20)]
draw_polygon(left_arm, "#FFDAB9", "#F4C2A1", 1)
# Left hand
draw_filled_circle(-110, 22, 12, "#FFDAB9", "#F4C2A1")

# Right arm
right_arm = [(55, 100), (75, 105), (110, 30), (90, 20)]
draw_polygon(right_arm, "#FFDAB9", "#F4C2A1", 1)
# Right hand
draw_filled_circle(110, 22, 12, "#FFDAB9", "#F4C2A1")

# Gloves
draw_ellipse(-110, 22, 13, 15, "#FF69B4", "#FF1493")
draw_ellipse(110, 22, 13, 15, "#FF69B4", "#FF1493")

# ── LEGS ──────────────────────────────────────────────────────────────────────
# Left leg
left_leg = [(-40, -242), (-10, -242), (-15, -360), (-42, -360)]
draw_polygon(left_leg, "#FFDAB9", "#F4C2A1", 1)
# Right leg
right_leg = [(40, -242), (10, -242), (15, -360), (42, -360)]
draw_polygon(right_leg, "#FFDAB9", "#F4C2A1", 1)

# ── HEELS / SHOES ─────────────────────────────────────────────────────────────
# Left shoe
left_shoe = [(-42, -355), (-10, -355), (-8, -375), (-20, -380),
             (-44, -372), (-48, -360)]
draw_polygon(left_shoe, "#C2185B", "#880E4F", 2)
# Left heel
draw_polygon([(-44, -365), (-50, -365), (-50, -385), (-42, -380)],
             "#880E4F", "#880E4F", 1)

# Right shoe
right_shoe = [(42, -355), (10, -355), (8, -375), (20, -380),
              (44, -372), (48, -360)]
draw_polygon(right_shoe, "#C2185B", "#880E4F", 2)
# Right heel
draw_polygon([(44, -365), (50, -365), (50, -385), (42, -380)],
             "#880E4F", "#880E4F", 1)

# ── HAIR BOW ──────────────────────────────────────────────────────────────────
left_bow = [(-5, 248), (-40, 265), (-35, 248), (-40, 230)]
draw_polygon(left_bow, "#FF1493", "#C2185B", 2)
right_bow = [(5, 248), (40, 265), (35, 248), (40, 230)]
draw_polygon(right_bow, "#FF1493", "#C2185B", 2)
draw_filled_circle(0, 248, 8, "#FFD700", "#DAA520")

# ── NECKLACE ──────────────────────────────────────────────────────────────────
t.penup(); t.goto(-25, 115); t.pendown()
t.pencolor("#FFD700"); t.pensize(2)
for angle in range(180, 360):
    rad = math.radians(angle)
    t.goto(25 * math.cos(rad), 115 + 12 * math.sin(rad))
draw_filled_circle(0, 103, 5, "#FF69B4", "#FF1493")

# ── LABEL ─────────────────────────────────────────────────────────────────────
t.penup(); t.goto(0, -420)
t.pencolor("#C2185B")
t.write("✨ Barbie Girl ✨", align="center",
        font=("Arial", 20, "bold"))

screen.mainloop()