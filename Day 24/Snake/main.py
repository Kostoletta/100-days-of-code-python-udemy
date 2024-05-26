import time
from turtle import Screen as S
from scoreboard import ScoreBoard
from food import Food
from snake import Snake

UPDATE_SPEED = 0.1  # sec

game_is_on = True

screen = S()
screen.setup(width=590, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake")
screen.listen()

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)

while game_is_on:
    screen.update()
    time.sleep(UPDATE_SPEED)

    if snake.eats(food):
        food.refresh()
        snake.add_segment()
        scoreboard.increase_score()

    snake.move()

    if snake.has_collided():
        scoreboard.reset()
        snake.reset()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

screen.exitonclick()
