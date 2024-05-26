from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
SCREEN_COLOR = "black"

screen = Screen()
screen.title("Pong")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(SCREEN_COLOR)
screen.tracer(0)
screen.listen()

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

scoreboard = ScoreBoard()

ball = Ball(scoreboard)

screen.update()

screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")

game_is_on = True

while game_is_on:
    ball.move()
    ball.check_collide_with_wall()

    if ball.distance(r_paddle.pos()) < 50 and ball.xcor() > r_paddle.xcor() - 10 or ball.distance(
            l_paddle.pos()) < 50 and ball.xcor() < l_paddle.xcor() + 10:
        ball.bouncex()

    screen.update()

screen.exitonclick()
