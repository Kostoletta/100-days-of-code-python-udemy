import random as r
import turtle as t
from turtle import Screen


def getRandomColor():
    return (r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))


def getRandomDirection():
    return r.choice([0, 90, -90, 180])


timmy = t.Turtle()
t.colormode(255)
timmy.pensize(10)
timmy.speed("fastest")

for _ in range(200):
    timmy.color(getRandomColor())
    timmy.forward(20)
    timmy.setheading(getRandomDirection())


screen = Screen()
screen.exitonclick()
