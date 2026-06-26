import turtle
import math
import time

# ── Screen setup ──────────────────────────────────────────────────────────────
screen = turtle.Screen()
screen.title("🦋 Butterfly Flying")
screen.bgcolor("#0a0a2e")          # deep midnight blue sky
screen.setup(width=800, height=600)
screen.tracer(0)                   # manual updates for smooth animation

# ── Utility: draw a filled curve (petal / wing lobe) ─────────────────────────
def draw_wing_lobe(t, radius, steps, color_fill, color_outline):
    """Draw a semicircular wing lobe using small forward steps."""
    t.fillcolor(color_fill)
    t.pencolor(color_outline)
    t.begin_fill()
    for _ in range(steps):
        t.forward(radius * math.pi / steps * 2)
        t.left(180 / steps)
    t.end_fill()

# ── Draw one full butterfly (body + 4 wings) at position (bx, by) ────────────
def draw_butterfly(t, bx, by, scale, angle, wing_open):
    """
    wing_open : 0.0 (closed) → 1.0 (fully open)
    angle     : heading of travel in degrees
    """
    t.penup()
    t.goto(bx, by)
    t.setheading(angle)

    # --- wing colours (monarch-style orange with dark veins) ---
    upper_color  = "#FF6B00"
    lower_color  = "#FF8C00"
    tip_color    = "#1a1a1a"
    outline      = "#2B1700"
    body_color   = "#3B1F00"

    # Flap factor maps wing_open to a y-scale stretch
    flap = 0.4 + 0.6 * wing_open   # 0.4 … 1.0

    def wing_pair(side):
        """side = +1 (right) or -1 (left)"""
        t.penup()
        t.goto(bx, by)
        t.pendown()
        t.pensize(1)

        # ── upper wing ──────────────────────────────────────────
        pts_upper = []
        for deg in range(0, 181, 6):
            r = scale * (1.0 + 0.35 * math.cos(math.radians(deg)))
            dx = r * math.cos(math.radians(deg)) * side
            dy = r * math.sin(math.radians(deg)) * flap
            pts_upper.append((bx + dx, by + dy))
        pts_upper.append((bx, by))

        t.fillcolor(upper_color)
        t.pencolor(outline)
        t.begin_fill()
        t.penup(); t.goto(pts_upper[0]); t.pendown()
        for px, py in pts_upper[1:]:
            t.goto(px, py)
        t.end_fill()

        # dark tip blotch
        t.penup()
        tip_cx = bx + side * scale * 1.25
        tip_cy = by + scale * flap * 0.85
        t.goto(tip_cx, tip_cy)
        t.pendown()
        t.fillcolor(tip_color)
        t.pencolor(tip_color)
        t.begin_fill()
        t.circle(scale * 0.22)
        t.end_fill()

        # ── lower wing ──────────────────────────────────────────
        pts_lower = []
        for deg in range(180, 361, 6):
            r = scale * (0.65 + 0.25 * math.cos(math.radians(deg)))
            dx = r * math.cos(math.radians(deg)) * side
            dy = r * math.sin(math.radians(deg)) * flap * 0.75
            pts_lower.append((bx + dx, by + dy))
        pts_lower.append((bx, by))

        t.fillcolor(lower_color)
        t.pencolor(outline)
        t.begin_fill()
        t.penup(); t.goto(pts_lower[0]); t.pendown()
        for px, py in pts_lower[1:]:
            t.goto(px, py)
        t.end_fill()

        # vein lines
        t.pencolor("#8B3A00")
        t.pensize(1)
        for i in range(1, 4):
            frac = i / 4
            vx = bx + side * scale * frac
            t.penup(); t.goto(bx, by); t.pendown()
            t.goto(vx, by + scale * flap * frac * 0.9)

    wing_pair(+1)
    wing_pair(-1)

    # ── Body ────────────────────────────────────────────────────
    t.penup()
    t.goto(bx, by - scale * 0.55)
    t.pendown()
    t.fillcolor(body_color)
    t.pencolor("#111")
    t.pensize(1)
    t.begin_fill()
    t.circle(scale * 0.12, 360)
    t.end_fill()

    # body elongated
    for seg in range(5):
        yy = by - scale * 0.45 + seg * scale * 0.22
        t.penup(); t.goto(bx, yy); t.pendown()
        t.fillcolor(body_color)
        t.begin_fill()
        t.circle(scale * (0.09 - seg * 0.01))
        t.end_fill()

    # ── Antennae ────────────────────────────────────────────────
    t.pencolor("#FFD700")
    t.pensize(1)
    for side in (+1, -1):
        t.penup()
        t.goto(bx, by + scale * 0.05)
        t.pendown()
        ax = bx + side * scale * 0.35
        ay = by + scale * 0.55
        t.goto(ax, ay)
        # knob
        t.fillcolor("#FFD700")
        t.begin_fill()
        t.circle(scale * 0.06)
        t.end_fill()

