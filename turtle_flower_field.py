#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import turtle as t
from random import randint, choice


def draw_square(color, size_f):
    t.begin_fill()
    t.pendown()
    t.color(color, 'red')
    t.forward(size_f)
    t.left(90)
    t.forward(size_f)
    t.left(90)
    t.forward(size_f)
    t.left(90)
    t.forward(size_f)
    t.left(90)
    t.fillcolor(color)
    t.penup()
    t.end_fill()


def draw_circle(color, size_f):
    t.begin_fill()
    t.pendown()
    t.color(color, "black")
    t.circle(size_f)
    t.fillcolor(color)
    t.end_fill()
    t.pencolor("black")
    t.circle(size_f)
    t.penup()


def draw_stick(x, y):
    t.goto(x, y - 400)
    t.setheading(90)
    t.pensize(20)
    t.pencolor("green")
    t.pendown()
    t.goto(x, y)
    t.pensize(3)
    t.pencolor("black")
    t.penup()
    t.goto(x - 9, y - 400)
    t.pendown()
    t.goto(x - 9, y)
    t.penup()
    t.goto(x + 9, y - 400)
    t.pendown()
    t.goto(x + 9, y)
    t.penup()


def draw_flower(size, x, y, color, color_center, angle, n):
    print(str("Drawing " + str(n) + "-petal " + color + " flower with " + color_center + " center at position x:" + str(x) + " and y:" + str(y) + "."))

    draw_stick(x, y)

    for j in range(n):
        t.setheading(angle + (360 * j // n))
        t.forward(size * 2.5)
        t.setheading(angle + (360 * j // n + 90))
        draw_circle(color, size)
        t.goto(x, y)

    t.setheading(90)
    t.forward(size * 1)
    t.setheading(180)
    draw_circle(color_center, size)


def draw_sun():
    t.penup()
    t.goto(-200, 200)
    a = abs(t.pos())
    t.pendown()
    t.color('orange', 'yellow')
    t.begin_fill()
    while True:
        t.forward(200)
        t.left(170)
        b = abs(t.pos())
        if a - 1 < b < a + 1:
            break
    t.penup()
    t.end_fill()


colors = ["magenta", "pink", "navy", "blue", "red", "yellow", "orange", "white"]

# --------------------

print()
print("Started")
t.bgcolor("cyan")
t.hideturtle()
t.penup()
t.speed(0)
t.pensize(3)

draw_sun()

# ---------------------------------------------------------------------
# Examples:
#   draw_flower(Size, X, Y, PetalColor, CenterColor, Angle, PetalCount)
#
#   randint(1, 6)
#     Returned value may be: "4";
#
#   choise("Python", "HTML", "JavaScript")
#     Returned value may be: "Python";
#
# ---------------------------------------------------------------------

for i in range(4):
    draw_flower(30, i * 100 + 50, i * 20, choice(colors), choice(colors), randint(-90, 180), randint(5, 7))
    draw_flower(30, i * -100 - 50, i * 20, choice(colors), choice(colors), randint(-90, 180), randint(5, 6))

for i in range(3):
    draw_flower(35, i * 100 + 80, i * 20 - 120, choice(colors), choice(colors), randint(-90, 180), randint(5, 7))
    draw_flower(35, i * -100 - 80, i * 20 - 120, choice(colors), choice(colors), randint(-90, 180), randint(5, 7))

for i in range(3):
    draw_flower(40, i * 100 + 70, i * 20 - 250, choice(colors), choice(colors), randint(-90, 180), randint(5, 7))
    draw_flower(40, i * -100 - 70, i * 20 - 250, choice(colors), choice(colors), randint(-90, 180), randint(5, 7))

draw_stick(0, -50)
draw_flower(40, 0, -50, "navy", "cyan", 0, 7)

print("Finished")

t.mainloop()
