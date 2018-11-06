#!/usr/bin/env python3

"""planets.py: Description of what planets does.

__author__ = "Lian Feiyue"
__pkuid__  = "1800011733"
__email__  = "1800011733@pku.edu.cn"
"""

import turtle
import math
a = turtle.Turtle()
b = turtle.Turtle()
c = turtle.Turtle()
d = turtle.Turtle()
e = turtle.Turtle()
f = turtle.Turtle()
g = turtle.Turtle()


def orbit(t, co, x):
    """行星起始轨道位置
    """
    t.color(co)
    t.shape("circle")
    t.speed(0)
    t.up()
    t.fd(x)
    t.down()


def mov(t, x, y, e):
    """m为椭圆的半长轴，n为椭圆的半短轴，e为离心率
    """
    m = (x-y)/2+(x+y)/2*math.cos(math.radians(10**7*i/(x+y)**3))
    n = (x+y)/2*(1-e**2)**0.5*math.sin(math.radians(10**7*i/(x+y)**3))
    t.goto(m, n)


orbit(a, "yellow", 0)
orbit(b, "blue", 68.32)
orbit(c, "green", 85.34)
orbit(d, "red", 100.8)
orbit(e, "black", 129.1)
orbit(f, "orange", 233.6)
orbit(g, "lightblue", 318.1)
for i in range(10000):
    mov(b, 68.32, 55.45, 0.206)
    mov(c, 85.34, 84.76, 0.007)
    mov(d, 100.8, 99.16, 0.017)
    mov(e, 129.1, 117.5, 0.093)
    mov(f, 233.6, 222.5, 0.048)
    mov(g, 318.1, 300.1, 0.056)
turtle.mainloop()
#  由开普勒第一定律，太阳在行星椭圆轨道的一个焦点上
#  由开普勒第三定律，w^2正比于r^-3,所以w正比于r^-3/2
#  本题x，y取100*r^1/2，单位为天文单位
