import turtle as t


# def draw_square():
#     color('black', 'red')
#     forward(50)
#     left(90)
#     forward(50)
#     left(90)
#     forward(50)
#     left(90)
#     forward(50)
#     left(90)

# def draw_spiral(radius):
#     original_xcor = xcor()
#     original_ycor = ycor()
#     speed = 1
#     while True:
#         forward(speed)
#         left(10)
#         speed += 0.1
#         if distance(original_xcor, original_ycor) > radius:
#             break

def draw_shape(sides, length):
    t.begin_fill()
    for _ in range(sides):
        t.forward(length)
        t.right(360 / sides)
    t.end_fill()


def draw_matrix(matrix):
    startX = -250
    startY = 200
    shapeSide = 50
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            cell = matrix[row][col]
            if cell == 1:
                t.fillcolor("red")
            else:
                t.fillcolor("black")
            curX = startX + shapeSide * col
            curY = startY - shapeSide * row
            t.goto(curX, curY)
            draw_shape(4, shapeSide)


matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
          [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
          [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


t.setup(width=600, height=600, startx=0, starty=0)
t.color('black')
t.hideturtle()

t.speed(0)
t.penup()
draw_matrix(matrix)

t.exitonclick()
