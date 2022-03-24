import turtle
import math


def house():
    size = int(input('Введите размер дома (макимум - 100): '))
    screen = turtle.getscreen()
    t = turtle.Turtle()
    for i in range(4):
        t.forward(size)
        t.left(90)
    t.forward(size/2)
    t.left(90)
    t.forward(size/2)
    t.right(90)
    t.forward(size/4)
    t.right(90)
    t.forward(size/2)
    t.left(90)
    t.forward(size/4)
    t.left(90)
    t.forward(size)
    t.left(45)
    t.forward(math.sqrt(2*pow(size/2, 2)))
    t.left(90)
    t.forward(math.sqrt(2 * pow(size / 2, 2)))

    screen.mainloop()


house()
