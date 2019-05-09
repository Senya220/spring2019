import turtle as t
import rainbow as r

t.goto(-300, -100)
r.move_l(600)


t.goto(300, -100)
r.rainbow(600)
t.turtlesize(2)
t.goto(0, -100)

num = 500
for i in range(num):
    t.color('#00004d', (r.calculate_y1(num, 255, i), r.calculate_y2(num, 255, i), r.calculate_y3(num, 255, i)))

t.mainloop()
