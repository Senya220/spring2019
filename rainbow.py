import turtle as t

all = "all"
rainbow_draw = "rainbow"
test = "test_rgb"
draw_line = "move_l"
calculate = "calculate_y"


def calculate_y1(x_m, y_m, x):
    if x < (x_m / 3):
        return y_m - int((x * y_m / x_m) * 3)
    elif (x >= x_m / 3) and (x < x_m * 2 / 3):
        return 0
    else:
        return int(((x - x_m * 2 / 3) * y_m / x_m) * 3)


def calculate_y2(x_m, y_m, x):
    if x < (x_m / 3):
        return int((x * y_m / x_m) * 3)
    elif (x >= x_m / 3) and (x < x_m * 2 / 3):
        return y_m - int(((x - x_m / 3) * y_m / x_m) * 3)
    else:
        return 0


def calculate_y3(x_m, y_m, x):
    if x < (x_m / 3):
        return 0
    elif (x >= x_m / 3) and (x < x_m * 2 / 3):
        return int(((x - x_m / 3) * y_m / x_m) * 3)
    else:
        return y_m - int(((x - x_m * 2 / 3) * y_m / x_m) * 3)


def move_t(how_many_pixels, height, y_func, color):
    x0, y0 = t.pos()
    t.pencolor(color)
    t.goto(x0, y0 + y_func(how_many_pixels, height, 0))
    t.pendown()
    for x in range(how_many_pixels + 1):
        t.goto(x0 + x, y0 + y_func(how_many_pixels, height, x))
    t.penup()


def move_l(how_many_pixels):
    t.pendown()
    t.setheading(0)

    for j in range(how_many_pixels):
        t.pencolor(calculate_y1(how_many_pixels, 255, j), calculate_y2(how_many_pixels, 255, j), calculate_y3(how_many_pixels, 255, j))
        t.forward(1)
    t.penup()


def rainbow(diameter, x, y):
    x0, y0 = t.pos()
    t.setheading(0)
    t.goto(x, y)
    t.pendown()
    m = diameter / 2
    for j in range(int(diameter / 6)):
        t.pencolor(calculate_y1(diameter / 6, 255, j), calculate_y2(diameter / 6, 255, j), calculate_y3(diameter / 6, 255, j))
        draw_half_circle(m)
        t.forward(-1)
        m = m - 1
    t.penup()
    t.goto(x0, y0)


def draw_half_circle(radius):
    t.setheading(90)
    t.circle(radius, 180)
    t.penup()
    t.setheading(0)
    t.forward(radius * 2)
    t.pendown()


def test_rgb():
    t.goto(-300, 0)
    move_t(600, 200, calculate_y1, '#b30000')
    t.goto(-300, 0)
    move_t(600, 200, calculate_y2, '#00cc00')
    t.goto(-300, 0)
    move_t(600, 200, calculate_y3, '#000080')


def help_r(command):
    print("Rainbow version 1.0 BETA")
    print("Set parameter to all to show all commands.")

    if command == "rainbow":
        print("Use this command to draw a rainbow!")
        print("Usage: rainbow(rainbow_diameter, x, y)")
        print("Examples:")
        print(">>> rainbow(600, 23, 30) (Draws a 600px diameter rainbow with start coordinates x:23 y:30")
        print(">>> rainbow(25, 140, -367) (Draws a 25px (Very small) diameter rainbow with start coordinates x:140 y:-367")
    elif command == "test_rgb":
        print("Use this command to see how to draw rainbow (RGB colors).")
        print("Usage: test_rgb()")
        print("Example:")
        print(">>> test_rgb() (Draws a RGB graphic used to draw this rainbow.")
    elif command == "move_l":
        print("Use this command to draw a rainbow line.")
        print("Usage: move_l(length)")
        print("Examples:")
        print(">>> move_l(456) (Draws a 456px rainbow line.")
        print(">>> move_l(2) (Draws a 2px (SO SMALL!!!) rainbow line.")
    elif command == "calculate":
        print("Use this command to calculate a RGB color what next in rainbow.")
        print("Usage: at example.")
        print("Example:")
        print("Use ")
        print(">>> for j in range(300):")
        print("        t.pencolor(calculate_y1(how_many_pixels, 255, j), calculate_y2(how_many_pixels, 255, j), calculate_y3(how_many_pixels, 255, j))")
        print("        t.forward(1)")
        print(" to draw your own 300px rainbow line!")
    elif command == "all":
        print("Commands:")
        print("rainbow_draw")
        print("test")
        print("draw_line")
        print("calculate")
