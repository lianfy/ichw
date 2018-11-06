import turtle
import math
a = turtle.Turtle()
a.color("yellow")
a.shape("circle")
b = turtle.Turtle()
b.color("blue")
b.shape("circle")
c = turtle.Turtle()
c.color("green")
c.shape("circle")
d = turtle.Turtle()
d.color("red")
d.shape("circle")
e = turtle.Turtle()
e.color("black")
e.shape("circle")
f = turtle.Turtle()
f.color("orange")
f.shape("circle")
g = turtle.Turtle()
g.color("lightblue")
g.shape("circle")


def orbit(t, x):
    t.up()
    t.fd(x)
    t.down()


def mov(t, x, y, i):
     t.goto(x*math.cos(math.radians(4*10**6*i/(x+y)**3)), y*math.sin(math.radians(4*10**6*i/(x+y)**3)))


orbit(a, 0)
orbit(b, 68.32)
orbit(c, 85.34)
orbit(d, 100.8)
orbit(e, 129.1)
orbit(f, 233.6)
orbit(g, 318.1)
for i in range(1500):
    mov(b, 68.32, 55.45, i)
    mov(c, 85.34, 84.76, i)
    mov(d, 100.8, 99.16, i)
    mov(e, 129.1, 117.5, i)
    mov(f, 233.6, 222.5, i)
    mov(g, 318.1, 300.1, i)
turtle.mainloop()
#  由开普勒第三定律，w^2正比于r^-3,所以w正比于r^-3/2
#  本题x，y取100*r^1/2，单位为天文单位
