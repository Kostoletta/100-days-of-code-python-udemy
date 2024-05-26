import turtle
from turtle import Screen

import pandas

data = pandas.read_csv("50_states.csv")
data_list = data["state"].to_list()
print(data_list)

img = "blank_states_img.gif"

screen = Screen()
screen.addshape(img)

turtle.shape(img)

screen.title("U.S. states game")
game_is_on = True
state_count = 0
while game_is_on:
    answer = screen.textinput(title=f"{state_count}/50 Guess the State", prompt="What's another state name?").title()

    if answer in data_list:
        state_count += 1
        y_coord = data[data["state"] == answer].y.item()
        x_coord = data[data["state"] == answer].x.item()
        data_list.pop(data_list.index(answer))
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x_coord, y_coord)
        t.write(answer)
    if answer == "Exit":
        missing_states = pandas.DataFrame(data_list)
        missing_states.to_csv("states_to_learn.csv")
        game_is_on = False

turtle.mainloop()
