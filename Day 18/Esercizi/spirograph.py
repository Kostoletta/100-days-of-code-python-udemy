import turtle as t
import random as r

def getRandomColor():
    return (r.randint(0,255), r.randint(0,255), r.randint(0,255))

timmy = t.Turtle()
timmy.speed("fastest")
t.colormode(255)

number_of_circles = 200

for i in range(number_of_circles):
    timmy.color(getRandomColor())
    timmy.circle(100)
    timmy.right(360 / number_of_circles)


screen = t.Screen()
screen.exitonclick()