#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Техническое задание:
На основе цветочка из квадратов, сделанного в первой итерации,
нарисовать картину из этого цветочка и солнышка.
Солнышко такое как тут, подойдет https://docs.python.org/3.7/library/turtle.html
В будущем ожидаю увидеть поле из разных цветов. Может, сделать цветок красивее.
"""

import turtle as t


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


def draw_flower(size):
    t.goto(60, 60)
    t.pendown()
    draw_square('purple', size)
    t.goto(-60, -60)
    draw_square('orange', size)
    t.goto(-60, 60)
    draw_square('pink', size)
    t.goto(60, -60)
    draw_square('blue', size)
    t.goto(0, 0)
    t.color('blue')
    draw_square('yellow', size)
    t.shape("turtle")
    t.hideturtle()
    t.penup()


t.speed(10)

# ------------------------
t.penup()
t.goto(-200, 200)
a = abs(t.pos())
t.pendown()
t.color('red', 'yellow')
t.begin_fill()
while True:
    t.forward(200)
    t.left(170)
    b = abs(t.pos())
    if a - 1 < b < a + 1:
        break
t.penup()
t.end_fill()

# ------------------------


draw_flower(70)

t.exitonclick()
