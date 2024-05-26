from turtle import Turtle, Screen

timmy = Turtle()

for _ in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()


screen = Screen()
screen.exitonclick()