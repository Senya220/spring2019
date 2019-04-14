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



def draw_flower(size, x, y, color, color_center, angle):
    print(str("Drawing " + color + " flower with " + color_center + " center."))
    t.goto(x, y)

    t.setheading(angle)
    t.forward(size * 2.5)
    t.setheading(angle + 90)
    draw_circle(color, size)
    t.goto(x, y)

    t.setheading(angle + 90)
    t.forward(size * 2.5)
    t.setheading(angle + 180)
    draw_circle(color, size)
    t.goto(x, y)

    t.setheading(angle + 180)
    t.forward(size * 2.5)
    t.setheading(angle + 270)
    draw_circle(color, size)
    t.goto(x, y)

    t.setheading(angle + 270)
    t.forward(size * 2.5)
    t.setheading(angle + 360)
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


colors = ["magenta", "cyan", "navy", "blue", "red", "yellow", "orange", "green"]

# --------------------

t.bgcolor("cyan")
t.hideturtle()
t.penup()
t.speed(0)

# draw_sun()


# draw_flower(50, 40, 40, "green", "yellow")
# draw_flower(70, -140, -140, "black", "green")
# draw_flower(50, 0, -100, "pink", "navy")
# draw_flower(50, 80, 145, "navy", "cyan")
# draw_flower(50, 100, -150, "orange", "yellow")
i = 50

draw_sun()

for g in range(i):
    i = i+1
    draw_flower(randint(10, 40), randint(-300, 300), randint(-300, 50), choice(colors), choice(colors), randint(0, 90))
    w.sleep(0.0001)

print("Finished")
t.exitonclick()