# ── Stars backdrop ────────────────────────────────────────────────────────────
def draw_stars(t, count=80):
    import random
    random.seed(42)
    t.pencolor("white")
    t.pensize(1)
    for _ in range(count):
        sx = random.randint(-390, 390)
        sy = random.randint(-280, 280)
        r  = random.choice([1, 1, 1, 2])
        t.penup(); t.goto(sx, sy); t.pendown()
        t.dot(r, "white")

# ── Flowers at bottom ─────────────────────────────────────────────────────────
def draw_flower(t, fx, fy, petal_color, center_color):
    for angle in range(0, 360, 60):
        t.penup()
        dx = 14 * math.cos(math.radians(angle))
        dy = 14 * math.sin(math.radians(angle))
        t.goto(fx + dx, fy + dy)
        t.pendown()
        t.fillcolor(petal_color)
        t.pencolor(petal_color)
        t.begin_fill()
        t.circle(7)
        t.end_fill()
    t.penup(); t.goto(fx, fy); t.pendown()
    t.fillcolor(center_color)
    t.begin_fill()
    t.circle(6)
    t.end_fill()

def draw_scenery(t):
    # Ground
    t.penup(); t.goto(-400, -220); t.pendown()
    t.fillcolor("#0d3b1a"); t.pencolor("#0d3b1a")
    t.begin_fill()
    for gx in range(-400, 401, 1):
        t.goto(gx, -300)
    t.goto(400, -220); t.goto(-400, -220)
    t.end_fill()

    # Flowers
    flowers = [
        (-300, -218, "#FF69B4", "#FFD700"),
        (-180, -215, "#FF4500", "#FFFF00"),
        ( -60, -220, "#9B59B6", "#FF8C00"),
        (  80, -216, "#FF1493", "#FFD700"),
        ( 200, -218, "#00CED1", "#FF69B4"),
        ( 320, -215, "#FF6347", "#FFFF00"),
    ]
    for fx, fy, pc, cc in flowers:
        draw_flower(t, fx, fy, pc, cc)

# ── Main animation loop ────────────────────────────────────────────────────────
def main():
    # Static background turtle
    bg = turtle.Turtle()
    bg.hideturtle(); bg.speed(0); bg.penup()
    draw_stars(bg)
    draw_scenery(bg)

    # Moon
    bg.penup(); bg.goto(300, 220); bg.pendown()
    bg.fillcolor("#FFFFF0"); bg.pencolor("#FFFFF0")
    bg.begin_fill(); bg.circle(38); bg.end_fill()

    # Title text
    bg.penup(); bg.goto(0, 255)
    bg.pencolor("#FFD700")
    bg.write("🦋  Butterfly Night Flight  🦋",
             align="center", font=("Arial", 16, "bold"))

    # Butterfly turtle
    bt = turtle.Turtle()
    bt.hideturtle(); bt.speed(0); bt.penup()

    # Flight path parameters
    t_val   = 0.0
    x_pos   = -350.0
    y_base  = 40.0
    speed   = 1.8          # horizontal pixels per frame
    amp     = 90           # vertical oscillation amplitude
    freq    = 0.025        # oscillation frequency

    frame   = 0
    wing_frames = 14       # frames per full flap cycle

    while True:
        bt.clear()

        # Flap: sine wave between 0 and 1
        wing_open = (math.sin(math.pi * frame / wing_frames) + 1) / 2

        # Position on a gentle sine wave
        cy = y_base + amp * math.sin(freq * x_pos)

        # Compute travel angle from derivative of sine path
        dy_dx   = amp * freq * math.cos(freq * x_pos)
        heading = math.degrees(math.atan(dy_dx))

        draw_butterfly(bt, x_pos, cy, scale=45,
                       angle=heading, wing_open=wing_open)

        screen.update()
        time.sleep(0.03)

        x_pos += speed
        frame += 1
        t_val += 0.03

        # Wrap around
        if x_pos > 420:
            x_pos = -390

if __name__ == "__main__":
    main()
    turtle.done()
