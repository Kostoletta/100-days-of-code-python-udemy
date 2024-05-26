import turtle as t


def forward():
    timmy.forward(5)


def backward():
    timmy.back(5)


def left():
    timmy.left(5)


def right():
    timmy.right(5)


def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


timmy = t.Turtle()

screen = t.Screen()
screen.listen()
screen.onkey(fun=forward, key="w")
screen.onkey(fun=backward, key="s")
screen.onkey(fun=left, key="a")
screen.onkey(fun=right, key="d")
screen.onkey(fun=clear , key="c")

screen.exitonclick()
