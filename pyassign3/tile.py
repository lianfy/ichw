#!/usr/bin/env python3

"""tiles.py: Description of how to pave tiles.

__author__ = "Lian Feiyue"
__pkuid__  = "1800011733"
__email__  = "1800011733@pku.edu.cn"
"""

import turtle


def conflict(a, b, c, d, x, y, count):
    """定义冲突函数，
    如不冲突，可以铺x方向长度为c
    y方向长度为d的一块砖
    count函数用来标记该砖是否被铺过
    没铺过为"ym"，铺过为"ymwc"
    """
    if y + d <= b and x + c <= a:
        for i in range(y, y + d):
            for j in range(x, x + c):
                if count[i * a + j] == "ymwc":
                    return True
        return False
    else:
        return True


def pave(a, c, d, x, y, count, s, ans):
    """定义铺砖函数
    铺x方向长度为c，y方向长度为d的一块砖
    并在count函数中标记之
    最后将砖块坐标传入ans
    """
    for i in range(y, y + d):
        for j in range(x, x + c):
            count[i * a + j] = "ymwc"
            s.append(i * a + j)
    ans.append(tuple(s))


def tile(a, b, c, d, count, alls=[], ans=[], x=0, y=0):
    """a为墙长，b为墙宽
    c为砖长，d为砖宽
    ans中储存每一种铺法的砖块坐标
    alls中储存所有铺法的砖块坐标
    当c=d时可简化算法
    """
    s = []
    if c == d:
        if not conflict(a, b, c, d, x, y, count):
            pave(a, c, d, x, y, count, s, ans)
            if "ym" in count:
                p = count.index("ym")
                tile(a, b, c, d, count, alls, ans, y=p // a, x=p % a)  # 下一块砖从x=p%a，y=p//a开始铺
            else:
                alls.append(ans)
    else:
        if not conflict(a, b, c, d, x, y, count) and not conflict(a, b, d, c, x, y, count):
            ans_1 = ans[:]  # 既可以横铺也可以竖铺时，复制列表，分别递归
            s_1 = s[:]
            count_1 = count[:]
            pave(a, c, d, x, y, count, s, ans)
            if "ym" in count:
                m = count.index("ym")
                tile(a, b, c, d, count, alls, ans, y=m // a, x=m % a)
            else:
                alls.append(ans)
            pave(a, d, c, x, y, count_1, s_1, ans_1)
            if "ym" in count_1:
                n = count_1.index("ym")
                tile(a, b, c, d, count_1, alls, ans_1, y=n // a, x=n % a)
            else:
                alls.append(ans_1)
        elif not conflict(a, b, c, d, x, y, count):
            pave(a, c, d, x, y, count, s, ans)
            if "ym" in count:
                m = count.index("ym")
                tile(a, b, c, d, count, alls, ans, y=m // a, x=m % a)
            else:
                alls.append(ans)
        elif not conflict(a, b, d, c, x, y, count):
            pave(a, d, c, x, y, count, s, ans)
            if "ym" in count:
                m = count.index("ym")
                tile(a, b, c, d, count, alls, ans, y=m // a, x=m % a)
            else:
                alls.append(ans)
    return alls


def draw(a, b, method):
    """定义t1,t2,t3三只乌龟
    t1画网格，先画行后画列
    t2通过读取method（即alls[e]）中的数据
    计算每一块砖x和y的最大最小坐标
    四个顶点连线即为砖块
    t3给砖块编号
    """
    t1 = turtle.Turtle()
    t2 = turtle.Turtle()
    t3 = turtle.Turtle()
    t1.speed(0)
    t2.speed(0)
    t3.speed(0)
    t1.color("blue")
    t2.pensize(10)
    t3.color("blue")
    t = 250 / (a*b)**0.5
    for row in range(0, b+1):
        t1.up()
        t1.goto(-t * a, 2 * t * row - t * b )
        t1.down()
        t1.fd(2 * t * a)
    t1.lt(90)
    for column in range(0, a+1):
        t1.up()
        t1.goto(2 * t * column - t * a, -t * b)
        t1.down()
        t1.fd(2 * t * b)  # 墙的左下角坐标为(-at,-bt)，右上角坐标为(at,bt)
    for i in method:
        m = max(i)
        n = min(i)
        t2.up()
        x_min = 2 * (n % a) * t - a * t
        y_min = 2 * (n // a) * t - b * t
        x_max = (2 + 2 * (m % a)) * t - a * t
        y_max = (2 + 2 * (m // a)) * t - b * t
        t2.goto(x_min, y_min)
        t2.down()
        t2.goto(x_max, y_min)
        t2.goto(x_max, y_max)
        t2.goto(x_min, y_max)
        t2.goto(x_min, y_min)
    for p in range(a):
        for q in range(b):
            t3.up()
            t3.goto(-(a-1) * t + 2 * p * t, -(b-1) * t + 2 * q * t)
            t3.down()
            t3.write(str(q * a + p), align="center", font=("微软雅黑", int(t/5), "bold"))
    turtle.mainloop()


def main():
    a = int(input("墙长："))
    b = int(input("墙宽："))
    c = int(input("砖长："))
    d = int(input("砖宽："))
    count = ["ym"] * (a*b)
    alls = tile(a, b, c, d, count)
    num = len(alls)
    for i in alls:
        print(i)
    print("共有" + str(num) + "种方案")
    if num > 0:
        e = int(input("请选择第X种方案："))
        draw(a, b, alls[e])


if __name__ == "__main__":
    main()
