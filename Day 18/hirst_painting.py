import turtle as t
import random as r

color_list = [(207, 160, 82), (54, 89, 130), (145, 91, 40), (140, 26, 49), (222, 206, 108), (132, 176, 203), (45, 55, 104), (158, 46, 83), (169, 160, 39), (129, 189, 143), (83, 20, 44), (38, 43, 66), (186, 94, 107),
              (186, 140, 169), (85, 120, 180), (59, 39, 31), (88, 157, 92), (79, 153, 165), (195, 79, 72), (161, 201, 219), (45, 74, 77), (79, 74, 44), (58, 125, 122), (218, 175, 187), (167, 206, 167), (220, 182, 168)]
space = 50
n_columns = 14
n_rows = 14
bottom_left = (0.00 - (space * n_columns)/2, 0.00 - (space * n_rows)/2)

timmy = t.Turtle()
timmy.speed("fastest")
timmy.hideturtle()
t.colormode(255)
timmy.pensize(20)
timmy.penup()

timmy.goto(bottom_left[0], bottom_left[1])

for row in range(n_rows):
    for _ in range (n_columns):
        timmy.color(r.choice(color_list))
        timmy.pendown()
        timmy.forward(0)
        timmy.penup()
        timmy.forward(space)
    if row != n_rows-1:
        timmy.goto(bottom_left[0], bottom_left[1]+ 50*(row + 1))
    else:
        timmy.goto(0, 0)
        
screen = t.Screen().exitonclick()
