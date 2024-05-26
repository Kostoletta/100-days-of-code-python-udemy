import random
from turtle import Turtle

from snake import MOVE_DISTANCE


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed(0)
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(x=rand_x - (rand_x % MOVE_DISTANCE), y=rand_y - (rand_y % MOVE_DISTANCE))

    def refresh(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(x=rand_x - (rand_x % MOVE_DISTANCE), y=rand_y - (rand_y % MOVE_DISTANCE))
