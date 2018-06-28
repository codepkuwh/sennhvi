# coding:utf-8
from turtle import *


def m_goto(x, y):
    penup()
    goto(x, y)
    pendown()


def nose(x, y):
    color((255, 155, 192), "pink")
    m_goto(x, y)
    setheading(-30)
    begin_fill()
    a = 0.4
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            left(3)
            forward(a)
        else:
            a = a - 0.08
            left(3)
            forward(a)
    end_fill()

    penup()
    setheading(90)
    forward(25)
    setheading(0)
    forward(10)
    pendown()
    pencolor(255, 155, 192)
    setheading(10)
    begin_fill()
    circle(5)
    color(160, 82, 45)
    end_fill()

    penup()
    setheading(0)
    forward(20)
    pendown()
    pencolor(255, 155, 192)
    setheading(10)
    begin_fill()
    circle(5)
    color(160, 82, 45)
    end_fill()


def head(x, y):
    color((255, 155, 192), "pink")
    setheading(0)
    m_goto(x, y)
    begin_fill()
    setheading(180)
    circle(300, -30)
    circle(100, -60)
    circle(80, -100)
    circle(150, -20)
    circle(60, -95)
    setheading(161)
    circle(-300, 15)
    m_goto(-100, 100)
    setheading(-30)
    a = 0.4
    for i in range(60):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            lt(3)
            fd(a)
        else:
            a = a - 0.08
            lt(3)
            fd(a)
    end_fill()


def ears(x, y):
    color((255, 155, 192), "pink")
    m_goto(x, y)
    begin_fill()
    setheading(100)
    circle(-50, 50)
    circle(-10, 120)
    circle(-50, 54)
    end_fill()

    penup()
    setheading(90)
    forward(-12)
    setheading(0)
    forward(30)
    pendown()
    begin_fill()
    setheading(100)
    circle(-50, 50)
    circle(-10, 120)
    circle(-50, 56)
    end_fill()


def eyes():
    color((255, 155, 192), "white")
    penup()
    setheading(90)
    forward(-20)
    setheading(0)
    forward(-95)
    pendown()
    begin_fill()
    circle(15)
    end_fill()

    color("black")
    penup()
    setheading(90)
    forward(12)
    setheading(0)
    forward(-3)
    pendown()
    begin_fill()
    circle(3)
    end_fill()

    color((255, 155, 192), "white")
    penup()
    seth(90)
    forward(-25)
    seth(0)
    forward(40)
    pendown()
    begin_fill()
    circle(15)
    end_fill()

    color("black")
    penup()
    setheading(90)
    forward(12)
    setheading(0)
    forward(-3)
    pendown()
    begin_fill()
    circle(3)
    end_fill()


def cheek(x, y):
    color((255, 155, 192))
    m_goto(x, y)
    setheading(0)
    begin_fill()
    circle(30)
    end_fill()


def mouth(x, y):
    color(239, 69, 19)
    m_goto(x, y)
    setheading(-80)
    circle(30, 40)
    circle(40, 80)


def body(x, y):
    color((118, 44, 69), (198, 55, 99))
    m_goto(x, y)

    begin_fill()
    setheading(-140)
    circle(140, 50)
    forward(40)
    left(90)
    forward(200)
    left(90)
    forward(40)
    circle(140, 50)
    setheading(-160)
    circle(-140, 41)
    end_fill()


def hand(is_left, x, y):
    color(0, 0, 0)
    m_goto(x, y)
    if is_left:
        setheading(-170)
        circle(140, 30)
        tmp_x, tmp_y = position()
        circle(140, 7)
        m_goto(tmp_x, tmp_y)
        left(15)
        circle(140, 5)
        m_goto(tmp_x, tmp_y)
        right(60)
        circle(140, 7)
    else:
        setheading(-10)
        circle(-140, 30)
        tmp_x, tmp_y = position()
        circle(-140, 7)
        m_goto(tmp_x, tmp_y)
        right(15)
        circle(-140, 5)
        m_goto(tmp_x, tmp_y)
        left(60)
        circle(-140, 7)


def foot(x, y):
    color(0, 0, 0)
    m_goto(x, y)
    setheading(-90)
    forward(50)
    right(90)
    begin_fill()
    forward(40)
    setheading(130)
    circle(-10, 90)
    right(50)
    forward(38)
    end_fill()


def setting():
    pensize(4)
    hideturtle()
    colormode(255)
    color((255, 155, 192), "pink")
    setup(840, 500)
    speed(10)


def main():
    setting()
    body(-10, -25)
    hand(True, -35, -50)
    hand(False, 115, -50)
    foot(0, -175)
    foot(80, -175)
    nose(-100, 100)
    head(-69, 167)
    ears(0, 160)
    eyes()
    cheek(80, 10)
    mouth(-20, 30)
    done()


if __name__ == '__main__':
    main()
