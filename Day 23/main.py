import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.onkey(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.create_car()
    car_manager.move_cars()

    # check collide
    if car_manager.check_collide(player):
        game_is_on = False

    if player.has_arrived():
        player.goto_start()
        scoreboard.add_point()
        scoreboard.update_score()
        car_manager.increase_speed()
    screen.update()

scoreboard.game_over()

screen.exitonclick()
