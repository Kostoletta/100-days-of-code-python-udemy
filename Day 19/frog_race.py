import turtle as t
import random as r

color_list = ["red", "green", "blue", "purple", "yellow", "orange"]
turtle_list = []
is_race_on = False

screen = t.Screen()
screen.setup(width=500, height=400)

guess = screen.textinput(title="Make your guess!",
                         prompt="Wich turtle will win?")

for turtle in range(6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.speed(0)
    new_turtle.color(color_list[turtle])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-125 + 50*turtle)
    new_turtle.speed("normal")
    turtle_list.append(new_turtle)

if guess:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        turtle.forward(r.randint(0,10))
        if turtle.xcor() > 230:
            is_race_on = False
            if turtle.pencolor() == guess:
                print(f"You have won! The {turtle.pencolor()} turtle has won!")
            else:
                print(f"You have lost! The {turtle.pencolor()} turtle has won!")


screen.exitonclick()
