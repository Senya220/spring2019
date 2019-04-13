#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import turtle as t
import time as w
from random import randint, choice

# Functions:


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


def draw_flower(size, x, y, color, color_center):
    print(str("Drawing " + color + " flower with " + color_center + " center."))
    t.goto(x+size, y+size)
    t.pendown()
    draw_square(color, size)
    t.goto(x-size, y-size)
    draw_square(color, size)
    t.goto(x-size, y+size)
    draw_square(color, size)
    t.goto(x+size, y-size)
    draw_square(color, size)
    t.goto(x, y)
    t.color(color)
    draw_square(color_center, size)
    t.shape("turtle")
    t.hideturtle()
    t.penup()


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


colors = ["black", "cyan", "navy", "blue", "red", "yellow", "orange", "green"]

# --------------------

t.speed(0)

# draw_sun()


# draw_flower(50, 40, 40, "green", "yellow")
# draw_flower(70, -140, -140, "black", "green")
# draw_flower(50, 0, -100, "pink", "navy")
# draw_flower(50, 80, 145, "navy", "cyan")
# draw_flower(50, 100, -150, "orange", "yellow")
i = 10000000

for g in range(i):
    i = i+1
    draw_flower(randint(50, 100), randint(-300, 300), randint(-300, 300), choice(colors), choice(colors))
    w.sleep(0.0001)

# r.randint(-300, 300)
t.exitonclick()
