from turtle import Turtle, Screen
import random


def getAngle(number_of_sides):
    return 360 / number_of_sides


def getRandomColor():

    R = random.random()
    G = random.random()
    B = random.random()

    return R, G, B


timmy = Turtle()

for side_number in range(3, 11):
    colors = getRandomColor()
    timmy.color((colors[0], colors[1], colors[2]))
    angle = getAngle(side_number)
    for _ in range(side_number):
        timmy.forward(100)
        timmy.right(angle)


screen = Screen().exitonclick()
