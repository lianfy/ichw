import turtle
import math
a = turtle.Turtle()
b = turtle.Turtle()
c = turtle.Turtle()
d = turtle.Turtle()
e = turtle.Turtle()
f = turtle.Turtle()
g = turtle.Turtle()


def orbit(t, c, x):
    t.color(c)
    t.shape("circle")
    t.speed(0)
    t.up()
    t.fd(x)
    t.down()


def mov(t, x, y, i):
    t.goto(x*math.cos(math.radians(4*10**6*i/(x+y)**3)), y*math.sin(math.radians(4*10**6*i/(x+y)**3)))


orbit(a, "yellow", 0)
orbit(b, "blue", 68.32)
orbit(c, "green", 85.34)
orbit(d, "red", 100.8)
orbit(e, "black", 129.1)
orbit(f, "orange", 233.6)
orbit(g, "lightblue", 318.1)
for i in range(20000):
    mov(b, 68.32, 55.45, i)
    mov(c, 85.34, 84.76, i)
    mov(d, 100.8, 99.16, i)
    mov(e, 129.1, 117.5, i)
    mov(f, 233.6, 222.5, i)
    mov(g, 318.1, 300.1, i)
turtle.mainloop()
#  由开普勒第三定律，w^2正比于r^-3,所以w正比于r^-3/2
#  本题x，y取100*r^1/2，单位为天文单位
